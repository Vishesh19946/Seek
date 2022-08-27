from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)
CORS(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

<<<<<<< HEAD
# aniket
api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorld, '/test')
=======

api.add_resource(HelloWorld, '/')
>>>>>>> acbe9015adf108392432f78a61eed6cace56cd5f

if __name__ == '__main__':
    app.run(debug=True)
