from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
def hello_user():
    return render_template('index.html')
