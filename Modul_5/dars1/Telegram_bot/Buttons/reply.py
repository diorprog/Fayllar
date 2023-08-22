from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

BOT_TOKEN = '6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_handler(message:types.Message):
    text=f"Hi {message.from_user.first_name}! Welcome to dior_prog bot"
    await message.answer(text)


@dp.message_handler(commands='reply_button')
async def start_handler(message:types.Message):
    design = [
        ["Button1","Button2","Button3"],
        ["Button4","Button5","Button6"]
    ]
    markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    await message.answer("Reply button show",reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)