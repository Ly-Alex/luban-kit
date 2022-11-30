import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'luban-kit'))

from common.config import DefaultConfig
from init import create_app

app = create_app(DefaultConfig, enable_env_config_cover=True)
