from aiogram import types, Dispatcher
from tgBot.services.message_analys import analys_question

# Обработка вопроса
async def question(message: types.Message):
    analysResult = analys_question(text=message.text)

    await message.answer(text=analysResult[0],
                         reply_markup=analysResult[1])

def register_question(dispatcher:Dispatcher):
    dispatcher.register_message_handler(question)