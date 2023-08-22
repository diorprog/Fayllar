# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup
#
# BOT_TOKEN = '6540368592:AAGALM8DIFvV_CgInEblwyWyR80aCqT2O_Y'
#
# bot = Bot(BOT_TOKEN)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands='start')
# async def start_handler(message:types.Message):
#     design = [
#         [InlineKeyboardButton("UZ 🇺🇿"), InlineKeyboardButton("RU 🇷🇺")]
#     ]
#     markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
#     await message.answer("Tilni tanlang | Выберите язык", reply_markup=markup)
#
#
# @dp.message_handler(lambda message: message.text == 'UZ 🇺🇿')
# async def register(message: types.Message):
#     markup = ReplyKeyboardMarkup()
#     markup.add(KeyboardButton("Ro'yxatdan o'ting", request_contact=True, resize_keyboard=True))
#     await message.answer("Iltimos, ro'yxatdan o'ting ! ", reply_markup=markup)
#
#
# @dp.message_handler(lambda message: message.text == 'RU 🇷🇺')
# async def register(message: types.Message):
#     markupp = ReplyKeyboardMarkup()
#     markupp.add(KeyboardButton("Регистрацию", request_contact=True))
#     await message.answer("Пожалуйста, пройдите регистрацию", reply_markup=markupp)
#
#
# Menu_markup = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton("Menu")],
#         [KeyboardButton("Buyurtmalarim")],
#         [KeyboardButton("Fikr bildirish"), KeyboardButton("Sozlanmalar")],
#         [KeyboardButton("Admin")]
#     ],
#     resize_keyboard=True
# )
#
# @dp.message_handler(lambda message: message.text == "Buyurtmalarim")
# async def buyurtma_handler(message: types.Message):
#     await message.answer("Buyurtma mavjud emas!")
#
#
# @dp.message_handler(lambda message: message.text == "Menu")
# async def menu_handler(message: types.Message):
#     await message.answer("Xozir bot yangilanmoqda!")
#
#
# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
# async def start_handler(message: types.Message):
#     await message.answer(" Kerakli bo'limni tanlang ", reply_markup=Menu_markup)
#
# @dp.message_handler(lambda message: message.text == "Admin")
# async def admin_show(message: types.Message):
#     await message.bot.send_contact(message.from_user.id, '998943331161', 'Diyorbek')
#
#
# @dp.message_handler(lambda message: message.text == "Sozlanmalar")
# async def settings_show(message: types.Message):
#     await message.answer("Xozir bot yangilanmoqda!")
#
#
#
# @dp.message_handler(lambda message: message.text == "Fikr bildirish")
# async def fikr_show(message: types.Message):
#     await message.answer("Xozir bot yangilanmoqda!")
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
import sqlite3

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = '6540368592:AAGALM8DIFvV_CgInEblwyWyR80aCqT2O_Y'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

conn = sqlite3.connect('userdata.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username VARCHAR(255),
        registration_date TIMESTAMP
    )
