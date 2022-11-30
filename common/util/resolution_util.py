class ResolutionUtil:
    """
    分辨率工具类
    """

    # 特殊格式的分辨率
    special_format: dict[str, tuple[int, int]] = {
        'UHD': (3840, 2160),
        '720P': (1280, 720),
        '1080P': (1920, 1080),
        '2K': (2048, 1080),
        '4K': (3840, 2160),
        '8K': (7680, 4320),
    }

    @staticmethod
    def parse(resolution: str) -> tuple[int, int]:
        """
        解析字符串格式的分辨率 (默认值: 800x240)
        """
        resolution = resolution.upper()
        if 'X' in resolution or '*' in resolution:
            resolution = resolution.replace('*', 'X')
            width = int(resolution.split('X')[0])
            height = int(resolution.split('X')[1])
            return width, height
        else:
            return ResolutionUtil.special_format.get(resolution, (800, 240))
