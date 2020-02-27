from .user.views import user
from .user.api import user_api


def init_views(app):
    app.register_blueprint(user)
    app.register_blueprint(user_api)