''')

conn.commit()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    design = [
        [KeyboardButton("UZ 🇺🇿"), KeyboardButton("RU 🇷🇺")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    await message.answer("Tilni tanlang | Выберите язык", reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'UZ 🇺🇿')
async def register_uz(message: types.Message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("Ro'yxatdan o'ting", request_contact=True, resize_keyboard=True))
    await message.answer("Iltimos, ro'yxatdan o'ting!", reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'RU 🇷🇺')
async def register_ru(message: types.Message):
    markupp = ReplyKeyboardMarkup()
    markupp.add(KeyboardButton("Регистрацию", request_contact=True))
    await message.answer("Пожалуйста, пройдите регистрацию", reply_markup=markupp)

@dp.message_handler(lambda message: message.text == "Ro'yxatdan o'ting")
async def registration_completed(message: types.Message):
    await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")


@dp.message_handler(lambda message: message.text == "Регистрацию")
async def registration_completed_ru(message: types.Message):
    await message.answer("Вы успешно зарегистрировались!")


Menu_markup_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🥂Menu")],
        [KeyboardButton("🔰Buyurtmalarim")],
        [KeyboardButton("✅Fikr bildirish"), KeyboardButton("🔨Sozlanmalar")],
        [KeyboardButton("🤵Admin")]
    ],
    resize_keyboard=True
)

@dp.message_handler(lambda message: message.text == "🔰Buyurtmalarim")
async def buyurtma_handler_uz(message: types.Message):
    await message.answer("Buyurtma mavjud emas!")

@dp.message_handler(lambda message: message.text == "🥂Menu")
async def menu_handler_uz(message: types.Message):
    await message.answer("Xozir bot yangilanmoqda!", reply_markup=Menu_markup_uz)

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler_uz(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang", reply_markup=Menu_markup_uz)

@dp.message_handler(lambda message: message.text == "🤵Admin")
async def admin_show_uz(message: types.Message):
    await message.bot.send_contact(message.from_user.id, '998943331161', 'Diyorbek')

@dp.message_handler(lambda message: message.text == "🔨Sozlanmalar")
async def settings_show(message: types.Message):
    await message.answer("Xozir bot yangilanmoqda!")

@dp.message_handler(lambda message: message.text == "✅Fikr bildirish")
async def fikr_show_uz(message: types.Message):
    await message.answer("Xozir bot yangilanmoqda!")


Menu_markup_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🥂Меню")],
        [KeyboardButton("🔰Мои заказы")],
        [KeyboardButton("✅Комментарий"), KeyboardButton("🔨Настройки")],
        [KeyboardButton("🤵Администратор")]
    ],
    resize_keyboard=True
)

@dp.message_handler(lambda message: message.text == "🔰Мои заказы")
async def buyurtma_handler_ru(message: types.Message):
    await message.answer("Заказ недоступен!")

@dp.message_handler(lambda message: message.text == "🥂Меню")
async def menu_handler_ru(message: types.Message):
    await message.answer("В настоящее время бот обновляется!", reply_markup=Menu_markup_ru)

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler_ru(message: types.Message):
    await message.answer("Выберите нужный раздел", reply_markup=Menu_markup_ru)

@dp.message_handler(lambda message: message.text == "🤵Администратор")
async def admin_show_ru(message: types.Message):
    await message.bot.send_contact(message.from_user.id, '998943331161', 'Диорбек')

@dp.message_handler(lambda message: message.text == "🔨Настройки")
async def settings_show_ru(message: types.Message):
    await message.answer("В настоящее время бот обновляется!")

@dp.message_handler(lambda message: message.text == "✅Комментарий")
async def fikr_show_ru(message: types.Message):
    await message.answer("В настоящее время бот обновляется!")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def register(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    registration_date = message.date

    cursor.execute('INSERT INTO users (user_id, username, registration_date) VALUES (?, ?, ?)',
                   (user_id, username, registration_date))
    conn.commit()

    await message.answer("🤝")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



#
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
# BOT_TOKEN = '6540368592:AAGALM8DIFvV_CgInEblwyWyR80aCqT2O_Y'
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
#
#
# uzbek_button = KeyboardButton("UZ 🇺🇿")
# russian_button = KeyboardButton("RU 🇷🇺")
#
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     design = [
#         [uzbek_button, russian_button]
#     ]
#     markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
#     await message.answer("Tilni tanlang | Выберите язык", reply_markup=markup)
#
# @dp.message_handler(lambda message: message.text == 'UZ 🇺🇿')
# async def register_uz(message: types.Message):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("Ro'yxatdan o'ting", request_contact=True))
#     await message.answer("Iltimos, ro'yxatdan o'ting!", reply_markup=markup)
#
# @dp.message_handler(lambda message: message.text == 'RU 🇷🇺')
# async def register_ru(message: types.Message):
#     markupp = ReplyKeyboardMarkup(resize_keyboard=True)
#     markupp.add(KeyboardButton("Регистрацию", request_contact=True))
#     await message.answer("Пожалуйста, пройдите регистрацию", reply_markup=markupp)
#
# @dp.message_handler(lambda message: message.text == "🥂Menu")
# async def menu_handler(message: types.Message):
#     await message.answer("Xozir bot yangilanmoqda!", reply_markup=uz_menu_markup)
#
# @dp.message_handler(lambda message: message.text == "🥂Меню")
# async def menu_handler_ru(message: types.Message):
#     await message.answer("В настоящее время бот обновляется!", reply_markup=ru_menu_markup)
#
#
# uz_menu_markup = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton("🥂Menu"), KeyboardButton("🔰Buyurtmalarim")],
#         [KeyboardButton("✅Fikr bildirish"), KeyboardButton("🔨Sozlanmalar")],
#         [KeyboardButton("🤵Admin")]
#     ],
#     resize_keyboard=True
# )
#
# ru_menu_markup = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton("🥂Меню"), KeyboardButton("🔰Мои заказы")],
#         [KeyboardButton("✅Комментарий"), KeyboardButton("🔨Настройки")],
#         [KeyboardButton("🤵Администратор")]
#     ],
#     resize_keyboard=True
# )
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
