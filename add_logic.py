from flask_restful import Resource
from flask import request, jsonify

def check_posted_data(posted_data, function_name):
    if function_name == "add" or function_name == "subtract" or function_name == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # Missing parameter
        else:
            return 200

class Add(Resource):
    def post(self):
        # If I am here, then the resouce Add was requested using the method POST

        # Step 1: Get posted data:
        posted_data = request.get_json()

        print(posted_data)

        # Steb 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "add")
        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x+y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)
