import urllib
import requests
import telebot
import urllib
import requests

TOKEN = '1029910258:AAEZMySWWxqScBiYXr4UkyqRwiIYppgMkA4'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты можешь использовать /help для просмотра функций')

@bot.message_handler(commands=['help'])
def test(message):
	bot.send_message(message.chat.id, 'sosi pisos')

@bot.message_handler(commands=['test'])
def test(message):
	dls = 'https://drive.google.com/file/d/1X4X1a1jUDekW2UDyoZaVTR8WyuAWkrUh'
	urllib.request.urlretrieve(dls, "test.xls")
	bot.send_message(message.chat.id, 'GAGAGAGA')


bot.polling()