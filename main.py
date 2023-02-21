import logging
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
from Keyboard import kb, inlineKbHelp, inlineKbForm
from messageAnalys import analys_question

bot = Bot(TOKEN, parse_mode='HTML')

dp = Dispatcher(bot)
logger = logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Приветствую, я чат-бот', reply_markup=kb)
    await bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp('Абитуриенту', web_app=types.WebAppInfo(url='https://www.masu.edu.ru/abit/')))

@dp.message_handler(text=['FAQ'])
async def faq(message: types.Message):
    await message.answer('Просто напишите мне ваш вопрос и я постараюсь найти на него ответ или задайте его вопрос приемной комиссии по форме', reply_markup=inlineKbForm)


@dp.message_handler(text=['Полезная информация'])
async def help(message: types.Message):
    await message.answer('Выберите интересующую вас тему', reply_markup=inlineKbHelp)

@dp.message_handler(text=['Тест на профориентацию'])
async def help(message: types.Message):
    await message.answer('Тест на профориентацию в разработке')

@dp.message_handler()
async def message(message: types.Message):
    answer = analys_question(message.text)
    await message.answer(f'{answer}. \n Если я не отыетил на ваш вопрос, вы можете задать вопрос приемной комиссии по форме', reply_markup=inlineKbForm)


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=False)
    except ConnectionError as conErorr:
        print('Connection error:', conErorr)
    except Exception as erorr:
        print('Error:', erorr)