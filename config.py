from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token="token yoziladi"

bot=Bot(token)
dp=Dispatcher(bot,storage=MemoryStorage())