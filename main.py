import logging
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
from Keyboard import kb, inlineKbHelp, inlineKbForm, inlineKb, inlineKbDeclaration, inlineKbConsert, inlineKbEge1, inlineKbEge2
from messageAnalys import analys_question
from db import fetchEGE

bot = Bot(TOKEN, parse_mode='HTML')

dp = Dispatcher(bot)
logger = logging.basicConfig(level=logging.INFO)

egeList = []

# Обработка команды Старт
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Приветствую, я чат-бот.\n Я могу проконсультировать вас по вопросам поступления в "МАГУ"', reply_markup=kb)
    await bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp('Абитуриенту', web_app=types.WebAppInfo(url='https://www.masu.edu.ru/abit/')))

# Обработка кнопок
@dp.message_handler(text=['FAQ'])
async def faq(message: types.Message):
    await message.answer('Просто напишите мне ваш вопрос и я постараюсь найти на него ответ или задайте его напрямую приемной комиссии по форме', reply_markup=inlineKbForm)


@dp.message_handler(text=['Полезная информация'])
async def help(message: types.Message):
    await message.answer('Выберите интересующую вас тему', reply_markup=inlineKbHelp)

@dp.message_handler(text=['Тест на профориентацию'])
async def help(message: types.Message):
    await message.answer('Тест на профориентацию в разработке')

@dp.message_handler(text=['Калькулятор ЕГЭ'])
async def EGE(message: types.Message):
    await message.answer('Какие экзамены вы сдавали/будете сдавать', reply_markup=inlineKbEge1)

# Обработка Callback'ов от inline-кнопок
@dp.callback_query_handler(lambda c: c.data)
async def callbackYes(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Загрузка")

    if callback_query.data == 'Yes':
        await bot.send_message(callback_query.message.chat.id, 'Спасибо за вопрос')

    elif callback_query.data == 'No':
        await bot.edit_message_text('К сожалению, я не знаю ответа на ваш вопрос, но вы можете задать свой вопрос напрямую приемной комиссии, по форме:', callback_query.message.chat.id, callback_query.message.message_id, reply_markup=inlineKbForm)

    # Заявление/Согласие на зачисление
    elif callback_query.data == 'Declaration':
        await bot.edit_message_text('Выберите уровень образования', callback_query.message.chat.id, callback_query.message.message_id, reply_markup=inlineKbDeclaration)

    elif callback_query.data == 'Consert':
        await bot.edit_message_text('Выберите уровень образования', callback_query.message.chat.id, callback_query.message.message_id, reply_markup=inlineKbConsert)

    # Калькулятор ЕГЭ
    elif callback_query.data.split(":")[0] == 'EGE1':
        egeList.append(callback_query.data.split(":")[1])
        await bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id, reply_markup=inlineKbEge2)

    elif callback_query.data.split(":")[0] == 'EGE2':
        egeList.append(callback_query.data.split(":")[1])
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

        ege = await fetchEGE(egeList[0], egeList[1])

        # Проверка нашлись ли совпадения
        try:
            if len(ege) > 0:
                await bot.send_message(callback_query.message.chat.id, "Вот на какие направления вы можете подать заявления: \n" + ege)

            else:
                await bot.send_message(callback_query.message.chat.id, "Я не нашел подходящие вам направления")

        except:
            await bot.send_message(callback_query.message.chat.id, "Я не нашел подходящие вам направления")

        egeList.clear()

# Обработка текстового сообщения
@dp.message_handler()
async def message(message: types.Message):
    analysResult = analys_question(message.text)
    question = analysResult[0]
    answer = analysResult[1]
    score = analysResult[2]

    #Отбор наиболее подходящих ответов
    if score >= 50:
        await message.answer(f'{answer}. \n Если я не ответил на ваш вопрос, то вы можете задать вопрос напрямую приемной комиссии по форме:', reply_markup=inlineKbForm)

    elif score >= 30:
        await message.answer(f'Я не нашел ответ на ваш вопрос, возможно вы имели в виду этот вопрос:\n {question}.', reply_markup=inlineKb)

    else:
        await message.answer('Я не нашел ответ на ваш вопрос, но вы можете задать вопрос напрямую приемной комиссии по форме:', reply_markup=inlineKbForm)


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=False)
    except ConnectionError as conErorr:
        print('Connection error:', conErorr)
    except Exception as erorr:
        print('Error:', erorr)