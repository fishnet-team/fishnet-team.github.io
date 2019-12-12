from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/jivosite', methods=['POST'])
def log_all_webhooks():
    print(1, request.form)
    print(2, request.args)
    print(3, request.values)
    print(4, request.json)
    return {"result": "ok"}

@app.route('/livechat', methods=['POST', 'GET'])
def log_all_webhooks():
    print(1, request.form)
    print(2, request.args)
    print(3, request.values)
    print(4, request.json)
    return {"result": "ok"}

if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0") #run app in debug mode on port 5000
