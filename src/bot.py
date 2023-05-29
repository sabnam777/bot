import requests
import io
import os
from PIL import Image
from telegram import InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup
from replicate import ReplicateAPI
import config
import utils

class Bot:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.replicate_api = ReplicateAPI(config.REPLICATE_API_TOKEN)

    def send_start_message(self):
        photo_url = 'https://i.imgur.com/7JQv1bL.jpg'
        caption = 'Welcome to the Real-ESRGAN Telegram Bot!'

        button1 = InlineKeyboardButton('Join Akimax', url='https://t.me/akimax')
        button2 = InlineKeyboardButton('Join AkimaxMovies', url='https://t.me/akimaxmovies')
        button3 = InlineKeyboardButton('Contact the Developer', url='https://t.me/bae_wafa')

        keyboard = [[button1, button2, button3]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        utils.send_photo_with_buttons(self.chat_id, photo_url, caption, reply_markup)

    def send_help_message(self):
        photo_url = 'https://i.imgur.com/7JQv1bL.jpg'
        caption = 'To use the Real-ESRGAN Telegram Bot, simply send an image to the bot, and it will enhance the image quality using the Real-ESRGAN API and send the enhanced image back to you.'

        button1 = InlineKeyboardButton('Example', callback_data='example')
        button2 = InlineKeyboardButton('Close', callback_data='close')

        keyboard = [[button1, button2]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        utils.send_photo_with_buttons(self.chat_id, photo_url, caption, reply_markup)

    def send_about_message(self):
        photo_url = 'https://i.imgur.com/7JQv1bL.jpg'
        caption = 'My Info\n\nName: Real-ESRGAN Telegram Bot\nCredit: @bae_wafa\nLanguage: Python3\nLibrary: v2.0.106\nServer: VPS\nBuild: V2.0'

        button1 = InlineKeyboardButton('Close', callback_data='close')

        keyboard = [[button1]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        utils.send_photo_with_buttons(self.chat_id, photo_url, caption, reply_markup)

    def send_ping_message(self):
        ping_time, dc = utils.get_ping_time()
        caption = f'Ping: {ping_time} ms\nData Center: {dc}'

        utils.send_text_message(self.chat_id, caption)

    def handle_image(self, message):
        # Get the file ID of the photo
        file_id = message.photo[-1].file_id if message.photo else message.document.file_id

        # Get the file path from the file ID
        file_path = utils.get_file_path(file_id)

        # Download the image file
        response = requests.get(file_path)
        image = Image.open(io.BytesIO(response.content))

        # Ask the user for the scale factor and face enhance option
        scale_factor = utils.ask_for_scale_factor(self.chat_id)
        face_enhance = utils.ask_for_face_enhance(self.chat_id)

        # Enhance the image using the Real-ESRGAN API
        output_uri = self.replicate_api.enhance_image(image, scale_factor=scale_factor, face_enhance=face_enhance)

        # Send the enhanced image to the user
        utils.send_photo(self.chat_id, output_uri)
