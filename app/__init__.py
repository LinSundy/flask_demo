from flask import Flask
from app.modules import init_views
from .ext import init_ext
from .setting import envs


def create_app(env):
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(envs.get(env))
    # 初始化第三方库
    init_ext(app)
    # 初始化路由
    init_views(app=app)
    return app
