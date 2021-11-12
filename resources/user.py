from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message":f"User with the name {data['username']} already exits"}, 403
        
        # user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()
        return {"message":"User created succesfully."}, 201
    
    def delete(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            user.delete_from_db()
            return {"message":f"User with name {data['username']} deleted successfully"}, 200
        
        return {'message':'User not exists'}, 404
