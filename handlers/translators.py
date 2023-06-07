from aiogram.types import Message
from config import dp 
from keyboards import lang_kb,main_kb,back_kb
from aiogram.dispatcher import FSMContext
from googletrans import Translator
from krill_latin.krill_latin import to_cyrillic,to_latin

@dp.message_handler(text="Tarjimon")
async def tarjimon(message:Message,state:FSMContext):
    await message.answer("Kerakli tilni tanlang.\n Yuborilgan so'zlar ushbu tilga tarjima qilinadi",reply_markup=lang_kb)
    await state.set_state("main")

@dp.message_handler(state="main")
async def til(message:Message,state:FSMContext):
    text=message.text
    if text=="UZ":
        await message.answer("Istalgan so'z yuboring O'zbekchaga tarjima qilaman",reply_markup=back_kb)
        await state.set_state("translator")
        await state.update_data(til="uz")
    elif text=="RU":
        await message.answer("Istalgan so'z yuboring Ruscha tarjima qilaman",reply_markup=back_kb)
        await state.set_state("translator")
        await state.update_data(til="ru")
    elif text=="ENG":
        await message.answer("Istalgan so'z yuboring Inglizcha tarjima qilaman",reply_markup=back_kb)
        await state.set_state("translator")
        await state.update_data(til="en")
    elif text=="LATIN":
        await message.answer("KRILLcha so'z yuboring LATINchaga o'tqazaman",reply_markup=back_kb)
        await state.set_state("latin-krill")
        await state.update_data(til="latin")
    elif text=="KRILL":
        await message.answer("LATINcha so'z yuboring KRILLchaga o'tqazaman",reply_markup=back_kb)
        await state.set_state("latin-krill")
        await state.update_data(til="krill")  
    elif text=="Ortga":
        await message.answer("Kerakli tugmani bosing",reply_markup=main_kb)
        await state.finish()
    else:
        await message.answer("Kerakli tilni tanlang.")

@dp.message_handler(text="Ortga",state=["translator","latin-krill"])
async def back(message:Message,state:FSMContext):
    await message.answer("Kerakli tilni tanlang.",reply_markup=lang_kb)
    await state.set_state("main")

@dp.message_handler(state="translator")
async def tarjima(message:Message,state:FSMContext):
    matn=message.text
    data=await state.get_data()
    til=data['til']
    t=Translator()
    tarjima_text=t.translate(text=matn,dest=til).text
    await message.reply(tarjima_text)
    
@dp.message_handler(state="latin-krill")
async def tarjima2(message:Message,state:FSMContext):
    matn=message.text
    data=await state.get_data()
    til=data['til']
    if til=="latin":
        tarjim_text=to_latin(matn)
    else:
        tarjim_text=to_cyrillic(matn)
    await message.reply(tarjim_text)