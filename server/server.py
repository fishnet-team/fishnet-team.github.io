from flask import Flask, escape, request
import bot
import requests
app = Flask(__name__)
BOT_ROOT = "/bot"
SERVER_URL = "http://178.128.196.165"
CLIENT_ID = "261ee9feef5e0a62fe03ff7a2ee7382f"
CLIENT_SECRET = "89169aa794afcc0463262a20631ed101"
ACCESS_TOKEN = "dal%3AWuHHLVdeTcGdmweUj6NsVA"
autofaq = None

agent_ids = set()
active_agent_ids = set()

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

@app.route(f'{BOT_ROOT}/incoming_chat_thread', methods=["POST"])
def bot_incoming_chat_thread():
    print(request.json())
    return {"result": "ok"}

@app.route(f'{BOT_ROOT}/thread_closed', methods=["POST"])
def bot_thread_closed():
    print(request.json())
    return {"result": "ok"}

@app.route(f'{BOT_ROOT}/incoming_event', methods=["POST"])
def bot_incoming_event():
    print(1, request.form)
    print(2, request.args)
    print(3, request.values)
    print(4, request.json)
    assert(request.json['secret_key'] == autofaq.SECRET_TOKEN)
    autofaq.process(request.json['payload']['event'], request.json['payload']['chat_id'])
    return {"result": "ok"}

'''
@app.route('/oauth2')
def auth():
    print(request.args)
    code = request.args['code']
    print("Code is {code}")
    print("Exchanging token")
    data = {'grant_type': 'authorization_code',
            'code': code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': f'{SERVER_URL}/oauth2'}
    resp = requests.post('https://accounts.livechatinc.com/token', data=data)
    print(resp.json())
    access_token = resp.json()['access_token']
    print('ACCESS_TOKEN is', access_token)
    global ACCESS_TOKEN, autofaq
    ACCESS_TOKEN = access_token
    autofaq = bot.Bot('Cerebra AutoFAQ', SERVER_URL + BOT_ROOT, ACCESS_TOKEN)
'''

@app.route('/livechat', methods=['POST', 'GET'])
def livechat():
    print(1, request.form)
    print(2, request.args)
    print(3, request.values)
    print(4, request.json)
    return {"result": "ok"}

def redirect_user():
    url = f"https://accounts.livechatinc.com/?response_type=code&client id={CLIENT_ID}" \
           "&redirect uri=http%3A%2F%2F178.128.196.165%2Foauth2"
    print(f"Go To: {url}")

if __name__ == '__main__':
    if ACCESS_TOKEN is None:
        redirect_user()
    else:
        autofaq = bot.Bot('Cerebra AutoFAQ', SERVER_URL + BOT_ROOT, ACCESS_TOKEN)
        autofaq.get_all_agents()
        #exit(0)
    app.run(debug=True, port=80, host="0.0.0.0") #run app in debug mode on port 5000
