from flask import Flask, jsonify, request
from flask_restful import Resource
from __init__ import api, app


class Register_User(Resource):
    def post(self):
        content = request.get_json()

        return content
        print(content, "---------------------------------------")


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

if __name__ == '__main__':
    app.run()
