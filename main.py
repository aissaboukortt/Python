import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7918593944:AAGlthevgUy6FDLbnvwRe_6LVSWKXxj3BYU'
WEB_APP_URL = 'http://t.me/selfietrex_bot/Reels'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🌐 افتح الموقع", url=WEB_APP_URL))
    bot.send_message(message.chat.id, "اضغط الزر لفتح الموقع 👇", reply_markup=markup)

bot.polling()