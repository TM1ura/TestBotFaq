from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from tgBot.services import analys_question
from tgBot.keyboard import inline_kb_form, inline_kb_declaration, inline_kb_consert, inline_kb_help
from tgBot.states import ExamState

# Обработка Callback'ов от inline-кнопок
async def yes(callback_query: types.CallbackQuery):
    analysResult = analys_question(callback_query.message.text.split(':')[1])

    await callback_query.bot.edit_message_text(text=analysResult[0].split('\n')[0],
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=None)

async def no(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(text='К сожалению, я не знаю ответа на ваш вопрос, но вы можете задать свой вопрос напрямую приемной комиссии, по форме:',
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=inline_kb_form)

# Заявление/Согласие на зачисление
async def declaration(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(text='Выберите уровень образования',
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=inline_kb_declaration)

async def consert(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(text='Выберите уровень образования',
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=inline_kb_consert)

async def back_to_help(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(text='Выберите интересующую вас тему',
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=inline_kb_help)

# Калькулятор ЕГЭ
async def exam1(callback_query: types.CallbackQuery, state:FSMContext):
    await callback_query.message.answer('Укажите баллы за первый экзамен по выбору')
    await state.update_data(exam1=callback_query.data.split(":")[1])
    await ExamState.exam1.set()
    await callback_query.message.delete()

async def exam2(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer('Укажите баллы за второй экзамен по выбору')
    await state.update_data(exam2=callback_query.data.split(":")[1])
    await callback_query.message.delete()
    await ExamState.exam2.set()

def register_callbacks(dispatcher:Dispatcher):
    dispatcher.register_callback_query_handler(callback=yes,
                                               data_yes=True)
    dispatcher.register_callback_query_handler(callback=no,
                                               data_no=True)
    dispatcher.register_callback_query_handler(callback=declaration,
                                               data_declaration=True)
    dispatcher.register_callback_query_handler(callback=consert,
                                               data_consert=True)
    dispatcher.register_callback_query_handler(callback=back_to_help,
                                               data_to_help=True)
    dispatcher.register_callback_query_handler(callback=exam2,
                                               data_exam=True,
                                               state=ExamState.exam1)
    dispatcher.register_callback_query_handler(callback=exam1,
                                               data_exam=True,
                                               state=ExamState.pre_exam)
