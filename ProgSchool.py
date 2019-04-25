from delorean import Delorean

import telebot
bot = telebot.TeleBot("815074412:AAE0KN93VAOtYp6lFcBZh5YqkFeAIPMVLmo")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	d = Delorean()
	d = d.shift("UTC")
	d = d.next_hour(3)
	if message.text == "Время":
		bot.send_message (message.chat.id, "Время: "+str(d.format_datetime(locale='en_US')))
#print (str(d))
bot.polling( none_stop = True )