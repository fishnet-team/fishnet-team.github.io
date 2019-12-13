from flask import Flask, escape, request
import bot
app = Flask(__name__)
BOT_ROOT = "/bot"
SERVER_URL = "http://178.128.196.165"

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

@app.route(f'{BOT_ROOT}/incoming_chat_thread')
def bot_incoming_chat_thread():
    print(request.json)
    return {"result": "ok"}

@app.route(f'{BOT_ROOT}/thread_closed')
def bot_thread_closed():
    print(request.json)
    return {"result": "ok"}

@app.route(f'{BOT_ROOT}/incoming_event')
def bot_incoming_event():
    print(request.json)
    assert(request.json['secret_key'] == bot.SECRET_TOKEN)
    chat_id = request.json['payload']['chat_id']
    text = request.json['payload']['event']['text'] # Other types are not supported
    bot.answer(text=text, chat_id=chat_id)
    return {"result": "ok"}

@app.route('/livechat', methods=['POST', 'GET'])
def livechat():
    print(1, request.form)
    print(2, request.args)
    print(3, request.values)
    print(4, request.json)
    return {"result": "ok"}

if __name__ == '__main__':
    autofaq = bot.Bot('Cerebra AutoFAQ', SERVER_URL + BOT_ROOT)
    app.run(debug=True, port=80, host="0.0.0.0") #run app in debug mode on port 5000
