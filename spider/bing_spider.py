# coding:utf-8

from datetime import datetime
import jsonpath as jp
import requests


class BingSpider:
    """
    必应壁纸爬虫
    """

    def __init__(self, date_str: str, resolution: str):
        """
        获取今日的必应壁纸 json 数据

        :param resolution: 分辨率
        :param date_str: 时间(默认值:今日时间[格式:%Y-%m-%d])
        :return: 必应壁纸 Json 数据 或 bool
        """
        # 时间
        self.date_str = date_str
        # 分辨率
        self.resolution = resolution
        # 必应地址
        self.bing_url = 'https://cn.bing.com'
        # 必应壁纸路径
        self.wallpaper_url = self.bing_url + '/HPImageArchive.aspx?format=js&n=1&mkt=zh-CN&uhd=1&idx=' + \
                             str(self.between())
        # 请求头
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36'
        }

    def between(self):
        """
        时间间隔
        """
        local_date = datetime.now()
        custom_date = datetime.strptime(self.date_str, '%Y-%m-%d')
        interval_day = (local_date - custom_date).days
        return interval_day

    def get_data(self, url: str):
        """
        从接口获取数据
        """
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                return False
        except (Exception,):
            return False

    def parse_json(self, crude_json):
        """
        解析接口返回的json数据
        """
        # 获取原始数据
        url = jp.jsonpath(crude_json, '$.images[0].url')[0]
        url_base = jp.jsonpath(crude_json, '$.images[0].urlbase')[0]
        copy_right = jp.jsonpath(crude_json, '$.images[0].copyright')[0]
        end_date = jp.jsonpath(crude_json, '$.images[0].enddate')[0]
        title = jp.jsonpath(crude_json, '$.images[0].title')[0]

        # 处理图片后缀
        uhd_url = url.split('&', 1)[0]
        suffix = uhd_url.rsplit('.', 1)[-1]

        # 拼接数据
        url = self.bing_url + url_base + '_' + self.resolution + '.' + suffix
        date = datetime.strptime(end_date, '%Y%m%d').strftime('%Y-%m-%d')

        return {'url': url, 'title': title, 'description': copy_right, 'date': date}

    def run(self):

        # 校验日期
        if self.between() > 7 or self.between() < 0:
            return False

        crude_json = self.get_data(self.wallpaper_url)
        if crude_json:
            dict_json = self.parse_json(crude_json)
            return dict_json
        else:
            return False


if __name__ == '__main__':
    bing = BingSpider('2022-11-22', '1920x1080')
    print_json = bing.run()
    print(print_json)
