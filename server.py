from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return  'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json  # Get the JSON data from the request body
    if 'x' in data and 'y' in data:
        x = data['x']
        y = data['y']
        result = x + y
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.json
    if "x" in data and "y" in data:
        x=data["x"]
        y=data['y']
        result =x-y
    return jsonify({'result':result})


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
