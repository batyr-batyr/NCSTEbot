from aiogram import Bot,Dispatcher, executor, types
from config import BOT_TOKEN
import menu as nav

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,'Здраствуйте! \nДобро пожаловать в телеграм бот АО "НЦГНТЭ".'.format(message.from_user), reply_markup = nav.mainMenu)

    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates= True)