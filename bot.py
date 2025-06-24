import telebot

TOKEN = "7764666872:AAH0gI-WQGXiL2uI84K0SkmP0F3QHyPDfqI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Я твій перший бот.")
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Команди:\n/start — почати\n/help — допомога\n/echo — повторити")

bot.polling()

