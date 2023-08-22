from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

BOT_TOKEN = "6037688459:AAGKrCRtY4EYkIm8oVNWgjofD0-fkh2-ri0"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    d = [
        [InlineKeyboardButton("UZ 🇺🇿"), InlineKeyboardButton("RU 🇷🇺")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=d, resize_keyboard=True)

    await message.answer("Tilni tanlang | Выберите язык", reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'UZ 🇺🇿')
async def register(message: types.Message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("Ro'yxatdan o'ting", request_contact=True))
    await message.answer("Iltimos, ro'yxatdan o'ting ! ", reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'RU 🇷🇺')
async def register(message: types.Message):
    markupp = ReplyKeyboardMarkup()
    markupp.add(KeyboardButton("Регистрацию", request_contact=True))
    await message.answer("Пожалуйста, пройдите регистрацию", reply_markup=markupp)


Menu_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🍽 Menu")],
        [KeyboardButton("🛍 Mening buyurtmalarim")],
        [KeyboardButton("✍️Fikr bildirish"), KeyboardButton("⚙️ Settings")],
        [KeyboardButton("Admin")]
    ],
    resize_keyboard=True
)


@dp.message_handler(lambda message: message.text == "🛍 Mening buyurtmalarim")
async def buyurtma_handler(message: types.Message):
    await message.answer("Sizda buyurtmalar mavjud emas ")


@dp.message_handler(lambda message: message.text == "🍽 Menu")
async def menu_handler(message: types.Message):
    await message.answer("Xozirda test jarayonida !! ")


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def start_handler(message: types.Message):
    await message.answer(" Kerakli bo'limni tanlang ", reply_markup=Menu_markup)


# Menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton("🗺 fast food location ")],
#         [KeyboardButton("📍 Geolokatsiya", request_location=True), KeyboardButton("🔙 Ortga")]
#
#     ]
# )
#
#
# @dp.message_handler(lambda message: message.text == "📍 Geolokatsiya")
# async def geolokat_handler(message: types.Message):
#     await message.answer()
# @dp.message_handler(lambda message: message.text == "🔙 Ortga")
# async def back_handler(message: types.Message):
#     await message.answer("Tugmani tanlang !", reply_markup=Menu_markup)


@dp.message_handler(lambda message: message.text == "Admin")
async def admin_show(message: types.Message):
    await message.bot.send_contact(message.from_user.id, '998881582225', 'Dilshodbek')


@dp.message_handler(lambda message: message.text == "⚙️ Settings")
async def settings_show(message: types.Message):
    await message.answer("Xozirda test jarayonida !!")



@dp.message_handler(lambda message: message.text == "✍️Fikr bildirish")
async def fikr_show(message: types.Message):
    await message.answer("Xozirda test jarayonida !!")



#
#
# Menu_markup1= ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton("🍽 Menu")],
#         [KeyboardButton("🛍 Mening buyurtmalarim")],
#         [KeyboardButton("✍️Fikr bildirish"), KeyboardButton(" Sozlamalar")],
#         [KeyboardButton("Admin")]
#     ],
#     resize_keyboard=True
# )
#
#
# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
# async def start_handler(message: types.Message):
#     await message.answer(" Kerakli bo'limni tanlang ", reply_markup=Menu_markup1)
#
#
# Menu1 = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton("🗺 fast food location ")],
#         [KeyboardButton("📍 Geolokatsiya", request_location=True), KeyboardButton("🔙 Ortga")]
#
#     ]
# )
#
#
# @dp.message_handler(lambda message: message.text == "🍽 Menu")
# async def menu_handler(message: types.Message):
#     await message.answer("Menu ", reply_markup=Menu1)
#
#
# @dp.message_handler(lambda message: message.text == "📍 Geolokatsiya")
# async def geolokat_handler(message: types.Message):
#     await message.answer()
#
#
# @dp.message_handler(lambda message: message.text == "Admin")
# async def admin_show(message: types.Message):
#     await message.bot.send_contact(message.from_user.id, '998881582225', 'Dilshodbek')
#
#
# @dp.message_handler(lambda message: message.text == "🔙 Ortga")
# async def back_handler(message: types.Message):
#     await message.answer("Tugmani tanlang !", reply_markup=Menu_markup1)
#
#
# @dp.message_handler(lambda message: message.text == "⚙️ Sozlamalar")
# async def settings_show(message: types.Message):
#     await message.bot.send_message(message.from_user.id, f"{message.from_user}")
#
#
# @dp.message_handler(lambda message: message.text == "🛍 Mening buyurtmalarim")
# async def buyurtma_handler(message: types.Message):
#     await message.answer("Sizda buyurtmalar mavjud emas ")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)