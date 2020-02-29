from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from datetime import timedelta
from flask_caching import Cache

cache = Cache(
    config={
        'CACHE_TYPE': 'redis'
    }
)

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    app.permanent_session_lifetime = timedelta(seconds=30)
    Session(app)
    cache.init_app(app)
