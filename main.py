from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def __get__(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, 'https://seek-community.netlify.app/')

if __name__ == '__main__':
    app.run(debug=True)
