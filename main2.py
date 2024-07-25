# import telebot
# import sqlite3

# API_TOKEN = "7166981544:AAH2oX0DRvRwPQRhH2Kq2FRo8NCjxSNi8SI"

# bot = telebot.TeleBot(API_TOKEN, parse_mode="HTML")

# conn = sqlite3.connect('users.db', check_same_thread=False)
# cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER UNIQUE,
#     username TEXT
# )
# ''')
# conn.commit()

# text_message = ""
# image_file_id = None

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     user_id = message.from_user.id
#     username = message.from_user.username

#     cursor.execute('''
#     SELECT * FROM users WHERE user_id = ?
#     ''', (user_id,))
#     existing_user = cursor.fetchone()

#     if existing_user:
#         print(f"Пользователь {username} уже есть в базе данных")
#     else:
#         cursor.execute('''
#         INSERT INTO users (user_id, username)
#         VALUES (?, ?)
#         ''', (user_id, username))
#         conn.commit()
#         print(f"Пользовватель {username} успешно добавлен в DB")

#     bot.send_message(message.chat.id, "Добро пожаловать!")


# @bot.message_handler(commands=['send'])
# def handle_send(message):
#     # Является ли пользователь админом
#     if message.from_user.id != 6704787842:
#         bot.reply_to(message, "Ты кто? Пошел ты!!!")
#         return

#     bot.send_message(message.chat.id, 'Отправить текст для рассылки')
#     bot.register_next_step_handler(message, process_text)

# def process_text(message):
#     global text_message
#     text_message = message.text
#     bot.send_message(message.chat.id, "Отправте картинку длля рассылки, или команду /done")
#     bot.register_next_step_handler(message, process_image)

# def process_image(message):
#     global image_file_id
#     if message.photo:
#         image_file_id = message.photo[-1].file_id
#         bot.send_message(message.chat.id, "Изображение получено. Рассылка будет выполнена.")
#     elif message.text == '/done':
#         bot.send_message(message.chat.id, "Рассылка завершена.")
#     else:
#         bot.send_message(message.chat.id, "Отправьте изображение или напишите /done.")
#         return

#     # Запуск рассылки сообщений
#     send_broadcast()

# def send_broadcast():
#     global text_message, image_file_id
#     cursor.execute('SELECT user_id FROM users')
#     users = cursor.fetchall()

#     for user in users:
#         user_id = user[0]
#         try:
#             if image_file_id:
#                 bot.send_photo(user_id, photo=image_file_id, caption=text_message)
#             else:
#                 bot.send_message(user_id, text_message)
#         except Exception as e:
#             print(f"Ошибка пользователем {user_id}: {e}")
#     text_message = ""
#     image_file_id = None



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