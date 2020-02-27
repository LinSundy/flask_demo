from .User.api import user


def init_views(app):
    app.register_blueprint(user)
