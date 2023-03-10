from flask import Flask
from flask_restful import Api, Resource
from add_logic import Add

app = Flask(__name__)
api = Api(app)

api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return 'Hello World'
 
if __name__ == '__main__':
    app.run()