from werkzeug.security import safe_str_cmp
from RestAPI.models.user import UserModel
from flask_jwt import JWT,JWTError

def authenticate(username,password):
    '''
    function that get called when user calls the  /auth end point
    :param username:
    :param password:
    :return: a UserModel object if the function run successful
    '''
    user=UserModel.find_by_name(username)
    if user and safe_str_cmp(user.password,password):
        return user
    return None

def identity(payload):

    '''
    ' function that gets called when user alreadu authenticated
    :param payload: a dictionary  with identity key which is user id
    :return: usermodel if the username identified
    '''

    user_id =payload['identity']
    return UserModel.find_by_id(user_id)


