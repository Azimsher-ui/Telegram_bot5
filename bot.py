from telebot import TeleBot, types
token = "8375049997:AAHd8vq0JwB6QB3uHdSDYfy6cjAc5TxIZV4"
bot = TeleBot(token)
CHANNELS = [
    "@python_sila_iii"
]
def check_user(user_id):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch, user_id).status
            if status in ['left', 'kicked']:
                return False
        except:
            return False
    return True
def IsSubscribe(chat_id):
    markup = types.InlineKeyboardMarkup()
    for ch in CHANNELS:
        markup.add(types.InlineKeyboardButton(text=ch, url=f"https://t.me/{ch[1:]}"))
    markup.add(types.InlineKeyboardButton("✅Tekshirish", callback_data="check"))
    bot.send_message(chat_id, "Botdan foydalanish uchun kanallarga obuna bo'lishingiz kerak!Agar obuna bo'lmasang sur bo'ttan bo't", reply_markup=markup)
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_user(user_id):
        bot.send_message(message.chat.id, "Botdan foydalanishingiz mumkin!😁")
        markup=types.InlineKeyboardMarkup()
        button1=types.InlineKeyboardButton("⚡Sonic 4",callback_data="sonic" )
        button2=types.InlineKeyboardButton("🎮Minecraft movie",callback_data="minecraft" )
        button3=types.InlineKeyboardButton("🤖Pacific Rim 2",callback_data="rim2" )
        button4=types.InlineKeyboardButton("🧟Zombielend",callback_data="zombie" )
        button5=types.InlineKeyboardButton("⚽Bluelock",callback_data="bluelock" )
        button6=types.InlineKeyboardButton("🤖Pacific Rim",callback_data="rim" )
        button7=types.InlineKeyboardButton("🦔Sonic 3",callback_data="sonic3" )
        button8=types.InlineKeyboardButton("🦸Avengers Doomsday",callback_data="avengers" )
        button9=types.InlineKeyboardButton("3️⃣Uch qahramon",callback_data="uch" )
        button10=types.InlineKeyboardButton("🔥Pele",callback_data="pele" )
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)
        markup.add(button5)
        markup.add(button6)
        markup.add(button7)
        markup.add(button8)
        markup.add(button9)
        markup.add(button10)
        bot.send_message(message.chat.id,"Film tanlang",reply_markup=markup)
    else:
        IsSubscribe(message.chat.id)
@bot.callback_query_handler(func=lambda call:True)
def quer(call):
    user_id = call.from_user.id
    if check_user(user_id):
        if call.data == "sonic":
            a=open("351b673f.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "minecraft":
            a=open("4f31794e-477b-4c28-b0ab-dda35af496ac.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "rim2":
            a=open("pacific.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "zombie":
            a=open("zombie.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "bluelock":
            a=open("bluelock.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "rim":
            a=open("rim.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "sonic3":
            a=open("sonic.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "avengers":
            a=open("avengers.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "uch":
            a=open("uch.mp4","rb")
            bot.send_video(call.message.chat.id,a)
        elif call.data == "pele":
            a=open("pele.mp4","rb")
            bot.send_video(call.message.chat.id,a)
    else:
        IsSubscribe(call.message.chat.id)    

@bot.callback_query_handler(func=lambda call: call.data == "check")
def check_callback(call):
    user_id = call.from_user.id
    if check_user(user_id):
        bot.send_message(call.message.chat.id, "Botdan foydalanishingiz mumkin!")
    else:
        bot.answer_callback_query(call.id, "Barcha kanallarga obuna bo'lmagansiz!\nObuna bo'ling!")
        IsSubscribe(call.message.chat.id)
@bot.message_handler(func=lambda message: True)
def send(message):
    user_id = message.from_user.id
    if not check_user(user_id):
        IsSubscribe(message.chat.id)
        return
    bot.send_message(message.chat.id, f"Siz yozdingiz: {message.text}")
    b=message.text
    if int(b)==1:
        a=open("351b673f.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==2:
        a=open("4f31794e-477b-4c28-b0ab-dda35af496ac.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==3:
        a=open("pacific.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==4:
        a=open("zombie.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==5:
        a=open("bluelock.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==6:
        a=open("rim.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==7:
        a=open("sonic.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==8:
        a=open("avengers.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==9:
        a=open("uch.mp4","rb")
        bot.send_video(message.chat.id,a)
    elif int(b)==10:
        a=open("pele.mp4","rb")
        bot.send_video(message.chat.id,a)
print("Dastur ishga tushdi!")
bot.infinity_polling()