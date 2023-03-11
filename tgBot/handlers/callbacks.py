from aiogram import types, Dispatcher
from tgBot.services.messageAnalys import analys_question
from tgBot.keyboard.inline import inlineKbForm, inlineKbDeclaration, inlineKbConsert
from tgBot.services.db import fetchEGE

exams = []

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
                                reply_markup=inlineKbForm)

# Заявление/Согласие на зачисление
async def declaration(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(text='Выберите уровень образования',
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=inlineKbDeclaration)

async def consert(callback_query: types.CallbackQuery):
    await callback_query.bot.edit_message_text(text='Выберите уровень образования',
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=inlineKbConsert)

# Калькулятор ЕГЭ
async def exam(callback_query: types.CallbackQuery):
    if len(exams) == 0:
        exams.append(callback_query.data.split(":")[1])

    elif len(exams) == 1:
        exams.append(callback_query.data.split(":")[1])
        await callback_query.message.delete()

        study_prog = await fetchEGE(ege1=exams[0],
                             ege2=exams[1])

        await callback_query.bot.send_message(chat_id=callback_query.message.chat.id,
                                text=study_prog)

        exams.clear()

def register_callbacks(dispatcher:Dispatcher):
    dispatcher.register_callback_query_handler(callback=yes,
                                               data_yn='is_yes')
    dispatcher.register_callback_query_handler(callback=no,
                                               data_yn='is_no')
    dispatcher.register_callback_query_handler(callback=declaration,
                                               data_declaration=True)
    dispatcher.register_callback_query_handler(callback=consert,
                                               data_consert=True)
    dispatcher.register_callback_query_handler(callback=exam,
                                               data_exam=True)