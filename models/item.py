from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # add new column for self.items in StoreModel
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    ## thus store id is the column that contains the id of stores and thus it is foreign key for items tables.
    # in parenthesis we have mention which column will used as a foreign key here, thus we have mention that id column of stores table.

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name':self.name, 'price':self.price, 'store_id':self.store_id}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM __tablename__ WHERE name=name
    
    def save_to_db(self):
        db.session.add(self) # thus it is saving the current object to database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

