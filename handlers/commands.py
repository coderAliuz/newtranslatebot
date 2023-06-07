from aiogram.types import Message
from config import dp 
from keyboards import main_kb

@dp.message_handler(commands="start",state="*")
async def start(message:Message):
    await message.answer(f"Assalom aleykum {message.chat.full_name}\nBu tarjimon bot.\nKerakli tugamani bosing.",reply_markup=main_kb) 

@dp.message_handler(text="Bot haqida")
async def about(message:Message):
    await message.reply("Ushbu istalgan tildan belgilangan tilga so'zlarni tarjima qilib beradi.\nBotdan foydalanish uchun\n1.Tarjimon tugmasi bosiladi.\n2.Til tanlanadi.\n3.So'z yuboriladi.")

@dp.message_handler(commands="help",state="*")
async def help(message:Message):
    await message.answer("Savol yoki shikoyat bo'lsa\nAdmin @coder_ali bog'laning!!!")



