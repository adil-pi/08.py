import telebot
import random
from telebot import types
import speech_recognition as sr
from pydub import AudioSegment
import os

# Замените 'YOUR_BOT_TOKEN' на ваш реальный токен, полученный от BotFather
API_TOKEN = 'YOUR_BOT_TOKEN'
pydub.AudioSegment.converter = "C:/Program Files (x86)/Microsoft/Edge/Application/126.0.2592.113/ffmpeg.exe"

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message): 
    # создание кнопок
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/rad')
    markup.add(btn1, btn2)

    # отправка сообщения юзеру
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите команду:", reply_markup=markup)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "<b>Доступные команды:</b>\n"
        "/start - начать взаимодействие с ботом\n"
        "/rad - отправить случайное изображение\n"
        "/help - получить помощь и информацию о командах\n"
    )
    bot.reply_to(message, help_text)

# Обработчик команды /rad
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

    try:
        # Выбираем случайное число от 0 до 9
        random_index = random.randint(0, 2)
        image_path = f"./img/image{random_index}.jpg"
        
        # Отправляем изображение пользователю
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file, reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


# Обработчик голосовых сообщений
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        voice_ogg_path = "voice.ogg"
        voice_wav_path = "voice.wav"

        with open(voice_ogg_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Конвертируем ogg в wav
        audio = AudioSegment.from_ogg(voice_ogg_path)
        audio.export(voice_wav_path, format="wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile(voice_wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            bot.reply_to(message, f"Вы сказали: {text}")

        # Удаляем временные файлы
        os.remove(voice_ogg_path)
        os.remove(voice_wav_path)
    except Exception as e:
        bot.reply_to(message, f"Не удалось распознать голосовое сообщение. Ошибка: {e}")

# Обработчик входящих изображений
@bot.message_handler(content_types=['photo', 'video', 'sticker'])
def handle_image(message):
    choice = random.choice(['😍', '👍', '👎', 'Ну такое...']) 
    bot.reply_to(message, choice)

# Обработчик текстовых сообщений
@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Я не хочу разговаривать на эту тему...</b>")

# Запуск бота
bot.polling()
