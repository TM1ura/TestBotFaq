from aiogram import types, Dispatcher
from tgBot.keyboard.inline import inlineKbForm, inlineKbHelp, inlineKbExam

# Обработка кнопок
async def faq(message: types.Message):
    await message.answer(
        text='Просто напишите мне ваш вопрос и я постараюсь найти на него ответ или задайте его напрямую приемной комиссии по форме',
        reply_markup=inlineKbForm)

async def help(message: types.Message):
    await message.answer(text='Выберите интересующую вас тему',
                         reply_markup=inlineKbHelp)

async def career_orient_test(message: types.Message):
    await message.answer(text='Тест на профориентацию в разработке')

async def calculator_ege(message: types.Message):
    await message.answer(text='Какие экзамены вы сдавали/будете сдавать',
                         reply_markup=inlineKbExam)

def register_buttons(dispatcher:Dispatcher):
    dispatcher.register_message_handler(callback=faq,
                                        is_faq=True)
    dispatcher.register_message_handler(callback=help,
                                        is_help=True)
    dispatcher.register_message_handler(callback=career_orient_test,
                                        is_test=True)
    dispatcher.register_message_handler(callback=calculator_ege,
                                        is_calculator=True)