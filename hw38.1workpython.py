import telebot
import hw382python, hw38workpython

bot = telebot.TeleBot('6148037034:AAGylTPYhWbrZce8J4aCULQF2x7Qns1zv5k')
bot.send_message(825113753, 'готов к работе')

@bot.message_handler(content_types=['text'])
def message(info):
    print(info.chat.id)
    if 'привет' in info.text:
        bot.send_message(info.chat.id,'privet')
    elif 'пока' in info.text:
        bot.send_message(info.chat.id,'poka')
    elif 'погода' in info.text:
        pog=hw38workpython.getpogoda()
        bot.send_message(info.chat.id,pog)
    elif 'анекдот' in info.text:
        anek = hw382python.anekdot()
        bot.send_message(info.chat.id,anek)
    else:
        bot.send_message(info.chat.id,'ya bot')
    pass

bot.polling(none_stop=True)