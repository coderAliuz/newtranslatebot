from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove

main_kb=ReplyKeyboardMarkup(
    [
        ["Tarjimon","Bot haqida"]
    ],resize_keyboard=True
)

lang_kb=ReplyKeyboardMarkup(
    [
        ["UZ","RU","ENG"],
        ["LATIN","KRILL"],
        ["Ortga"]
    ],resize_keyboard=True
)

back_kb=ReplyKeyboardMarkup(
    [
        ["Ortga"]
    ],resize_keyboard=True
)