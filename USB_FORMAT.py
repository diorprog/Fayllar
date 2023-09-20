# """
#
# from sqlalchemy import create_engine, Column, BigInteger, String
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base
# Base = declarative_base()
#
# DATABASE_URL = "postgresql+psycopg2://postgres:1@pg/postgres"
# engine = create_engine(DATABASE_URL)
#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(BigInteger, primary_key=True, index=True)
#     user_id = Column(BigInteger, unique=True, index=True)
#     username = Column(String, unique=True, index=True, nullable=True)
#     first_name = Column(String)
#
# Base.metadata.create_all(bind=engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# #models.py
#
# from aiogram import Bot, Dispatcher, types
# from sqlalchemy.exc import IntegrityError
#
# from buttonss import markup, menugym, oygym, haftagym
# from models import User, SessionLocal
#
# BOT_TOKEN = "5906643439:AAFw0F_utBFNVV_oGPECsz19VXmJ6QJPbzA"
#
# bot = Bot(BOT_TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(lambda message: message.text == "back 🔙")
# @dp.message_handler(commands=["start"])
# async def start(message: types.Message):
# # Botdan kelgan foydalanuvchi ma'lumotlarini olish
#     user_id = message.from_user.id
#     username = message.from_user.username
#     first_name = message.from_user.first_name
#
#     # Ma'lumotlarni ma'lumotlar bazasiga saqlash
#     db = SessionLocal()
#     try:
#         db_user = User(user_id=user_id, username=username, first_name=first_name)
#         db.add(db_user)
#         db.commit()
#     except IntegrityError as e:
#         # Handle the case where the username already exists
#         db.rollback()
#         existing_user = db.query(User).filter(User.username == username).first()
#         if existing_user:
#             existing_user.user_id = user_id
#             existing_user.first_name = first_name
#             db.commit()
#             await message.reply("Sizning ma'lumotlaringiz yangilandi!")
#         else:
#             # Handle other IntegrityError cases if necessary
#             await message.reply("Ma'lumotlarni saqlashda xatolik yuz berdi!")
#
#     db.close()
#     if message.text != "back 🔙":
#
#         text = """Assalomu alaykum !
# Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi"""
#         await message.bot.send_photo(message.from_user.id, "https://assets.turbologo.ru/blog/ru/2020/11/18161626/fitness-2.png", caption=text, parse_mode="Markdown" ,  reply_markup=markup)
#     else: await message.answer("Kerakli menyuni tanlang ",reply_markup=markup)
#
#
#
# @dp.message_handler(lambda message: message.text == "Admin 👨‍🚀")
# async def admin_handler(message: types.Message):
#
#     await message.reply(f"Admin bilan aloqa 📱 "
#                         f"https://t.me/secdeee1" ,reply_markup=markup)
#
# @dp.message_handler(lambda message: message.text == "📍 Filial")
# async def filial_hendler(message: types.Message):
#     latitude = 41.313605
#     longitude = 69.279691
#     await message.bot.send_location(message.chat.id, latitude, longitude,  reply_markup=markup)
#
#
#
# @dp.message_handler(lambda message: message.text == "Back 🔙")
# @dp.message_handler(lambda message: message.text  == "Start 🏋️‍♂️")
# async def gym_start_hendler(message: types.Message):
#     await message.answer("Jinsingizni Tanlang ⤵️", reply_markup=menugym)
#
#
#
# @dp.message_handler(lambda message: message.text == "Man 🤵‍♂️")
# async def start_hendler(message: types.Message):
#     await message.answer("Kerakli oyni tanlang ⬇️", reply_markup=oygym)
#
#
# @dp.message_handler(lambda message: message.text == "Woman 👩‍🦰")
# async def start_hendler(message: types.Message):
#     await message.answer("Kerakli oyni tanlang ⬇️", reply_markup=oygym)
#
# @dp.message_handler(lambda message: message.text in ["1-OY", "2-OY", "3-OY", "4-OY"])
# async def hafta_hend(message: types.Message):
#     await message.answer("Kunni tanlang  ⤵️", reply_markup=haftagym)
#
#
# if __name__ == "__main__":
#     from aiogram import executor
#     from models import Base, engine
#     Base.metadata.create_all(bind=engine)
#     executor.start_polling(dp, skip_updates=True)
#
# .., [08/09/23 09:24]
# main.py
#
# .., [08/09/23 09:24]
# from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
#
# markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# markup.add(KeyboardButton("📍 Filial"), KeyboardButton("Start 🏋️‍♂️"))
# markup.add(KeyboardButton("Admin 👨‍🚀"))
#
#
# menugym = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# menugym.add(KeyboardButton("Woman 👩‍🦰"), KeyboardButton("Man 🤵‍♂️"))
# menugym.add(KeyboardButton("back 🔙"))
#
#
# oygym = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# oygym.add(KeyboardButton("1-OY"), KeyboardButton("2-OY"))
# oygym.add(KeyboardButton("3-OY"), KeyboardButton("4-OY"))
# oygym.add(KeyboardButton("Back 🔙"))
#
#
# haftagym = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# haftagym.add(KeyboardButton("Dushanba"), KeyboardButton("Seshanba"), KeyboardButton("Chorshanba"))
# haftagym.add(KeyboardButton("Payshanba"), KeyboardButton("Juma"),KeyboardButton("Shanba"))
# haftagym.add(KeyboardButton("Back 🔙"))
#
# .., [08/09/23 09:24]
# buttinss.py
#
# """