import datetime
import telebot

print("Введите токен бота")
TOKEN = input()

used_by = []

bot = telebot.TeleBot()

now = datetime.datetime.now()
then = datetime.datetime(2020, 12, 31, 23, 59, 59)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот что бы узнать про меня больше пиши /help')
    print(message.chat.first_name, message.chat.last_name, message.chat.username)
    used_by.append(str(message.chat.first_name) + " " + str(message.chat.last_name) + " " + str(message.chat.username))
    while(True):
        now = datetime.datetime.now()
        if now >= then:
            bot.send_message(message.chat.id, "С новым годом!")
            break

@bot.message_handler(commands=['help'])
def helping(message):
    bot.send_message(message.chat.id, 'Я бот и знаю команды:\n /start \n /help \n /weather и местность в которой нужно посмотреть погоду \n /Humana \n /Serial')

@bot.message_handler(commands=['weather'])
def weather(message):
    if message.text == '/weather Киев':
        bot.send_message(message.chat.id, 'https://www.gismeteo.ua/weather-kyiv-4944/')
    else:
        if message.text == '/weather Дымер':
            bot.send_message(message.chat.id, 'https://www.gismeteo.ua/weather-dymer-13512/')
        else:
            if message.text == '/weather Вышгород':
                bot.send_message(message.chat.id, 'https://www.gismeteo.ua/weather-vyshhorod-12073/')

@bot.message_handler(commands=['Humana'])
def sales(message):
    bot.send_message(message.chat.id, 'http://humana.com.ua/')

@bot.message_handler(commands=['Serial'])
def sales(message):
    bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=da_Fgu2qzXY&t=2683s')

@bot.message_handler(commands=['Who_us_you_MF'])
def Who_us_you(message):
    bot.send_message(message.chat.id, used_by)

if __name__ == '__main__':
    bot.polling(none_stop=True)