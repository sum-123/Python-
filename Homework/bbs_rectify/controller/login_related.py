from common.utility import *
from flask import request, Blueprint
from flask_cors import *
from database import User

identification = Blueprint('identification', __name__)

@identification.route('/register', methods = ["GET", "POST"])
def register():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    avatar = request.get_json().get('avatar')
    if len(User.through_username(username)) > 0:
        return 'repetition'
    User.register(username, password, avatar)
    return 'success'

@identification.route('/login', methods = ['GET', 'POST'])
def login():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    res = User.through_username(username)
    if len(res) != 1:
        return 'invalid'
    if password == res[0].password:
        token = generate_access_token(username)
        dic = {
            '0':'success',
            '1': res[0].avatar,
            '2': token
        }
        return dic
    else:
        return 'fail'