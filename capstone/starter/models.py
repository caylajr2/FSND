from sqlalchemy import Column, String, Integer, Float
from flask_sqlalchemy import SQLAlchemy

database_name = "earring_shoppe"
database_user = "student"
database_password = "student"
database_host = 'localhost:5432'
database_path = f'postgresql://{database_user}:{database_password}@{database_host}/{database_name}'

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

'''Item'''
class Item(db.Model):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

    def __init__(self, name, description, image, cost):
        self.name = name
        self.description = description
        self.image = image
        self.cost = cost

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'cost': self.cost
        }

'''Customer'''

class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    cart_id = Column(Integer, nullable=False)

    def __init__(self, name, image, cart_id):
        self.name = name
        self.image = image
        self.cart_id = cart_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image
        }

'''Cart'''
class Cart(db.Model):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    item_ids = Column((db.ARRAY(db.Integer)))

    def __init__(self, customer_id, item_ids):
        self.customer_id = customer_id
        self.item_ids = item_ids

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'item_ids': self.item_ids
        }