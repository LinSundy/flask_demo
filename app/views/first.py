from flask import Blueprint, render_template
from ..models.User import User

first = Blueprint('first', __name__)


@first.route('/')
def first_fun():
    users = User.query.all()
    print(users)
    return render_template('index.html')


@first.route('/create_db/')
def hello():
    return '创建成功!'
