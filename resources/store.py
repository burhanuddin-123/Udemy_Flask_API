from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message':f'Store with name {name} not exists'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':"Store with name '{}' already exists.".format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occured'}, 500
        
        return {'Store created': store.json()}, 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"Store deleted":store.json()}, 200
        
        return {'message':'store not exists'}, 404
            

    ### 
    # we will not create put method as we don't want to allow to change the store info.

class StoreList(Resource):
    def get(self):
        return {"Store":[store.json() for store in StoreModel.query.all()]}, 200