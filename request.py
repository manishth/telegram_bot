import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]


greet_bot = BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = new.hour

    while True:
        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning {}'.format(last_chat_name))
            today += 1
        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1
        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening {}'.format(last_chat_name))
            today += 1
        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()


# url = "https://api.telegram.org/bot318923032:AAE4-qHn-k2umzPBLzriUlZsRZjNYXlN7Cc/"
#
# def main():
#     update_id = last_update(get_updates_json(url))['update_id']
#     while True:
#         if update_id == last_update(get_updates_json(url))['update_id']:
#             send_message(get_chat_id(last_update(get_updates_json(url))), 'test')
#             update_id += 1
#     sleep(1)

# def get_updates_json(request):
#     params = {'timeout': 100, 'offset': None}
#     response = requests.get(request + 'getUpdates', data=params)
#     return response.json()
#
# def last_update(data):
#     results = data['result']
#     total_updates = len(results)
#     return results[total_updates]
#
# def get_chat_id(update):
#     chat_id = update['message']['chat']['id']
#     return chat_id
#
# def send_message(chat, text):
#     params = {'chat_id': chat, 'text': text}
#     response = requests.post(url + 'sendMessage', data = params)
#     return response
#
# chat_id = get_chat_id(last_update(get_updates_json(url)))
#
# send_message(chat_id, "Your message goes here")
#
# if __name__ == '__main__':
#     main()
