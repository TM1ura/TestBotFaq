from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from tgBot.states import ExamState
from tgBot.keyboard import inline_kb_exam, inline_kb_back, inline_kb_dec_bachelor
from tgBot.services import fetch_study_prog

# Получение баллов для экзамена по рус.яз
async def pre_exam_score(message: types.Message, state: FSMContext):
    try:
        score = int(message.text)
        await state.update_data(exam_score=score)
        await message.answer(text='Какие экзамены по выбору, которые вы сдавали/будете сдавать',
                             reply_markup=inline_kb_exam)

    except ValueError:
        await message.answer(text='Не правильное значение баллов ЕГЭ, попробуйте снова (указывайте только кол-во баллов, без слов)', reply_markup=inline_kb_back)

    except:
        await message.answer(text='Произошла ошибка, попробуйте снова')
        await state.reset_data()

# Получение баллов для экзаменов по выбору
async def exam1_score(message: types.Message, state: FSMContext):
    try:
        score = int(message.text)
        await state.update_data(exam1_score=score)
        await message.answer('Укажите второй экзамен по выбору',
                             reply_markup=inline_kb_exam)

    except ValueError:
        await message.answer(text='Не правильное значение баллов ЕГЭ, попробуйте снова (указывайте только кол-во баллов, без слов)', reply_markup=inline_kb_back)

    except:
        await message.answer(text='Произошла ошибка, попробуйте снова')
        await state.reset_data()

async def exam2_score(message: types.Message, state: FSMContext):
    try:
        score = int(message.text)
        await state.update_data(exam2_score=score)

    except ValueError:
        await message.answer(text='Не правильное значение баллов ЕГЭ, попробуйте снова (указывайте только кол-во баллов, без слов)', reply_markup=inline_kb_back)

    except:
        await message.answer(text='Произошла ошибка, попробуйте снова')
        await state.reset_data()

    finally:
        exams = await state.get_data()
        study_prog = await fetch_study_prog(exam_score=exams.get('exam_score'),
                                            exam1=exams.get('exam1'),
                                            exam2=exams.get('exam2'),
                                            exam1_score=exams.get('exam1_score'),
                                            exam2_score=exams.get('exam2_score'))

        await message.answer(text=study_prog, reply_markup=inline_kb_dec_bachelor)
        await state.reset_state()

# Регистрация обработчиков сообщений
def register_exams_scores(dispatcher:Dispatcher):
    dispatcher.register_message_handler(callback=pre_exam_score,
                                        state=ExamState.pre_exam)
    dispatcher.register_message_handler(callback=exam1_score,
                                        state=ExamState.exam1)
    dispatcher.register_message_handler(callback=exam2_score,
                                        state=ExamState.exam2)