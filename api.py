from flask import Flask
from flask_graphql import GraphQLView
from Schema import Schema
from Database.base import connect

def create_app(path='/graphql', **kwargs):
    backend = None
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(path, view_func=GraphQLView.as_view('graphql', schema=Schema, backend=backend, **kwargs))
    return app

if __name__ == '__main__':
    app = create_app(graphiql=True)
    app.run()
