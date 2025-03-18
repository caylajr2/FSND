import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Item, Customer, Cart, db


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
    def get_customers():
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
    @app.route('/customers/<int:customer_id>')
    def get_specific_customer(customer_id):
        try:
            customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
            return jsonify({
                'customer': customer.format()
            }), 200
        except Exception as e:
            abort(404, description="get /customers: " + str(e))


    """
    Get Carts
    """
    @app.route('/carts')
    def get_carts():
        try:
            data = db.session.query(Cart, Customer).join(Customer, Cart.id == Customer.cart_id).all()
            data = [(cart.format(), customer.format()) for cart, customer in data]
            return jsonify({
                'carts': data
            }), 200
        except Exception as e:
            abort(404, description="get /carts: " + str(e))
    
    """
    Get Cart by id
    """
    @app.route('/carts/<int:cart_id>')
    def get_specific_cart(cart_id):
        try:
            cart, customer = db.session.query(Cart, Customer).join(Customer, Cart.id == Customer.cart_id).filter(Cart.id == cart_id).one_or_none()
            return jsonify({
                'customer': customer.format(),
                'cart': cart.format()
            }), 200
        except Exception as e:
            abort(404, description="get /carts/<int:cart_id>: " + str(e))










    """
    Add New Item from request json
    """
    @app.route('/items', methods=['POST'])
    def add_item():
        try:
            item = Item(**request.get_json())
            item.insert()
            return jsonify({
                'item': item.format()
            }), 200
        except Exception as e:
            abort(422, description="add /items: " + str(e))


    """
    Add New Customer (and Cart) from request json
    Creates a new Customer and a new Cart associated with that customer
    """
    @app.route('/customers', methods=['POST'])
    def add_customer():
        try:
            customer = Customer(**request.get_json())
            customer.insert()

            cart = Cart(customer.id, [])
            cart.insert()

            customer.cart_id = cart.id
            customer.update()

            return jsonify({
                'customer': customer.format(),
                'cart': cart.format()
            }), 200
        except Exception as e:
            abort(404, description="add /customers: " + str(e))










    """
    Add item to cart
    """
    @app.route('/items/<int:item_id>/add_to_cart', methods=['POST'])
    def add_item_to_cart(item_id):
        try:
            item = Item.query.filter(Item.id == item_id).one_or_none()
            print("\nTODO\n")
            print(item.format())
            print()
            return jsonify({
                'item': item.format()
            }), 200
        except Exception as e:
            abort(422, description="add /items/<int:item_id>/add_to_cart: " + str(e))

    
    """
    Place order
    """
    @app.route('/carts/<int:cart_id>', methods=['POST'])
    def place_order(cart_id):
        try:
            cart = Cart.query.filter(Cart.id == cart_id).one_or_none()
            print("\nTODO\n")
            print(cart.format())
            print()
            cart.item_ids = []
            return jsonify({
                'cart': cart.format()
            })
        except Exception as e:
            abort(404, description="post /carts/<int:cart_id>: " + str(e))

    
    
    
    
    
    
    
    
    
    """
    Update specific item
    """
    @app.route('/items/<int:item_id>', methods=['PATCH'])
    def update_item(item_id):
        try:
            item = Item.query.filter(Item.id == item_id).one_or_none()
            print("\nTODO\n")
            print(item.format())
            print()
            return jsonify({
                'item': item.format()
            }), 200
        except Exception as e:
            abort(404, description="update /items/<int:item_id>: ") + str(e)


    """
    Update specific customer
    """
    @app.route('/customers/<int:customer_id>', methods=['PATCH'])
    def update_customer(customer_id):
        try:
            customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
            print("\nTODO\n")
            print(customer.format())
            print()
            return jsonify({
                'customer': customer.format()
            }), 200
        except Exception as e:
            abort(404, description="update /customers/<int:customer_id>: ") + str(e)


    """
    Update specific cart
    """
    @app.route('/carts/<int:cart_id>', methods=['PATCH'])
    def update_cart(cart_id):
        try:
            cart = Cart.query.filter(Cart.id == cart_id).one_or_none()
            print("\nTODO\n")
            print(cart.format())
            print()
            return jsonify({
                'cart': cart.format()
            }), 200
        except Exception as e:
            abort(404, description="update /carts/<int:cart_id>: ") + str(e)









    """
    Delete item
    """
    @app.route('/items/<int:item_id>', methods=['DELETE'])
    def delete_item(item_id):
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
    @app.route('/customers/<int:customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        try:
            customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
            cart = Cart.query.filter(Cart.id == customer.cart_id).one_or_none()
            customer.delete()
            cart.delete()
            return jsonify({
                "message": "deleted customer with id " + str(customer_id)
            }), 200
        except Exception as e:
            abort(404, description="delete /customers/<int:customer_id>: " + str(e))










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

    return app










app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
