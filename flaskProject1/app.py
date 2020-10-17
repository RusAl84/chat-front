from flask import Flask, jsonify, request,abort

app = Flask(__name__)

mas=[]

@app.route('/')
def hello_world():
    return 'Hello World!'

# https://habr.com/ru/post/246699/

@app.route('/api/data/<string:id>', methods=['GET'])
def add_data(id):
    # print(id)
    if (int)(id) < 4:
        abort(404)
    mas.append(id)
    return mas

@app.route('/api/data', methods=['POST'])
def get_data():
    # print(mas)
    return jsonify(mas)


if __name__ == '__main__':
    app.run()
