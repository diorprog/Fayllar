#  Spotifydan musiqa yuklash
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from aiogram import Bot, Dispatcher, types, executor

BOT_TOKEN = '6348363410:AAFTR0jwutVLCdiszzxK8GXh5eib_aho__M'
SPOTIPY_CLIENT_ID = '27d615576ce74ccfb4ef5f09c36bff2e'
SPOTIPY_CLIENT_SECRET = 'c6b0a6983f6e43ea8d3b6e6de992c992'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Initialize Spotipy client
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Salom! Musiqa qidirish uchun /search buyrug'ini kiriting.")


@dp.message_handler(commands=['search'])
async def search_handler(message: types.Message):
    await message.answer("Iltimos, qidirish uchun so'zni kiriting.")


@dp.message_handler(lambda message: message.text and message.text.startswith('/search'))
async def search_music(message: types.Message):
    query = message.text.split('/search', 1)[1].strip()

    try:
        results = sp.search(query, type='track', limit=1)
        if results and 'tracks' in results and 'items' in results['tracks']:
            track = results['tracks']['items'][0]
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            preview_url = track['preview_url']

            if preview_url:
                await message.answer(
                    f"Musiqa topildi:\nNom: {track_name}\nArtist: {artist_name}\nSizga eshitish uchun: {preview_url}")
            else:
                await message.answer("Ma'lumotlar topilmadi.")
        else:
            await message.answer("Musiqa topilmadi.")
    except Exception as e:
        await message.answer("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


















#youtube instagram chromeni t.meda ochish
import Filters as Filters
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
#
# BOT_TOKEN = '6348363410:AAFTR0jwutVLCdiszzxK8GXh5eib_aho__M'
#
# bot = Bot(BOT_TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start_handler(message:types.Message):
#     design = [
#         [InlineKeyboardButton("You Tube",web_app=({"url":"https://www.youtube.com"})), InlineKeyboardButton("Instagram", web_app=({"url":"https://www.instagram.com/?hl=ru"}))],
#         [InlineKeyboardButton("Google Chrome",web_app=({"url":"https://www.google.com"}))]
#     ]
#
#     ikm=InlineKeyboardMarkup(inline_keyboard=design)
#     await  message.answer("Inline keyboard show",reply_markup=ikm)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)




#video yuklash

#
# import logging
# import asyncio
#
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
#
# # Set up logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
#
#
# # Define a function to handle the /start command
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Assalomu alaykum! Videoni yuboring.')
#
#
# # Define a function to handle video messages
# async def handle_video(update: Update, context: CallbackContext) -> None:
#     video_file = update.message.video
#     file_id = video_file.file_id
#     await context.bot.send_message(chat_id=update.message.chat_id, text=f"Video qabul qilindi! File ID: {file_id}")
#
#
# async def main():
#     # Replace 'YOUR_BOT_TOKEN' with your actual bot token
#     bot_token = '6348363410:AAFTR0jwutVLCdiszzxK8GXh5eib_aho__M'
#
#     updater = Updater(token=bot_token, use_context=True)
#     dispatcher = updater.dispatcher
#
#     # Add handlers for commands and messages
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(MessageHandler(Filters.video, handle_video))
#
#     # Start the bot
#     await updater.start_polling()
#
#     # Run the bot until you press Ctrl-C
#     updater.idle()
#
#
# if __name__ == '__main__':
#     asyncio.run(main())



#musiqa nomi orqali qidiruv


# import logging
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
#
# # Bu funksiya /start buyrug'iga javob beradi
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Assalomu alaykum! Botimizga xush kelibsiz. Musiqa nomini yuboring.')
#
# # Bu funksiya foydalanuvchi xaberi kelganda ishlaydi
# def echo(update: Update, context: CallbackContext) -> None:
#     musiqa_nomi = update.message.text
#     update.message.reply_text(f'Siz "{musiqa_nomi}" musiqasini qidirib chiqaringiz.')
#
# def main() -> None:
#     # Bu sizning bot tokeningiz bo'lishi kerak
#     bot_token = 'BOT_TOKEN'
#
#     updater = Updater(token=bot_token)
#
#     dispatcher = updater.dispatcher
#
#     # /start buyrug'iga javob berish uchun handler
#     dispatcher.add_handler(CommandHandler("start", start))
#
#     # Foydalanuvchi xaberi kelganda ishlaydigan handler
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
#
#     updater.start_polling()
#
#     updater.idle()
#
# if __name__ == '__main__':
#     main()




#musiqa matni orqali qidiruv



# import logging
# import asyncio
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
#
# # Telegram bot tokenini quyidagi o'zgaruvchiga o'zgartiring
# TOKEN = "BOT_TOKEN"
#
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#
# # Musiqa matnini saqlash uchun lug'at
# music_texts = {
#     "song1": "Musiqa matni 1",
#     "song2": "Musiqa matni 2",
#     # Boshqa musiqa matnlarni ham qo'shishingiz mumkin
# }
#
# # /qidir komandasi uchun handler
# async def qidir(update: Update, context: CallbackContext) -> None:
#     chat_id = update.message.chat_id
#     text = update.message.text[7:]  # /qidirdan keyin kelgan matn
#     if text in music_texts:
#         await update.message.reply_text(music_texts[text])
#     else:
#         await update.message.reply_text("Musiqa topilmadi")
#
# async def main():
#     updater = Updater(token=TOKEN, use_context=True)
#     dp = updater.dispatcher
#
#     dp.add_handler(CommandHandler("qidir", qidir))
#
#     await updater.start_polling()
#     await updater.idle()
#
# if __name__ == '__main__':
#     asyncio.run(main())
