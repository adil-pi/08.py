
# import telebot 
# import random 
 
# API_TOKEN = "7093621172:AAH4Q58ghuDP7hAVGfAdMu4bfEeM-3DgVG0" 
# bot = telebot.TeleBot(API_TOKEN) 
 
 
# @bot.message_handler(commands=['start']) 
# def send_welcome(message): 
#     bot.reply_to(message, "Добро пожаловать!") 
 
 
# @bot.message_handler(commands=['help']) 
# def send_help(message): 
#     help_text = ( 
#         "<b>Доступные команды:</b>\n" 
#         "/start - начать взаимодействие с ботом\n" 
#         "/register - отправить случайное изображение\n" 
#         "/help - получить помощь и информацию о командах\n" 
 
#     ) 
#     bot.reply_to(message, help_text) 
 
 
 
# @bot.message_handler(commands=['rad']) 
# def send_random_image(message): 
#     try: 
#         # Выбираем случайное число от 0 до 9 
#         random_index = random.randint(0, 2) 
#         image_path = f"./img/image{random_index}.jpg" 
         
#         # Отправляем изображение пользователю 
#         with open(image_path, 'rb') as image_file: 
#             bot.send_photo(message.chat.id, image_file ) 
#     except Exception as e: 
#         bot.reply_to(message, f"Произошла ошибка: {e}") 
 
 
# user_data = {} 
# user_states = {} 
  
# # Определение состояний 
# STATE_WAITING_NAME = 'waiting_name' 
# STATE_WAITING_AGE = 'waiting_age' 
# STATE_WAITING_EMAIL = 'waiting_email' 
 
# @bot.message_handler(commands=['register']) 
# def start_registration(message): 
#     chat_id = message.chat.id 
#     user_states[chat_id] = STATE_WAITING_NAME 
#     bot.reply_to(message, "Введите ваше имя:") 
 
# @bot.message_handler(func=lambda message: message.chat.id in user_states) 
# def handle_message(message): 
#     chat_id = message.chat.id 
#     state = user_states.get(chat_id) 
 
#     if state == STATE_WAITING_NAME: 
#         handle_name(message) 
#     elif state == STATE_WAITING_AGE: 
#         handle_age(message) 
#     elif state == STATE_WAITING_EMAIL: 
#         handle_email(message) 
 
# def handle_name(message): 
#     chat_id = message.chat.id 
#     user_data[chat_id] = {'name': message.text} 
#     user_states[chat_id] = STATE_WAITING_AGE 
#     bot.reply_to(message, "Введите ваш возраст:") 
 
# def handle_age(message): 
#     chat_id = message.chat.id 
#     user_data[chat_id]['age'] = message.text 
#     user_states[chat_id] = STATE_WAITING_EMAIL 
#     bot.reply_to(message, "Введите ваш email:") 
 
# def handle_email(message): 
#     chat_id = message.chat.id 
#     user_data[chat_id]['email'] = message.text 
#     # Завершение регистрации 
#     bot.reply_to(message, f"Регистрация завершена!\nИмя: {user_data[chat_id]['name']}\nВозраст: {user_data[chat_id]['age']}\nEmail: {user_data[chat_id]['email']}") 
#     # Очистка состояния и данных 
#     del user_states[chat_id] 
#     del user_data[chat_id] 
 
 
# bot.polling()


# 7166981544:AAH2oX0DRvRwPQRhH2Kq2FRo8NCjxSNi8SI

import telebot
import requests
import json
from telebot import types

API_TOKEN = "7047802868:AAHJu3I7qpblv3SSuzfORK9WHtIU9ZwOMps"
bot = telebot.TeleBot(API_TOKEN, parse_mode="HTML")


@bot.message_handler(commands=['start']) 
def send_welcome(message): 
    # создание кнопок
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/rad')
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Добро пожаловать! Выберите команду:", reply_markup=markup)

@bot.message_handler(commands=['rad'])
def send_random_image(message):
    # первая колонка
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Кнопка 1', url='https://t.me/+Uuv83tzKFXpkNzMy')
    markup.add(btn1)

    # Вторая и третья кнопки в одной строке под первой кнопкой
    btn2 = types.InlineKeyboardButton('Кнопка 2', url='https://t.me/+Uuv83tzKFXpkNzMy')
    btn3 = types.InlineKeyboardButton('Кнопка 3', url='https://t.me/+Uuv83tzKFXpkNzMy')
    markup.row(btn2, btn3)

    bot.reply_to(message, "Добро пожаловать!") 

@bot.message_handler(commands=['help']) 
def send_help(message): 
    help_text = ( 
        "<b>Доступные команды:</b>\n" 
        "/start - начать взаимодействие с ботом\n" 
        "/help - получить помощь и информацию о командах\n" 
    ) 
    bot.reply_to(message, help_text) 

@bot.message_handler(commands=['joke'])
def get_random_joke(message):
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    joke_data = json.loads(response.text)
    bot.send_message(message.chat.id, joke_data['setup'])
    bot.send_message(message.chat.id, joke_data['punchline'])

bot.polling()