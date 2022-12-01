from deta import Deta
from flask import current_app as app
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common.enum import ResolutionEnum
from common.util import DateUtil


class BingJsonResource(Resource):
    """
    必应壁纸 Json
    """

    def __init__(self):
        # 初始化存储资源
        _deta = Deta(app.config.get('PROJECT_KEY', None))
        self.bing_db = _deta.Base("bing_wallpaper")

    def get(self):
        # 验证参数
        parser = RequestParser()

        parser.add_argument('r', dest='resolution', default=ResolutionEnum.R_1920x1080, type=ResolutionEnum,
                            location='args')
        parser.add_argument('d', dest='date', default=DateUtil.today(), type=str, location='args')
        parser.add_argument('b', dest='blur', default=None, type=str, location='args')
        parser.add_argument('la', dest='last', default=None, type=str, location='args')
        parser.add_argument('li', dest='limit', default=1, type=int, location='args')
        parser.add_argument('de', dest='description', default=None, type=str, location='args')
        parser.add_argument('t', dest='title', default=None, type=str, location='args')

        # 解析参数
        args = parser.parse_args()
        date = args.get('date')
        blur = args.get('blur')
        last = args.get('last')
        limit = args.get('limit')
        title = args.get('title')
        resolution = args.get('resolution')
        description = args.get('description')

        # 格式化时间
        fmt_date = DateUtil.format_date(date)

        res = self.bing_db.fetch(query=[{'blur': blur}, {'date': fmt_date}, {'resolution': resolution.value},
                                        {'title?contains': title}, {'description?contains': description}],
                                 limit=limit,
                                 last=last)

        return res.items
