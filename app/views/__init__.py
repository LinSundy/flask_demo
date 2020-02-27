from .first import first


def init_views(app):
    app.register_blueprint(first)

