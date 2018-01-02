# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import reqparse, Api, Resource
from pymongo import MongoClient

db_name = 'your-db'
col_name = 'your-col'
client = MongoClient('localhost', 27017)
col = client[db_name][col_name]
col.remove({})
col.insert({'_id': 1, "name": "debugo", "values": [70, 65]})
col.insert({'_id': 2, "name": "leo", "values": [65]})
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('values', type=int, help='rate is a number', action='append')


class UserInfo(Resource):
    # def get(self):
    #     return [str(i) for i in col.find({})] 

    def post(self):
        args = parser.parse_args()
        user_id = col.count() + 1
        col.insert({'_id': user_id, "name": args["name"], "values": args["values"]})
        return [str(i) for i in col.find({'_id': user_id})], 201


api.add_resource(UserInfo, '/')

if __name__ == '__main__':
    app.run(debug=True)
