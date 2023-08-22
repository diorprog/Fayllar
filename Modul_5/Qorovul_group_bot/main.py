
import logging
from datetime import timedelta

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ChatPermissions

BOT_TOKEN = "6196916793:AAFGXe2f9ZlqULVxAXY7pGniaCFeGyQ2j6E"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
datas = ["yaramas" , "jinursin" , "block" , "axmoq"]
block = []

@dp.message_handler(lambda msg : msg.from_user.id in block)
async def delete_msg(message : types.Message):
    await message.delete()

@dp.message_handler()
async def any_message(msg: types.Message):
    for i in msg.text.split():
        if i in datas:
            await msg.delete()
            await msg.answer(f"Iltimos haqoratli so'z ishlatilmasin ! {msg.from_user.first_name}")
            await bot.ban_chat_member(msg.chat.id, msg.from_user.id,ChatPermissions(can_change_info = False), until_date=timedelta(seconds=10))
            # block.append(msg.from_user.id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)