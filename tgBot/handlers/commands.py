from aiogram import types, Dispatcher
from tgBot.keyboard.reply import kb

# Обработка команды Старт
async def welcome(message: types.Message):
    await message.answer(text='Приветствую, я чат-бот.\n Я могу проконсультировать вас по вопросам поступления в "МАГУ"',
                         reply_markup=kb)
    await message.bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp(text='Абитуриенту',
                                                                            web_app=types.WebAppInfo(url='https://www.masu.edu.ru/abit/')))

# Регистрация хендлера комманды
def register_commands(dispatcher:Dispatcher):
    dispatcher.register_message_handler(callback=welcome,
                                        commands=['start'])