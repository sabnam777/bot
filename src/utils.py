import os
import time
import requests
from telegram import InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

def send_photo(chat_id, photo_url):
    response = requests.get(photo_url)
    photo = InputMediaPhoto(io.BytesIO(response.content))
    context.bot.send_photo(chat_id=chat_id, photo=photo)

def send_text_message(chat_id, text):
    context.bot.send_message(chat_id=chat_id, text=text)

def send_photo_with_buttons(chat_id, photo_url, caption, reply_markup):
    response = requests.get(photo_url)
    photo = InputMediaPhoto(io.BytesIO(response.content), caption=caption)
    context.bot.send_photo(chat_id=chat_id, photo=photo, reply_markup=reply_markup)

def get_file_path(file_id):
    file_path = context.bot.get_file(file_id).file_path
    return f'https://api.telegram.org/file/bot{os.environ.get("TELEGRAM_BOT_TOKEN")}/{file_path}'

def ask_for_scale_factor(chat_id):
    text = 'Please enter the scale factor (default: 2):'
    message = context.bot.send_message(chat_id=chat_id, text=text)
    response = message.text.strip()
    return int(response) if response else 2

def ask_for_face_enhance(chat_id):
    text = 'Do you want to enable face enhance? (yes or no, default: no):'
    message = context.bot.send_message(chat_id=chat_id, text=text)
    response = message.text.strip().lower()
    return response == 'yes'

def get_ping_time():
    start_time = time.time()
    response = requests.get('https://www.google.com')
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000)
    dc = response.headers['X-Datacenter']
    return ping_time, dc
