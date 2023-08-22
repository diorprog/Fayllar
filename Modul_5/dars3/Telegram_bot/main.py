# import logging
#
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup
#
# BOT_TOKEN = '6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4'
#
# bot = Bot(BOT_TOKEN)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)
#
#
# @dp.message_handler(commands="group")
# async def any_message(msg:types.Message):
#     print(msg)
#     await msg.answer(msg)
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
