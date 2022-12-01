import io
import uuid
import requests
from urllib.request import urlopen
from PIL import ImageFilter, Image
from deta import Deta
from flask import current_app as app, stream_with_context, send_file
from flask_restful import Resource, inputs
from flask_restful.reqparse import RequestParser
from common.enum import ResolutionEnum
from common.util import DateUtil
from spider.bing_spider import BingSpider


class BingWallpaperResource(Resource):
    """
    必应壁纸
    """

    def __init__(self):
        # 初始化存储资源
        _deta = Deta(app.config.get('PROJECT_KEY', None))
        self.bing_db = _deta.Base("bing_wallpaper")
        self.bing_oss = _deta.Drive("bing_wallpaper")

    def get(self):
        """
        获取壁纸
        """

        # 验证参数
        parser = RequestParser()
        parser.add_argument('r', dest='resolution', default=ResolutionEnum.R_1920x1080, type=ResolutionEnum,
                            location='args', help='分辨率格式不正确！')

        parser.add_argument('d', dest='date', default=DateUtil.today(), type=str, location='args',
                            help='日期格式不正确！')

        parser.add_argument('b', dest='blur', default=0, type=inputs.int_range(1, 100), location='args',
                            help='模糊值范围不正确！')

        # 解析参数
        args = parser.parse_args()
        resolution = args.get('resolution')
        date = args.get('date')
        blur = args.get('blur')

        # 格式化时间
        fmt_date = DateUtil.format_date(date)

        # 从数据库获取壁纸数据
        db_result = self.bing_db.fetch(query={'date': fmt_date, 'resolution': resolution.value, 'blur': blur},
                                       limit=1)

        # 数据库中存在, 直接返回数据库中的数据
        if len(db_result.items) != 0:
            item = db_result.items[0]
            file_name = item.get('file_name')
            wallpaper_streaming = self.bing_oss.get(file_name)

            # 返回数据库中的图片
            return app.response_class(
                stream_with_context(wallpaper_streaming.iter_chunks(1024 * 10)), mimetype='image/jpeg'
            )

        # 如果数据库中不存在, 则调用爬虫
        bing_spider = BingSpider(fmt_date, resolution)
        bing_json = bing_spider.run()

        image_format = 'jpeg'

        # 如果爬虫没有获取到数据,则生成一张临时图片
        if not bing_json:
            return '第三方接口没有数据'

        # 拼接字段
        bing_wallpaper_url = bing_json.get('url')
        key = uuid.uuid1().hex
        file_name = key + '.' + image_format

        # 保存爬虫数据到数据库
        self.bing_db.put(dict(bing_json, **{'resolution': resolution, 'blur': blur, 'file_name': file_name,
                                            'image_format': image_format, 'create_time': DateUtil.now(),
                                            'update_time': DateUtil.now(), }), key=key)

        # 如果图片需要模糊, 则使用 Pillow 库进行高斯模糊
        if blur != 0:
            gauss_image_bytes = io.BytesIO()

            # 请求必应图片接口
            ori_image = Image.open(urlopen(bing_wallpaper_url))
            gauss_image = ori_image.filter(ImageFilter.GaussianBlur(blur))
            gauss_image.save(gauss_image_bytes, image_format, quality=100)
            ori_image.close()
            gauss_image_bytes.seek(0)

            # 保存模糊处理后的图片到文件服务器
            self.bing_oss.put(file_name, gauss_image_bytes.getvalue())

            # 返回模糊的图片
            return send_file(gauss_image_bytes, mimetype='image/jpeg')

        # 请求必应图片接口
        response = requests.get(bing_wallpaper_url, stream=True)

        # 保存清晰的图片到文件服务器
        self.bing_oss.put(file_name, response.content)

        # 返回清晰的图片
        return app.response_class(
            stream_with_context(response.iter_content(chunk_size=1024 * 10)), mimetype='image/jpeg'
        )
