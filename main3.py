# import telebot

# API_TOKEN = "7166981544:AAH2oX0DRvRwPQRhH2Kq2FRo8NCjxSNi8SI"
# bot = telebot.TeleBot(API_TOKEN)

# user_data = {}
# user_states = {}


# STATE_WAITING_NAME = 'waiting_name'
# STATE_WAITING_AGE = 'waiting_age'
# STATE_WAITING_EMAIL = 'waiting_email'

# @bot.message_handler(commands=['register'])
# def start_registration(message):
#     chat_id = message.chat.id
#     user_states[chat_id] = STATE_WAITING_NAME
#     bot.reply_to(message, "Введите свое имя!")

# @bot.message_handler(func=lambda message: message.chat.id in user_states)
# def handle_message(message):
#     chat_id = message.chat.id
#     state = user_states.get(chat_id)

#     if state == STATE_WAITING_NAME:
#         handle_name(message)
#     if state == STATE_WAITING_AGE:
#         handle_age(message)
#     if state == STATE_WAITING_EMAIL:
#         handle_email(message)

# def handle_name(message):
#     chat_id = message.chat.id
#     user_data[chat_id] = {'name': message.text}
#     user_states[chat_id] = STATE_WAITING_AGE
#     bot.reply_to(message, "Введите ваше возвраст:")

# def handle_age(message):
#     chat_id = message.chat.id
#     user_data[chat_id]['age'] = message.text
#     user_states[chat_id] = STATE_WAITING_EMAIL
#     bot.reply_to(message, "Введите ваш email")

# def handle_email(message):
#     chat_id = message.chat.id
#     user_data[chat_id]['email'] = message.text
#     text_user_info = (
#         'Регистрация завершена!\n'
#         f'Имя: {user_data[chat_id]["name"]}\n'        
#         f'Возвраст: {user_data[chat_id]["age"]}\n'
#         f'Почта: {user_data[chat_id]["email"]}\n'        
#     )
#     bot.reply_to(message, text_user_info)
#     del user_states[chat_id]    
#     del user_data[chat_id]

# bot.polling()    





import telebot

API_KEY = '7166981544:AAH2oX0DRvRwPQRhH2Kq2FRo8NCjxSNi8SI'
bot = telebot.TeleBot(API_KEY)

# Словарь для хранения состояния и данных регистрации
user_data = {}
user_states = {}
 
# Определение состояний
STATE_WAITING_NAME = 'waiting_name'
STATE_WAITING_AGE = 'waiting_age'
STATE_WAITING_EMAIL = 'waiting_email'

@bot.message_handler(commands=['register'])
def start_registration(message):
    chat_id = message.chat.id
    user_states[chat_id] = STATE_WAITING_NAME
    bot.reply_to(message, "Введите ваше имя:")

@bot.message_handler(func=lambda message: message.chat.id in user_states)
def handle_message(message):
    chat_id = message.chat.id
    state = user_states.get(chat_id)

    if state == STATE_WAITING_NAME:
        handle_name(message)
    elif state == STATE_WAITING_AGE:
        handle_age(message)
    elif state == STATE_WAITING_EMAIL:
        handle_email(message)

def handle_name(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'name': message.text}
    user_states[chat_id] = STATE_WAITING_AGE
    bot.reply_to(message, "Введите ваш возраст:")

def handle_age(message):
    chat_id = message.chat.id
    user_data[chat_id]['age'] = message.text
    user_states[chat_id] = STATE_WAITING_EMAIL
    bot.reply_to(message, "Введите ваш email:")

def handle_email(message):
    chat_id = message.chat.id
    user_data[chat_id]['email'] = message.text
    # Завершение регистрации
    bot.reply_to(message, f"Регистрация завершена!\nИмя: {user_data[chat_id]['name']}\nВозраст: {user_data[chat_id]['age']}\nEmail: {user_data[chat_id]['email']}")
    # Очистка состояния и данных
    del user_states[chat_id]
    del user_data[chat_id]

bot.polling()