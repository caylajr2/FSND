import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Item, db


# pagination modified from trivia_api
ITEMS_PER_PAGE = 20

def paginate_items(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

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
    Get Items
    """
    @app.route('/items')
    def get_items():
        try:
            selection = Item.query.all()
            return "hello worlde"
            formatted_items = paginate_items(selection)
            return jsonify({
                'items': formatted_items
            }), 200
        except BaseException:
            abort(404, description="get_items")


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




# def create_app(test_config=None):
#   # create and configure the app
#   app = Flask(__name__)
#   CORS(app)

#   return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
