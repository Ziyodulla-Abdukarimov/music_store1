import requests


def send_message(bot_token, chat_id, message):
    url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message
    result = requests.get(url_req)
    return result.status_code
