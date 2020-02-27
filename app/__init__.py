from flask import Flask
from app.views import init_views
from .ext import init_ext
from .setting import envs


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_views(app=app)
    return app
