import requests as rq
import json

class Bot:
    TOKEN = "261ee9feef5e0a62fe03ff7a2ee7382f"
    SECRET_TOKEN = "89169aa794afcc0463262a20631ed101"
    URL = "http://..."

    headers = {'content-type': 'application/json',
               'Authorization': f'Bearer {TOKEN}',
               'X-Region': 'fra header',
               }

    def action(self, action, data):
        url = f'https://api.livechatinc.com/v3.1/configuration/action/{action}'
        return rq.post(url, json=data, headers=self.headers)

    def __init__(self, name, url=None, token=None):
        if url is not None:
            self.URL = url
        if token is not None:
            self.TOKEN = token

        self.name = name
        data = {'name': name,
                'status': 'accepting chats',
                'default_group_priority': 'first',
                'webhooks': [
                    {'action': 'incoming_chat_thread', 'secret_key': self.SECRET_TOKEN, 'url': f'{self.URL}/incoming_chat_thread'},
                    {'action': 'thread_closed', 'secret_key': self.SECRET_TOKEN, 'url': f'{self.URL}/thread_closed'},
                    {'action': 'incoming_event', 'secret_key': self.SECRET_TOKEN, 'url': f'{self.URL}/incoming_event'}
                ]}
        # ['chat_user_added', 'chat_user_removed', 'event_updated']
        resp = self.action('create_bot_agent', data)
        print(resp.json())
        self.id = resp.json()['bot_agent_id']

    def __del__(self):
        self.action('remove_bot_agent', self.id)

    def redirect(self):
        pass

    def send_message(chat_id, text):
        url = "https://api.livechatinc.com/v3.1/agent/action/send_event"
        return rq.post(url, headers=headers, json={'chat_id': chat_id, 'event': {
           "type": "message",
           "text": text,
           "recipients": "all"
        }})

    def answer(self, message, chat_id):
        self.send_message(chat_id, "Your message is " + message)

    def __str__(self):
        return "Bot{id=" + str(self.id) + "name=" + str(self.name) + "}"
    __repr__ = __str__
