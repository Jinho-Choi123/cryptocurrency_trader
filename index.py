from flask import Flask 
from flask_restx import Api, Resource
from trader import Trader

app = Flask(__name__)
api = Api(app)

api.add_namespace(Trader)

if __name__ == '__main__':
    app.run()