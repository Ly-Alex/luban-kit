from flask import Blueprint
from flask_restful import Api
from . import bing_wallpaper, bing_json

# 蓝图
bing_bp = Blueprint('bing', __name__, url_prefix='/bing')
_bing_api = Api(bing_bp)

# 路由
_bing_api.add_resource(bing_wallpaper.BingWallpaperResource, '/', endpoint='BingWallpaper')
_bing_api.add_resource(bing_json.BingJsonResource, '/json', endpoint='BingJson')
