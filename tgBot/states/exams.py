from aiogram.dispatcher.filters.state import StatesGroup, State

class ExamState(StatesGroup):
    # Состояние для экзамена по рус.яз
    pre_exam = State()

    # Состояния для экзаменов по выбору
    exam1 = State()
    exam2 = State()