import requests

def send_telegram_message(message):
    token='5876439174:AAH4_fTlK0GMeIhV-0IvEyUiwrxHHzjkPz8'
    chat_id = '448891019'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, json=payload)
    response.raise_for_status()
