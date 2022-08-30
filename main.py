import json
from flask import jsonify, request
from flask_restful import Resource
from models import User, app, api, db, Professional
from flask_bcrypt import generate_password_hash


class Get_All_Users(Resource):
    def get(self):
        user = User.query.all()
        print(user)
        return [user.json() for user in user]


class Register_User(Resource):
    def post(self):
        content = request.get_json()
        user = User(username=content['username'], email=content['email'],
                    password_hash=generate_password_hash(content['password']),
                    image_url=content['image_url'])
        db.session.add(user)
        db.session.commit()
        return "Data saved in Database", 200
        print(content, "---------------------------------------")


class Register_Pro(Resource):
    def post(self):
        content = request.get_json()
        pro = Professional(username=content['username'], email=content['email'],
                           password=generate_password_hash(content['password']),
                           calendly_url=content['calendly_url'], skill_level=content['skill_level'],
                           bio=content['bio'], category=content['category'], specialization=content['specialization'])
        db.session.add(pro)
        db.session.commit()
        return "Data saved in Database", 200


class Get_All_Pro(Resource):
    def get(self):
        pro = Professional.query.all()
        print(pro)
        return [pro.json() for pro in pro]


class status(Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


class Sum(Resource):
    def get(self, a, b):
        return jsonify({'data': a + b})


api.add_resource(status, '/')
api.add_resource(Sum, '/add/<int:a>,<int:b>')
api.add_resource(Register_User, '/register/user/')
api.add_resource(Get_All_Users, '/all_users')
api.add_resource(Register_Pro, '/register/professional')
api.add_resource(Get_All_Pro, '/all_professionals')

if __name__ == '__main__':
    app.run()
