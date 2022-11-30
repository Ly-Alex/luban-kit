import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 从配置文件中加载配置, 并覆盖已加载的配置信息
SETTINGS_FILE_PATH = os.path.join(BASE_DIR, 'settings.py')
