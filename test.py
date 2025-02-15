from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def entry_point():
    return jsonify(message="Hello Wordl")

@app.route('/salam',methods = ['GET'])
def salam_sehat():
    return jsonify(message="Assalamualaikum")

@app.route('/test',methods = ['GET','POST'])
def test():
    if request.method == 'GET':
        return jsonify(message="Assalamualaikum GET")
    elif request.method == 'POST':
        return jsonify(message="Waalaikumsalam POST")

if __name__ == '__main__':
    app.run(debug=True)