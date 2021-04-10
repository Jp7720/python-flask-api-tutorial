from flask import Flask
app = Flask(__name__)
from flask import jsonify           #importe jsonify
from flask import request
import json



@app.route('/todos', methods=['GET'])
def hello_world():
    return  jsonify(todos)         #cambie hello por jsonify

todos = [
    { "label": "Study", "done": False },    #cree variable fuera del scope de la función.
    { "label": "sleep", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    return json_text 
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if request.method == 'DELETE':
        todos.pop(position-1)
        print(f"This is the position to delete: {position}")
        return jsonify(todos)






# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)