import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "سلام به کافینت آریا خوش اومدی 🌹\n\n"
        "به دستیار هوشمند آریا خوش آمدید.\n"
        "برای مشاهده خدمات از منوی زیر استفاده کنید."
    )

bot.infinity_polling()
