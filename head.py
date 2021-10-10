import config
import weather_data
import telebot

USERS = {}

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def first_start(message):
    """Обработчик команды /start"""
    text = """
    Telegram WeatherHelper Bot v0.1
    """
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['set'])
def first_start(message):
    """Обработчик команды /set"""
    text = """
    Send your location.
    """
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['location'])
def first_start(message):
    """Обработчик location"""
    weather_now = weather_data.weather_helper(message.location)
    bot.send_message(message.chat.id, weather_now)

@bot.message_handler(content_types=['text'])
def first_start(message):
    """Обработчик text"""
    answer = 'Ты почесать языком хочешь или погоду узнать? Шли локацию!'
    bot.send_message(message.chat.id, answer)

if __name__ == '__main__':
    bot.infinity_polling()