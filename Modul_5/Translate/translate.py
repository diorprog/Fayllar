# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from googletrans import Translator
#
# logging.basicConfig(level=logging.INFO)
#
# BOT_TOKEN = "6357742300:AAFp8yUNJA1LTArfUBFdUKL6jWKFLxnyi5s"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
#
# translator = Translator()
#
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(types.KeyboardButton("Uzbek"))
#     keyboard.add(types.KeyboardButton("English"))
#     keyboard.add(types.KeyboardButton("Russian"))
#     keyboard.add(types.KeyboardButton("Turkish"))
#
#     await message.answer("Istalgan tildan 👇 tillarga tarjima qilish uchun tanlang: ", reply_markup=keyboard)
#
#
# @dp.message_handler(lambda message: message.text.lower() == "uzbek")
# async def translate_to_uzbek(message: types.Message):
#     await message.answer("Please enter the text you want to translate to Uzbek:")
#
#     @dp.message_handler(lambda message: message.text)
#     async def translate_text_to_uzbek(message: types.Message):
#         text_to_translate = message.text
#
#         try:
#             translation = translator.translate(text_to_translate, src='auto', dest="uz")
#             translated_text = translation.text
#             await message.answer(f"Translated text to Uzbek: {translated_text}")
#         except Exception as e:
#             await message.answer("An error occurred while translating. Please try again later.")
#
#
# @dp.message_handler(lambda message: message.text.lower() == "english")
# async def translate_to_english(message: types.Message):
#     await message.answer("Please enter the text you want to translate to English:")
#
#     @dp.message_handler(lambda message: message.text)
#     async def translate_text_to_english(message: types.Message):
#         text_to_translate = message.text
#
#         try:
#             translation = translator.translate(text_to_translate, src='auto', dest="en")
#             translated_text = translation.text
#             await message.answer(f"Translated text to English: {translated_text}")
#         except Exception as e:
#             await message.answer("An error occurred while translating. Please try again later.")
#
#
# @dp.message_handler(lambda message: message.text.lower() == "russian")
# async def translate_to_russian(message: types.Message):
#     await message.answer("Please enter the text you want to translate to Russian:")
#
#     @dp.message_handler(lambda message: message.text)
#     async def translate_text_to_russian(message: types.Message):
#         text_to_translate = message.text
#
#         try:
#             translation = translator.translate(text_to_translate, src='auto', dest="russian")
#             translated_text = translation.text
#             await message.answer(f"Translated text to Russian: {translated_text}")
#         except Exception as e:
#             await message.answer("An error occurred while translating. Please try again later.")
#
#
# @dp.message_handler(lambda message: message.text.lower() == "turkish")
# async def translate_to_turkish(message: types.Message):
#     await message.answer("Please enter the text you want to translate to Turkish:")
#
#     @dp.message_handler(lambda message: message.text)
#     async def translate_text_to_turkish(message: types.Message):
#         text_to_translate = message.text
#
#         try:
#             translation = translator.translate(text_to_translate, src='auto', dest="turkish")
#             translated_text = translation.text
#             await message.answer(f"Translated text to Turkish: {translated_text}")
#         except Exception as e:
#             await message.answer("An error occurred while translating. Please try again later.")
#
#
#
# # @dp.message_handler(lambda message: message.text.lower() in ["uzbek", "english", "russian", "turkish"])
# # async def handle_translation_request(message: types.Message):
# #     target_language = message.text.lower()
# #     text_to_translate = "Enter the text you want to translate."  # You should replace this with the actual user's message
# #
# #     try:
# #         if target_language == "uzbek":
# #             translation = translator.translate(text_to_translate, src='auto', dest="uzbek")
# #             translated_text = translation.text
# #             await message.answer(f"O'zbek tiliga tarjima: {translated_text}")
# #         elif target_language == "english":
# #             translation = translator.translate(text_to_translate, src='auto', dest="english")
# #             translated_text = translation.text
# #             await message.answer(f"Translated text to English: {translated_text}")
# #         elif target_language == "russian":
# #             translation = translator.translate(text_to_translate, src='auto', dest="russian")
# #             translated_text = translation.text
# #             await message.answer(f"Русский перевод: {translated_text}")
# #         elif target_language == "turkish":
# #             translation = translator.translate(text_to_translate, src='auto', dest="turkish")
# #             translated_text = translation.text
# #             await message.answer(f"Türkçe çeviri: {translated_text}")
# #     except Exception as e:
# #         await message.answer("An error occurred during translation. Please try again.")
#
#
#
#
# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)



import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from googletrans import Translator


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6357742300:AAFp8yUNJA1LTArfUBFdUKL6jWKFLxnyi5s"

P = "http://proxy.server:3128"

bot = Bot(token=BOT_TOKEN, proxy=P)
dp = Dispatcher(bot)

translator = Translator()

language_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
language_keyboard.add(types.KeyboardButton("Uzbek"))
language_keyboard.add(types.KeyboardButton("English"))
language_keyboard.add(types.KeyboardButton("Russian"))
language_keyboard.add(types.KeyboardButton("Turkish"))

translation_state = {}

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Choose a language to translate to:", reply_markup=language_keyboard)

@dp.message_handler(lambda message: message.text.lower() in ["uzbek", "english", "russian", "turkish"])
async def handle_language_choice(message: types.Message):
    user_id = message.from_user.id
    target_language = message.text.lower()
    translation_state[user_id] = {"target_language": target_language, "translating": False}

    await message.answer(f"You've selected {target_language.capitalize()}. Send me text to translate or press /cancel to stop.")

@dp.message_handler(lambda message: message.text.lower() == "/cancel")
async def handle_cancel(message: types.Message):
    user_id = message.from_user.id
    if user_id in translation_state:
        del translation_state[user_id]
    await message.answer("Translation canceled. Choose a language to translate to:", reply_markup=language_keyboard)

@dp.message_handler(lambda message: message.from_user.id in translation_state and translation_state[message.from_user.id]["translating"])
async def translate_text(message: types.Message):
    user_id = message.from_user.id
    state = translation_state[user_id]
    text_to_translate = message.text

    try:
        translation = translator.translate(text_to_translate, src='auto', dest=state["target_language"])
        translated_text = translation.text
        await message.answer(f"Translated text to {state['target_language'].capitalize()}: {translated_text}\n\n"
                             f"Send me another text or press /cancel to stop.")
    except Exception as e:
        await message.answer("An error occurred while translating. Please try again.")

@dp.message_handler(lambda message: message.text.lower() == "/start" and message.from_user.id in translation_state)
async def handle_start_over(message: types.Message):
    user_id = message.from_user.id
    del translation_state[user_id]
    await message.answer("Translation canceled. Choose a language to translate to:", reply_markup=language_keyboard)

@dp.message_handler(lambda message: message.from_user.id in translation_state and not translation_state[message.from_user.id]["translating"])
async def handle_text_input(message: types.Message):
    user_id = message.from_user.id
    translation_state[user_id]["translating"] = True
    await message.answer("Please enter the text you want to translate:")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)