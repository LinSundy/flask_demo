from flask import Blueprint, render_template, session
from app.ext import cache

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
def hello_user():
    return render_template('index.html')


@user.route('/set/')
def set_session():
    session['key'] = '小米'
    return 'ok'


@user.route('/set1/')
def set_session1():
    cache.set('key1', '小米1', timeout=30)
    return 'ok2'


@user.route('/show/')
def show_name():
    name = session.get('key')
    name2 = cache.get('key1')
    return render_template('index.html', name2=name2, name=name)
