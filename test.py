from flask import Flask,jsonify, request
from flask import request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def entry_point():
    return jsonify(message="Hello Wordl")

@app.route('/salam',methods = ['GET'])
def salam_sehat():
    return jsonify(message="Assalamualaikum")

@app.route('/test',methods = ['POST','GET'])
def test():
    if request.method == 'POST':
        body = request.get_json()
        params = request.args.get('timestamp')
        print(params)
        # print("Body nya adalah", body)
        # print(body['data'])
        # return jsonify(message="Assalamualaikum POST",data=body['data'])
        return {
            "message":"Hello, i have processed your request",
            "data":body['data'],
            "params":params
        }
    elif request.method == 'GET':
        return jsonify(message="Waalaikumsalam GET")

if __name__ == '__main__':
    app.run(debug=True)