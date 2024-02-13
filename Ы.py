import telebot
from telebot import types
bot = telebot.TeleBot("6558386511:AAHOiiVOAeXH1NAVgxOItOx-qIVmady0tqw")
@bot.message_handler(commands = ["start"])
def test2(m):
    bot.send_message(m.chat.id, "привет  "+m.from_user.first_name)

score = 0

@bot.message_handler(commands = ['basket'])
def game(m):
    global score
    dicemsg = bot.send_dice(m.chat.id, "🏀")
    result = dicemsg.dice.value
    print(result)
    if result == 5:
        bot.send_message(m.chat.id, 'вы джордан?')
    else:
        bot.send_message(m.chat.id, "вы криворук:(")
    score+= result
    bot.send_message(m.chat.id, "ваш счет: "+str(score))


@bot.message_handler(commands = ['spidybutton'])
def spidybutton(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)

    kb.add(types.KeyboardButton("🕷Начать босса🕷"))



    bot.send_message(m.chat.id, "кнопка", reply_markup = kb)
@bot.message_handler()
def test (m):
    if m.text == "🕷Начать босса🕷":
        bot.send_photo(m.chat.id, "https://avatars.dzeninfra.ru/get-zen_doc/2436983/pub_64a2b035e6b5371cc96c38d9_64a2b5b602f3c51219af24f7/scale_1200",caption = "ваш босс это зеленый гоблин")

bot.infinity_polling()
