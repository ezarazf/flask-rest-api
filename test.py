from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def entry_point():
    return jsonify(message="Hello Wordl")

@app.route('/salam',methods = ['GET'])
def salam_sehat():
    return jsonify(message="Assalamualaikum")

if __name__ == '__main__':
    app.run(debug=True)