from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "Sample Todo 1", "done": False },
    { "label": "Sample Todo 2", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
     json_text = jsonify(todos)
     return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json 
    todos.append(request_body)  
    return jsonify(todos)  

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)