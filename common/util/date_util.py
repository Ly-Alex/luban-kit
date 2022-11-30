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
