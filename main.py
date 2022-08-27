from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)
CORS(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# Flah
# Flah
# aniket
api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
