import telebot
import wikipedia

wikipedia.set_lang("ru")
bot = telebot.TeleBot("5919240047:AAG3I-yxpMogdFKtKWmUJzQVLkctzwz18lE")

@bot.message_handler(commands = ["start"])
def searc_wikipedia(message):
    searc_wik = message.text
    searc_img = message.text

    try:
        search = wikipedia.summary(searc_wik, sentences = 3)
        bot.send_message(message.chat.id, search)
        ss = wikipedia.page(searc_img).images[1]
        bot.send_message(message.chat.id, ss)
    except:
        bot.send_message(message,chat.id, "К сожалению, ничего пока не нашли")

bot.polling(none_stop = True)








