from typing import Text

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Filter
from aiogram.types import ReplyKeyboardMarkup, message

BOT_TOKEN = '6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


class MyFilter(Filter):
    def __init__(self,message_text):
        self.message_text=message_text

    async def check(self, *args) -> bool:
        pass

    def __invert__(self):
        return super().__invert__()

    def __and__(self, other):
        return super().__and__(other)

    def __or__(self, other):
        return super().__or__(other)

    async def __call__(self, message):
        return self.message_text == message.text



@dp.message_handler(commands='start')
async def start_handler(message:types.Message):
    text=f"Hi {message.from_user.first_name}! Welcome to *dior_prog bot*"
    await message.answer(text,parse_mode="Markdown")


@dp.message_handler(commands=["lang", "language"])
async def language_handler(massage: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🏴󠁧󠁢󠁥󠁮󠁧󠁿ENG", "🇺🇿UZB")
    await message.answer("Choice language", reply_markup=markup)

    # 1-usul


# @dp.message_handler(lambda msg: msg.text in ("🏴󠁧󠁢󠁥󠁮󠁧󠁿ENG" , "🇺🇿UZB"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿UZB":
#         await message.answer("Assalomu alaykum !")
#     else:
#         await message.answer("Hello !")

# 2-usul
# @dp.message_handler(Text("🇺🇿UZB"))
# @dp.message_handler(Text("🏴󠁧󠁢󠁥󠁮󠁧󠁿ENG"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿UZB":
#         await message.answer("Assalomu alaykum !")
#     else:
#         await message.answer("Hello !")



# @dp.message_handler(MyFilter("🇺🇿UZB"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿UZB":                                         #MyFilter funksiyasi bn ishlashi 2-usulni
#         await message.answer("Assalomu alaykum !")
#     else:
#         await message.answer("Hello !")


    # 3-usul


# @dp.message_handler(lambda msg: msg.text.startswith("🇺🇿U") or msg.text.startswith("🏴󠁧󠁢󠁥󠁮󠁧󠁿E"))
# async def choice_handler(message: types.Message):
#     if message.text == "🇺🇿UZB":
#         await message.answer("Assalomu alaykum !")
#     else:
#         await message.answer("Hello !")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
