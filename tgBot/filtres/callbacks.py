from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import BoundFilter
from typing import Union

# Фильтры для кнопок
class YesOrNoFilter(BoundFilter):
    key = 'data_yn'

    def __init__(self, data_yn: Union[str, bool]):
        self.data_yn = data_yn
    async def check(self, callback: CallbackQuery):
        if callback.data == 'Yes':
            self.data_yn = 'is_yes'
            return self.data_yn
        elif callback.data == 'No':
            self.data_yn = 'is_no'
            return self.data_yn
        return self.data_yn is False

class DeclarationFilter(BoundFilter):
    key = 'data_declaration'

    def __init__(self, data_declaration: bool):
        self.data_yes = data_declaration
    async def check(self, callback: CallbackQuery):
        if callback.data == 'Declaration':
            return self.data_yes is True
        return self.data_yes is False

class ConsertFilter(BoundFilter):
    key = 'data_consert'

    def __init__(self, data_consert: bool):
        self.data_consert = data_consert
    async def check(self, callback: CallbackQuery):
        if callback.data == 'Consert':
            return self.data_consert is True
        return self.data_consert is False

class ExamFilter(BoundFilter):
    key = 'data_exam'

    def __init__(self, data_exam: bool):
        self.data_exam = data_exam
    async def check(self, callback: CallbackQuery):
        if callback.data.split(":")[0] == 'exam':
            return self.data_exam is True
        return self.data_exam is False