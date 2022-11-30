from flask import Flask, render_template


def create_flask_app(default_config, enable_env_config_cover=False):
    """
    创建 Flask 对象

    :param default_config: 默认配置文件的对象
    :param enable_env_config_cover: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return: Flask 对象
    """
    app = Flask(__name__, static_folder='static')

    app.config.from_object(default_config)
    if enable_env_config_cover:
        from common.constant import SETTINGS_FILE_PATH
        app.config.from_pyfile(SETTINGS_FILE_PATH, silent=True)

    # Flask 对象
    return app


def handler_exception(app):
    """
    异常处理
    """

    @app.errorhandler(404)
    def handle_404(e):
        """
        404
        """
        return render_template('404.html')

    @app.errorhandler(500)
    def handle_500(e):
        """
        500
        """
        return render_template('500.html')

    @app.errorhandler(Exception)
    def handle_exception(e):
        """
        exception
        """
        return render_template('500.html')


def create_app(default_config, enable_env_config_cover=False):
    """
    创建 App

    :param default_config: 默认配置文件的对象
    :param enable_env_config_cover: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return: App 对象
    """
    app = create_flask_app(default_config, enable_env_config_cover)

    handler_exception(app)

    # 注册 bing 模块
    from resource.bing_wallpaper import bing_bp
    app.register_blueprint(bing_bp)

    return app
