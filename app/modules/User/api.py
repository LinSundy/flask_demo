from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/user/<name_id>')
def hello_user(name_id):
    return '您的id是%s' % name_id
