from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


BOT_TOKEN = '6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_handler(message:types.Message):
    text=f"Hi {message.from_user.first_name}! Welcome to dior_prog bot"
    await message.answer(text)


@dp.message_handler(commands='inline_button')
async def start_handler(message:types.Message):
    design = [
        [InlineKeyboardButton("Button1",callback_data="btn1"), InlineKeyboardButton("Button2",callback_data="btn2")],
        [InlineKeyboardButton("Button3",callback_data="btn2")]
    ]

    ikm=InlineKeyboardMarkup(inline_keyboard=design)
    await  message.answer("Inline keyboard show",reply_markup=ikm)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)