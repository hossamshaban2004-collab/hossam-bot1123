import telebot
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

TOKEN = '8773169758:AAH84Zr5W8Hyf931ovuoC6xAHXOCBj6V6VM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبا! قل "مطور طلعت مصطفى" أو "سوق" أو "جديد"')

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    text = message.text.lower()
    
    if 'سوق' in text:
        bot.reply_to(message, '''📊 السوق العقاري 2026:
- 2026 عام الشراء بعد خفض الفائدة [web:1]
- العاصمة الإدارية + العلمين الأكثر طلباً [web:2]
- الناس تشتري وحدات صغيرة كملاذ آمن [web:3]''')
    
    elif 'جديد' in text:
        bot.reply_to(message, '📰 أخبار جديدة:\n- مبيعات طلعت مصطفى 211 مليار [web:4]\n- بالم هيلز 143 مليار [web:4]')
    
    elif 'مطور' in text:
        dev = text.split()[-1]
        news = f"أخبار {dev}:\n- مشاريع جديدة في العاصمة [web:9]\n- عروض تقسيط جديدة"
        bot.reply_to(message, news)
    else:
        bot.reply_to(message, 'جرب: "سوق" أو "مطور طلعت مصطفى"')

print("البوت شغال!")
bot.infinity_polling()
