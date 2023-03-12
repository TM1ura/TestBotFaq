from aiogram import types, Dispatcher
from tgBot.keyboard import inline_kb_form, inline_kb_help, inline_kb_exam
from tgBot.states import ExamState

# Обработка кнопок
async def faq(message: types.Message):
    await message.answer(
        text='Просто напишите мне ваш вопрос и я постараюсь найти на него ответ или задайте его напрямую приемной комиссии по форме',
        reply_markup=inline_kb_form)

async def help(message: types.Message):
    await message.answer(text='Выберите интересующую вас тему',
                         reply_markup=inline_kb_help)

async def career_orient_test(message: types.Message):
    await message.answer(text='Тест на профориентацию в разработке')

async def calculator_ege(message: types.Message):
    await message.answer(text='Укажите ваши баллы за экзамен по русскому языку (только число, например: 40) ')
    await ExamState.pre_exam.set()

def register_buttons(dispatcher:Dispatcher):
    dispatcher.register_message_handler(callback=faq,
                                        is_faq=True)
    dispatcher.register_message_handler(callback=help,
                                        is_help=True)
    dispatcher.register_message_handler(callback=career_orient_test,
                                        is_test=True)
    dispatcher.register_message_handler(callback=calculator_ege,
                                        is_calculator=True)