from flask import Blueprint
from .model import User

user_api = Blueprint('user_api', __name__, url_prefix='/api/users')


@user_api.route('/')
def hello_user():
    users = User.query.all()
    print(users)
    return '用户列表'
