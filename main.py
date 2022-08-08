import telebot
from telebot import types
bot = telebot.TeleBot("ВАШ ТОКЕН БОТА")
@bot.message_handler(commands=['start'])
def start(message):
    knopki= types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1= types.KeyboardButton("👋 Введи свой секретный код)")
    btn2= types.KeyboardButton("❓")
    btn3= types.KeyboardButton("Что-то еще")
    knopki.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Это сейф, {0.first_name} тут нужен секретный ключ)".format(message.from_user), reply_markup = knopki)



@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Введи свой секретный код)"):
        bot.send_message(message.chat.id, text="Введи секретный код")
    elif (message.text=="3131"):
        photo=open('C:\\Users\\Александр\\Desktop\\Новая папка\\photo.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    elif (message.text == "❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Знаешь что это?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Знаешь что это?"):
        bot.send_message(message.chat.id, "Это сейф, который отправляет разные материалы по кодам")

    elif (message.text == "Вернуться в главное меню"):
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Введи свой секретный код)")
        btn2 = types.KeyboardButton("❓")
        btn3 = types.KeyboardButton("Что-то еще")
        knopki.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=knopki)
    else:
        bot.send_message(message.chat.id, text="Жми на кнопку секретный код")



bot.polling(none_stop=True)







@bot.message_handler(content_types=['text'])
def textbota(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Жду твой Секретный код")
    pass
bot.polling()
