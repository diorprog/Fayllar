import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton

BOT_TOKIN="6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4"

bot=Bot(BOT_TOKIN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
role= ["Mafia", "Tinch aholi", "Kamissar"]
user_data=[]

@dp.message_handler(commands="game")
async def register_user(msg: types.Message):
    inb=InlineKeyboardButton("qo'shilish",callback_data="add")
    ikm=InlineKeyboardButton()
    ikm.add(inb)

    await msg.answer("*Ro'yxatdan o'tish boshlandi*",parse_mode="Markdown")

@dp.message_handler(Text("add"))
async def add_users(callback: types.Message):
    user_data.append(callback.from_user.id)

    text = "Ro'yxatdan o'tganlar:  \n"