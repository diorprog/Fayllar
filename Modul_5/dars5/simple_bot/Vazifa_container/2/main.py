from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

BOT_TOKEN = "6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cats(message:types.Message):
    await message.answer("Welcome to bot")






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)