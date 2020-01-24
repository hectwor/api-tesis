from flask import Flask
from flask_graphql import GraphQLView
from Schema  import Schema

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=Schema, graphiql=True))

if __name__ == '__main__':
    app.run()