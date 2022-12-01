from datetime import datetime
import pytz


class DateUtil:
    """
    时间工具类
    """

    @staticmethod
    def today() -> str:
        """
        当前时间 UTC+8 (格式: %Y-%m-%d)
        """
        return DateUtil.now('%Y-%m-%d')

    @staticmethod
    def now(date_format='%Y-%m-%d %H:%M:%S'):
        """
        当前时间 UTC+8 (格式: %Y-%m-%d %H:%M:%S)
        """
        timezone = pytz.timezone('Asia/Shanghai')
        return datetime.now(timezone).strftime(date_format)

    @staticmethod
    def format_date(date_str: str):
        """
        对时间进行格式化
        """
        return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
