import io
from PIL import Image, ImageDraw, ImageFont


class ImageUtil:
    """
    图片工具类
    """

    @staticmethod
    def generate_image_placeholder(width: int, height: int, text: str, text_size: int, text_color: str,
                                   background_color: str) -> io.BytesIO:
        """
        生成占位图片

        :param width: 背景图片的宽度
        :param height: 背景图片的高度
        :param text: 填充的文字
        :param text_size: 文字大小
        :param text_color: 文字颜色
        :param background_color: 背景颜色

        :return 图片字节
        """

        # 生成图片
        new_image = Image.new(mode='RGBA', size=(width, height), color=background_color)
        image_draw = ImageDraw.Draw(new_image)
        # 字体
        font = ImageFont.truetype("static/font/SourceHanSansCN-Normal.otf", text_size)
        # 文字的宽度
        text_width = font.getlength(text)
        # 计算居中大小
        x = width / 2 - text_width / 2
        y = height / 2 - text_size / 2
        # 填充文字
        image_draw.text((x, y), text, font=font, fill=text_color)
        # 保存到 IO 流中
        image_bytes = io.BytesIO()
        new_image.save(image_bytes, 'PNG', quality=100)

        image_bytes.seek(0)
        # 关闭图片流, 此操作将销毁图像并释放其内存
        new_image.close()
        # 返回
        return image_bytes
