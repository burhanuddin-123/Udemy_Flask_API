from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel
        

class Items(Resource):
    def get(self):
        return {'Items': [item.json() for item in ItemModel.query.all()]}, 200
        


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank"
        )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help="Every item need a store id"
    )
        
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'item': item.json()}, 200
        return {'message': 'Item not found'}, 404
    
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message":f"An item with name {name} already exists"}, 400
        
        data = Item.parser.parse_args()

        # item = {'name':name, 'price':data['price']}
        item = ItemModel(name, data['price'],data['store_id'])

        try:
            # ItemModel.insert_data(item)
            item.save_to_db()
        except:
            return {"message":"An error occured"}, 500  # Internal Server Error

        return {'Item Created': item.json()}, 201


    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"Item deleted": item.json()}, 200
        
        return {"message":f"Item with name {name} don't exists"}, 404

    def put(self,name):
        item = ItemModel.find_by_name(name)
        data = Item.parser.parse_args()
        

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'],data['store_id'])

        item.save_to_db()
        return item.json()