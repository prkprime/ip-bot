#!/usr/bin/python3

import requests
import telebot
import os
import json

# Get config data from json / env
if os.path.exists(r'data.json'):
    with open(r'data.json', 'r') as f:
        data = json.load(f)
else:
    try:
        data = {
            'bot-token': environ['BOT_TOKEN'],
            'notify-id': environ['NOTIFY_ID'],
        }
    except KeyError:
        print("You don't have configuration JSON or environment variables set, go away")
        exit(1)

bot = telebot.AsyncTeleBot(data['bot-token'])

@bot.message_handler(commands=['public_ip'])
def get_public_ip(message):
    bot.reply_to(message, requests.get('https://api.ipify.org').text)

# Start ze bot
print('start')
bot.send_message(data['notify-id'], 'Bot Started')
bot.polling()
