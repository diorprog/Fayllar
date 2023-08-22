# dior_prog bot BOTFATHER dan hosil qilingan
from aiogram import Bot, Dispatcher, types, executor

BOT_TOKEN = '6139228289:AAH0paU3MwqVpjupf7-ZVcFVObi9s7I2hS4'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    # print(message)        #start bosganda print qiladi
    text = f"Hi {message.from_user.first_name}! Welcome to dior_prog bot"
    await message.answer(text)


@dp.message_handler(commands="info")
async def echo_handler(message: types.Message):  # get_me ishlatilishi
    bot_info = await bot.get_me()
    await message.answer(str(bot_info))


@dp.message_handler(commands="answer")
async def echo_handler(message: types.Message):
    await message.answer("This is answer method !")


@dp.message_handler(commands="reply")
async def echo_handler(message: types.Message):
    await message.reply("This is reply method !")


@dp.message_handler(commands="send_message")
async def echo_handler(message: types.Message):
    await message.bot.send_message(message.from_user.id,
                                   message.txt)  # message.from_user.id  o'rnida kimnidir t.me id si kiritilsa xabar shu id egasiga boradi


@dp.message_handler(commands="send_photo")
async def echo_handler(message: types.Message):
    # await message.bot.send_photo(message.chat.id, open("bmw_.jpg",'rb'))               #computerda bor rasmni chaqirish
    await message.bot.send_photo(message.chat.id,
                                 "https://img5.goodfon.ru/wallpaper/nbig/6/1b/bmw-2019-manhart-mh5-800-m5-f90-sedan-vid-speredi-v8-biturbo.jpg",
                                 caption="BMW")


@dp.message_handler(commands="send_video")
async def echo_handler(message: types.Message):
    await message.bot.send_video(message.chat.id, "https://t.me/PRIKOLLAR_LATIFALAR_KULGU_HAZILL/3549")


@dp.message_handler(commands="send_phone")
async def echo_handler(message: types.Message):
    await message.bot.send_contact(message.chat.id, "998943331161", "Diyorbek", "Dilmurodov")


@dp.message_handler(commands="send_location")
async def echo_handler(message: types.Message):
    await message.bot.send_location(message.chat.id, 34.5, 45.9)


@dp.message_handler()
async def echo_handler(
        message: types.Message):  # comanda dan tashqari yozilgan har bir so'zni qaytarib chiqarib javob beradi comandalar xirida yozlishi kk
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
