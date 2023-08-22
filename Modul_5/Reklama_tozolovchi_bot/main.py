# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.types import ChatPermissions
# import re
#
# BOT_TOKEN = "6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# def remove_arabic(text):
#     arabic_pattern = re.compile("[\u0600-\u06FF]+")
#     return arabic_pattern.sub("", text)

# def remove_links(text):
#     link_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
#     return link_pattern.sub("", text)

# @dp.message_handler()
# async def check_ad(message: types.Message):
#     if message.chat.type == types.ChatType.GROUP or message.chat.type == types.ChatType.SUPERGROUP:
#         if "t.me" in message.text:
#             await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
#             await message.answer(f"Itimos {message.from_user.full_name} reklama tarqatmang!")
#             return
#
#         cleaned_text = remove_arabic(message.text)
#         cleaned_text = remove_links(cleaned_text)
#
#         if len(cleaned_text) < len(message.text):
#             await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
#             return
#
# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)


import logging
from datetime import timedelta
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ChatPermissions
import re

BOT_TOKEN = "6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
datas = ["yaramas" , "jinursin" , "block" , "axmoq"]


def remove_arabic(text):
    arabic_pattern = re.compile("[\u0600-\u06FF]+")
    return arabic_pattern.sub("", text)


def remove_links(text):
    link_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    return link_pattern.sub("", text)


@dp.message_handler()
async def check_ad(message: types.Message):
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPERGROUP]:
        if "t.me" in message.text:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await message.answer(f"Itimos {message.from_user.full_name} reklama tarqatmang!")
            return
        # if "t.me" in message.text1:
        #     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        #     await message.answer(f"Itimos {message.from_user.full_name} arab tilida kiritmang!")
        #     return
        for word in datas:
            if word in message.text.lower():
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                await message.answer(f"Iltimos, haqoratli so'zlar ishlatmang! {message.from_user.first_name}")
                await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id, permissions=ChatPermissions(can_send_messages=False),until_date=timedelta(seconds=10))
                return


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)

