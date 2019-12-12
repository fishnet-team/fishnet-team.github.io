from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/jivosite', methods=['POST'])
def log_all_webhooks():
    print(request.form)
    return {"result": "ok"}

if __name__ == '__main__':
    app.run(debug=True, port=80) #run app in debug mode on port 5000
