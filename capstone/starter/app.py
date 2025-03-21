import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Item, Customer, db
from auth import AuthError, requires_auth


# pagination modified from trivia_api
ITEMS_PER_PAGE = 20

def paginate_items(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    items = [item.format() for item in selection]
    current_items = items[start:end]

    return current_items

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    with app.app_context():
        db.create_all()

    # From trivia_api code
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response










    """
    Get Home Page
    """
    @app.route('/')
    def get_home():
        try:
            return "hello worlde"
        except Exception as e:
            abort(404, description=str(e))










    """
    Get Items
    """
    @app.route('/items')
    def get_items():
        try:
            selection = Item.query.all()
            formatted_items = paginate_items(request, selection)
            return jsonify({
                'items': formatted_items
            }), 200
        except Exception as e:
            abort(404, description="get /items: " + str(e))

    """
    Get Item by id
    """
    @app.route('/items/<int:item_id>')
    def get_specific_item(item_id):
        try:
            item = Item.query.filter(Item.id == item_id).one_or_none()
            return jsonify({
                'item': item.format()
            }), 200
        except Exception as e:
            abort(404, description="get /item/<int:item_id>: " + str(e))


    """
    Get Customers
    """
    @app.route('/customers')
    @requires_auth('get:customers')
    def get_customers(payload):
        try:
            customers = Customer.query.all()
            return jsonify({
                'customers': [customer.format() for customer in customers]
            }), 200
        except Exception as e:
            abort(404, description="get /customers: " + str(e))

    """
    Get Customer by id
    """
    @app.route('/customer')
    @requires_auth('get:customer')
    def get_specific_customer(payload):
        try:
            sub = payload['sub']
            customer = Customer.query.filter(Customer.sub == sub).one_or_none()
            return jsonify({
                'customer': customer.format()
            }), 200
        except Exception as e:
            abort(404, description="get /customers: " + str(e))
    

    """
    Get Only Customer's Cart
    """
    @app.route('/customer/cart')
    @requires_auth('get:customer')
    def get_specific_cart(payload):
        try:
            sub = payload['sub']
            customer = Customer.query.filter(Customer.sub == sub).one_or_none()
            return jsonify({
                'customer': customer.id,
                'cart': customer.cart
            }), 200
        except Exception as e:
            abort(404, description="get /customers/cart: " + str(e))










    """
    Add New Item from request json
    """
    @app.route('/items', methods=['POST'])
    @requires_auth('post:item')
    def add_item(payload):
        try:
            item = Item(**request.get_json())
            item.insert()
            return jsonify({
                'item': item.format()
            }), 200
        except Exception as e:
            abort(422, description="add /items: " + str(e))


    """
    Add New Customer from request json
    """
    @app.route('/customer', methods=['POST'])
    @requires_auth('post:customer')
    def add_customer(payload):
        try:
            sub = payload['sub']
            data = request.get_json()
            data['sub'] = sub
            if Customer.query.filter(Customer.sub == sub).all():
                abort(403, description="add /customer: Customer Already Exists")
            
            customer = Customer(**data)
            customer.insert()

            return jsonify({
                'customer': customer.format()
            }), 200
        except Exception as e:
            if e.code == 403:
                raise
            abort(404, description="add /customer: " + str(e))










    """
    Add item to cart
    """
    @app.route('/items/<int:item_id>/add_to_cart', methods=['POST'])
    @requires_auth('reserve:item')
    def add_item_to_cart(payload, item_id):
        try:
            sub = payload['sub']
            customer = Customer.query.filter(Customer.sub == sub).one_or_none()
            item = Item.query.filter(Item.id == item_id).one_or_none()
            if not customer.cart:
                customer.cart = []
            customer.cart = customer.cart + [item.id]
            customer.update()
            return jsonify({
                'cart': customer.cart
            }), 200
        except Exception as e:
            abort(422, description="add /items/<int:item_id>/add_to_cart: " + str(e))


    """
    Remove item from cart
    """
    @app.route('/items/<int:item_id>/remove_from_cart', methods=['POST'])
    @requires_auth('reserve:item')
    def remove_item_from_cart(payload, item_id):
        try:
            sub = payload['sub']
            customer = Customer.query.filter(Customer.sub == sub).one_or_none()
            item = Item.query.filter(Item.id == item_id).one_or_none()
            cart = customer.cart

            if not cart:
                abort(400, description='remove /items/<intLitem_id>/remove_from_cart: cart is empty')

            if item.id not in cart:
                abort(400, description='remove /items/<intLitem_id>/remove_from_cart: item not in cart')
            
            cart.remove(item.id)
            print(cart)
            customer.cart = cart
            print(customer.cart)
            customer.update()
            print(customer.cart)
            return jsonify({
                'cart': customer.cart
            }), 200
        except Exception as e:
            if e.code == 400:
                raise
            abort(422, description="add /items/<int:item_id>/add_to_cart: " + str(e))

    
    """
    Place order
    """
    @app.route('/customer/place_order', methods=['POST'])
    @requires_auth('reserve:item')
    def place_order(payload):
        try:
            sub = payload['sub']
            customer = Customer.query.filter(Customer.sub == sub).one_or_none()
            customer.cart = []
            customer.update()
            return jsonify({
                'customer': customer.format()
            })
        except Exception as e:
            abort(404, description="post /customer/place_order: " + str(e))

    
    
    
    
    
    
    
    
    
    """
    Update specific item
    """
    @app.route('/items/<int:item_id>', methods=['PATCH'])
    @requires_auth('edit:item')
    def update_item(payload, item_id):
        try:
            item = Item.query.filter(Item.id == item_id).one_or_none()
            data = request.get_json()

            if 'cost' in data:
                item.cost = data['cost']
            if 'description' in data:
                item.description = data['description']
            if 'image' in data:
                item.image = data['image']
            if 'name' in data:
                item.name = data['name']
            
            item.update()

            return jsonify({
                'item': item.format()
            }), 200
        except Exception as e:
            abort(404, description="update /items/<int:item_id>: ") + str(e)


    """
    Update specific customer
    """
    @app.route('/customer', methods=['PATCH'])
    @requires_auth('edit:customer')
    def update_customer(payload):
        try:
            sub = payload['sub']
            customer = Customer.query.filter(Customer.sub == sub).one_or_none()

            data = request.get_json()

            if 'image' in data:
                customer.image = data['image']
            if 'cart' in data:
                customer.cart = data['cart']
            if 'name' in data:
                customer.name = data['name']

            customer.update()

            return jsonify({
                'customer': customer.format()
            }), 200
        except Exception as e:
            abort(404, description="update /customer: ") + str(e)









    """
    Delete item
    """
    @app.route('/items/<int:item_id>', methods=['DELETE'])
    @requires_auth('delete:item')
    def delete_item(payload, item_id):
        try:
            item = Item.query.filter(Item.id == item_id).one_or_none()
            print(item.format())
            item.delete()
            return jsonify({
                "message": "deleted item with id " + str(item_id)
            }), 200
        except Exception as e:
            abort(404, description="delete /items/<int:item_id>: " + str(e))
    

    """
    Delete Customer
    """
    @app.route('/customer', methods=['DELETE'])
    @requires_auth('delete:customer')
    def delete_customer(payload):
        try:
            sub = payload['sub']
            customer = Customer.query.filter(Customer.sub == sub).one_or_none()
            id = customer.id
            customer.delete()
            return jsonify({
                "message": "deleted customer with id " + str(id)
            }), 200
        except Exception as e:
            abort(404, description="delete /customer: " + str(e))










    """
    Error handlers
    """
    # Modified from trivia_api code
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found: " + error.description
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable: " + error.description
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request: " + error.description
        }), 400

    @app.errorhandler(500)
    def server_error():
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500
    
    # AuthError handler from Identity and Access Management
    @app.errorhandler(AuthError)
    def authentication_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error["description"]
        }), error.status_code



    return app










app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
