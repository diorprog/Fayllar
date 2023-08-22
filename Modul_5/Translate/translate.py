# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
# from googletrans import Translator
#
# BOT_TOKEN = '6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro'
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
#
# # Initialize the translator
# translator = Translator()
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     design = [
#         [InlineKeyboardButton("🇺🇿 UZBEK"), InlineKeyboardButton("🇷🇺 RUSSIAN"), InlineKeyboardButton("🇪🇸 SPAIN"), InlineKeyboardButton("🇹🇷 TURKEY")],
#         [InlineKeyboardButton("🇦🇱 Albanian"), InlineKeyboardButton("🇰🇷 KOREAN"), InlineKeyboardButton("🇨🇳 CHINA")]
#     ]
#     markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
#     await message.answer("Qaysi tildan ingliz tilida tarjima qilmoqchisiz: ", reply_markup=markup)
#
# @dp.message_handler(lambda msg: msg.text in ("🇺🇿 UZBEK", "🇷🇺 RUSSIAN", "🇪🇸 SPAIN", "🇹🇷 TURKEY", "🇦🇱 Albanian", "🇰🇷 KOREAN","🇨🇳 CHINA"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇨🇳 CHINA":
#         await message.answer("輸入要翻譯的單詞!")
#     elif message.text == "🇰🇷 KOREAN":
#         await message.answer("번역할 단어를 입력하세요!")
#     elif message.text == "🇦🇱 Albanian":
#         await message.answer("Futni fjalën për ta përkthyer!")
#     elif message.text == "🇺🇿 UZBEK":
#         await message.answer("Tarjima uchun so'zni kiriting!")
#     elif message.text == "🇷🇺 RUSSIAN":
#         await message.answer("Введите слово для перевода!")
#     elif message.text == "🇪🇸 SPAIN":
#         await message.answer("Introduzca la palabra para traducir!")
#     elif message.text == "🇹🇷 TURKEY":
#         await message.answer("Çevrilecek bir kelime girin!")
#
# @dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
# async def translate_word(message: types.Message):
#     try:
#         translation = translator.translate(message.text, dest='en')
#         await message.answer(f"Tarjima: {translation.text}")
#     except Exception as e:
#         logging.error(str(e))
#         await message.answer("Tarjima amalga oshmadi. Iltimos, qayta urinib ko'ring.")
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)





# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# from googletrans import Translator
#
# BOT_TOKEN = '6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro'
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
#
# # Initialize the translator
# translator = Translator()
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     design = [
#         [InlineKeyboardButton("🇺🇿 UZBEK", callback_data="uzbek"), InlineKeyboardButton("🇷🇺 RUSSIAN", callback_data="russian"), InlineKeyboardButton("🇪🇸 SPAIN", callback_data="spanish"), InlineKeyboardButton("🇹🇷 TURKEY", callback_data="turkish")],
#         [InlineKeyboardButton("🇦🇱 Albanian", callback_data="albanian"), InlineKeyboardButton("🇰🇷 KOREAN", callback_data="korean"), InlineKeyboardButton("🇨🇳 CHINA", callback_data="chinese")]
#     ]
#     markup = InlineKeyboardMarkup(inline_keyboard=design)
#     await message.answer("Qaysi tildan ingliz tilida tarjima qilmoqchisiz: ", reply_markup=markup)
#
# @dp.callback_query_handler(lambda callback_query: True)
# async def choice_handler(callback_query: types.CallbackQuery):
#     selected_language = callback_query.data
#     if selected_language == "chinese":
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(callback_query.from_user.id, "輸入要翻譯的單詞!")
#     elif selected_language == "korean":
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(callback_query.from_user.id, "번역할 단어를 입력하세요!")
#     elif selected_language == "albanian":
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(callback_query.from_user.id, "Futni fjalën për ta përkthyer!")
#     elif selected_language == "uzbek":
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(callback_query.from_user.id, "Tarjima uchun so'zni kiriting!")
#     elif selected_language == "russian":
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(callback_query.from_user.id, "Введите слово для перевода!")
#     elif selected_language == "spanish":
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(callback_query.from_user.id, "Introduzca la palabra para traducir!")
#     elif selected_language == "turkish":
#         await bot.answer_callback_query(callback_query.id)
#         await bot.send_message(callback_query.from_user.id, "Çevrilecek bir kelime girin!")
#
# @dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
# async def translate_word(message: types.Message):
#     try:
#         translation = translator.translate(message.text, dest='en')
#         await message.answer(translation.text)
#     except Exception as e:
#         logging.error(str(e))
#         await message.answer("Translation failed. Please try again.")
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)









# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
# from googletrans import Translator
#
# BOT_TOKEN = '6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro'
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
#
# # Initialize the translator
# translator = Translator()
#
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     design1 = [
#         ["English to Other Language."],
#         ["Other Language to English."]
#     ]
#     markup = ReplyKeyboardMarkup(keyboard=design1, resize_keyboard=True)
#     await message.answer("From which language you want to translate into English:", reply_markup=markup)
#
#
# @dp.message_handler(lambda msg: msg.text == "English to Other Language.")
# async def other_lan(message: types.Message):
#     design3=[
#                 [InlineKeyboardButton("Which language do you want to translate from:",callback_data="btn1")]
#     ]
#     ikm = ReplyKeyboardMarkup(inline_keyboard=design3)
#     await message.answer(reply_markup=ikm)
#
#
# @dp.message_handler(lambda msg: msg.text in ("🇺🇿 UZBEK", "🇷🇺 RUSSIAN", "🇪🇸 SPAIN", "🇹🇷 TURKEY", "🇦🇱 Albanian", "🇰🇷 KOREAN","🇨🇳 CHINA"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇨🇳 CHINA":
#         await message.answer("輸入要翻譯的單詞!")
#     elif message.text == "🇰🇷 KOREAN":
#         await message.answer("번역할 단어를 입력하세요!")
#     elif message.text == "🇦🇱 Albanian":
#         await message.answer("Futni fjalën për ta përkthyer!")
#     elif message.text == "🇺🇿 UZBEK":
#         await message.answer("Tarjima uchun so'zni kiriting!")
#     elif message.text == "🇷🇺 RUSSIAN":
#         await message.answer("Введите слово для перевода!")
#     elif message.text == "🇪🇸 SPAIN":
#         await message.answer("Introduzca la palabra para traducir!")
#     elif message.text == "🇹🇷 TURKEY":
#         await message.answer("Çevrilecek bir kelime girin!")
#
# @dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
# async def translate_word(message: types.Message):
#     try:
#         translation = translator.translate(message.text, dest='en')
#         await message.answer(f"Tarjima: {translation.text}")
#     except Exception as e:
#         logging.error(str(e))
#         await message.answer("Tarjima amalga oshmadi. Iltimos, qayta urinib ko'ring.")
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# from googletrans import Translator
#
# BOT_TOKEN = "6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
# translate = Translator()
# logging.basicConfig(level=logging.INFO)
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     design = [
#         [KeyboardButton("English to Other Language.")],
#         [KeyboardButton("Other Language to English.")]
#     ]
#     markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
#     await message.answer("From which language do you want to translate to English?", reply_markup=markup)
#
# @dp.message_handler(lambda msg: msg.text == "English to Other Language.")
# async def english_to_other_lan(message: types.Message):
#     design = [
#         [InlineKeyboardButton("🇺🇿 UZBEK", callback_data="uz"), InlineKeyboardButton("🇷🇺 RUSSIAN", callback_data="ru"), InlineKeyboardButton("🇪🇸 SPAIN", callback_data="es")],
#         [InlineKeyboardButton("🇹🇷 TURKISH", callback_data="tr")]
#     ]
#     markup = InlineKeyboardMarkup(inline_keyboard=design)
#     await message.answer("Choose the language you want to translate from:", reply_markup=markup)
#
# @dp.message_handler(lambda msg: msg.text in ("🇺🇿 UZBEK", "🇷🇺 RUSSIAN", "🇪🇸 SPAIN", "🇹🇷 TURKISH"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿 UZBEK":
#         lang="uzbek"
#         await message.answer("Tarjima uchun so'zni kiriting!")
#     elif message.text == "🇷🇺 RUSSIAN":
#         lang="russian"
#         await message.answer("Введите слово для перевода!")
#     elif message.text == "🇪🇸 SPAIN":
#         lang="spain"
#         await message.answer("Introduzca la palabra para traducir!")
#     elif message.text == "🇹🇷 TURKISH":
#         lang="turkey"
#         await message.answer("Çevrilecek bir kelime girin!")
#
# @dp.message_handler(lambda msg: msg.text and not msg.text.startswith('/'))
# async def translate_to_english(message: types.Message, lang=None):
#     try:
#         translation = translate.translate(message.text, dest=lang)
#         await message.answer(translation.text)
#     except Exception as e:
#         logging.error(str(e))
#         await message.answer("Translation failed. Please try again.")
#
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)



#, "🇦🇱 Albanian", "🇰🇷 KOREAN","🇨🇳 CHINA"))
# elif message.text == "🇰🇷 KOREAN":
    #     await message.answer("번역할 단어를 입력하세요!")
    # elif message.text == "🇦🇱 Albanian":
    #     await message.answer("Futni fjalën për ta përkthyer!")
    # elif message.text == "🇨🇳 CHINA":
    #     await message.answer("輸入要翻譯的單詞!")


# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# from googletrans import Translator
#
# BOT_TOKEN = "6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
#
# logging.basicConfig(level=logging.INFO)
#
# # Tarjima uchun Translator obyektini yaratish
# translator = Translator()
#
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     design = [
#         [KeyboardButton("English to Other Language.")],
#         [KeyboardButton("Other Language to English.")]
#     ]
#     markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
#     await message.answer("From which language do you want to translate to English?", reply_markup=markup)
#
#
# @dp.message_handler(lambda msg: msg.text == "English to Other Language.")
# async def english_to_other_lan(message: types.Message):
#     design = [
#         [InlineKeyboardButton("🇺🇿 UZBEK", callback_data="uz"),
#          InlineKeyboardButton("🇷🇺 RUSSIAN", callback_data="ru"),
#          InlineKeyboardButton("🇪🇸 SPANISH", callback_data="es")],
#         [InlineKeyboardButton("🇹🇷 TURKISH", callback_data="tr")]
#     ]
#     markup = InlineKeyboardMarkup(inline_keyboard=design)
#     await message.answer("Choose the language you want to translate from:", reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda callback_query: callback_query.data in ["uz", "ru", "es", "tr"])
# async def choice_handler(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#
#     selected_language = callback_query.data
#     await bot.send_message(callback_query.from_user.id,
#                            f"Enter the word you want to translate from {selected_language}:")
#
#
# @dp.message_handler(lambda msg: msg.text and not msg.text.startswith('/'))
# async def translate_to_english(message: types.Message):
#     try:
#         translation = translator.translate(message.text, dest="en")
#         await message.answer(translation.text)
#     except Exception as e:
#         logging.error(str(e))
#         await message.answer("Translation failed. Please try again.")
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)




# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# from googletrans import Translator
#
# BOT_TOKEN = "6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
# translator = Translator()
#
# # Initial keyboard layout with language options
# language_selection_keyboard = ReplyKeyboardMarkup(
#     resize_keyboard=True,
#     keyboard=[
#         [KeyboardButton("From Language"), KeyboardButton("To Language")]
#     ]
# )
#
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer("Welcome to the translation bot! Please select the languages:",
#                          reply_markup=language_selection_keyboard)
#
#
# # Dictionary to store user selected languages
# user_languages = {}
#
#
# @dp.message_handler(lambda message: message.text.lower() in ["from language", "to language"])
# async def choose_language(message: types.Message):
#     await message.answer(f"Please enter the {message.text.lower()} (e.g., 'en' for English):")
#     user_languages[message.text.lower()] = None
#
#
# @dp.message_handler(lambda message: True)
# async def translate_text(message: types.Message):
#     if "from language" in user_languages and "to language" in user_languages:
#         from_lang = user_languages["from language"]
#         to_lang = user_languages["to language"]
#
#         if from_lang and to_lang:
#             try:
#                 translation = translator.translate(message.text, src=from_lang, dest=to_lang)
#                 translated_text = translation.text
#                 await message.answer(f"Translated: {translated_text}")
#             except Exception as e:
#                 await message.answer("An error occurred during translation.")
#         else:
#             await message.answer("Please select both 'From Language' and 'To Language'.")
#     else:
#         await message.answer("Please select both 'From Language' and 'To Language'.")
#
#
# if __name__ == '__main__':
#     from aiogram import executor
#
#     executor.start_polling(dp, skip_updates=True)




# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from googletrans import Translator
#
# BOT_TOKEN = "6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
# translator = Translator()
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     markup = InlineKeyboardMarkup(row_width=1)
#     languages_button = InlineKeyboardButton("Select Languages", callback_data='select_languages')
#     markup.add(languages_button)
#     await message.reply("Welcome to the translation bot! Please select the languages you want to translate between.", reply_markup=markup)
#
# @dp.callback_query_handler(text_contains='select_languages')
# async def select_languages(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, "Enter the source language:")
#     await bot.register_next_step_handler(callback_query.message, get_source_language)
#
# async def get_source_language(message: types.Message):
#     message_text = message.text.strip().lower()
#     message.chat['source_language'] = message_text
#     await message.reply("Enter the target language:")
#     await bot.register_next_step_handler(message, get_target_language)
#
# async def get_target_language(message: types.Message):
#     message_text = message.text.strip().lower()
#     message.chat['target_language'] = message_text
#     await message.reply(f"You've selected {message.chat['source_language']} to {message.chat['target_language']} translation.\n"
#                         "Now enter the word you want to translate:")
#
# @dp.message_handler(lambda message: 'source_language' in message.chat and 'target_language' in message.chat)
# async def translate(message: types.Message):
#     source_lang = message.chat['source_language']
#     target_lang = message.chat['target_language']
#     word = message.text.strip()
#
#     try:
#         translation = translator.translate(word, src=source_lang, dest=target_lang)
#         await message.reply(f"Translation: {translation.text}")
#     except Exception as e:
#         await message.reply("An error occurred while translating. Please try again later.")
#
# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)



import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, CallbackQueryHandler

# Import Google Cloud Translation API
from google.cloud import translate_v2 as translate

# Set up your Google Cloud credentials (replace 'path/to/your/key.json' with the actual path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/key.json"

# Initialize the Google Cloud Translation client
translate_client = translate.Client()

# Define your Telegram bot token
TOKEN = "6348526580:AAH1LbUkaqH4XGzCj8gDnfZ2IKU6kWA-mro"

# Handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("From English to French", callback_data='en-fr')],
        [InlineKeyboardButton("From French to English", callback_data='fr-en')],
        # Add more language pairs here
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Select a translation direction:", reply_markup=reply_markup)

# Handler for inline keyboard button callbacks
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    context.user_data['language_pair'] = query.data
    query.edit_message_text(text=f"Selected: {query.data}\nEnter the text to translate.")

# Handler for text messages
def translate_text(update: Update, context: CallbackContext) -> None:
    if 'language_pair' not in context.user_data:
        update.message.reply_text("Please select a translation direction using the buttons.")
        return

    language_pair = context.user_data['language_pair']
    source_lang, target_lang = language_pair.split('-')

    text_to_translate = update.message.text
    translation = translate_client.translate(text_to_translate, source_language=source_lang, target_language=target_lang)

    update.message.reply_text(f"Translated: {translation['translatedText']}")

def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
