from flask_restful import Resource,reqparse
from RestAPI.models.user import UserModel

class UserRegister(Resource):

    parser=reqparse.RequestParser()

    parser.add_argument('username',type=str,
                        required=True,help="this field can not be blank")
    parser.add_argument('password',type=str,
                        required=True,help="this field can not be blank")



    def post(self):
        data=UserRegister.parser.parse_args()


        if UserModel.find_by_name(data['username']):
           return {'message' : 'User with name allready exist'},400

        user=UserModel(**data)
        user.save_to_db()
        return {'message':"User created with the inputs provided"},201






