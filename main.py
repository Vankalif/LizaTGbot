import telebot

liza_bot = telebot.TeleBot('1381040431:AAEcUZ84K6KfwrVh4tc1vQeWrpiv4ar3VN0')


@liza_bot.message_handler(commands=['start'])
def start_message(message):
    liza_bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


liza_bot.polling()
