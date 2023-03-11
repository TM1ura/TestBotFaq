from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import BoundFilter
from typing import Union

# Фильтры для кнопок
class YesCallbackFilter(BoundFilter):
    key = 'data_yes'

    def __init__(self, data_yes: Union[str, bool]):
        self.data_yes = data_yes
    async def check(self, callback: CallbackQuery):
        if callback.data == 'Yes':
            return self.data_yes is True
        return self.data_yes is False

class NoCallbackFilter(BoundFilter):
    key = 'data_no'

    def __init__(self, data_no: bool):
        self.data_no = data_no
    async def check(self, callback: CallbackQuery):
        if callback.data == 'No':
            return self.data_no is True
        return self.data_no is False
class DeclarationFilter(BoundFilter):
    key = 'data_declaration'

    def __init__(self, data_declaration: bool):
        self.data_declaration = data_declaration
    async def check(self, callback: CallbackQuery):
        if callback.data == 'Declaration':
            return self.data_declaration is True
        return self.data_declaration is False

class ConsertFilter(BoundFilter):
    key = 'data_consert'

    def __init__(self, data_consert: bool):
        self.data_consert = data_consert
    async def check(self, callback: CallbackQuery):
        if callback.data == 'Consert':
            return self.data_consert is True
        return self.data_consert is False

class BackToHelpFilter(BoundFilter):
    key = 'data_to_help'

    def __init__(self, data_to_help: bool):
        self.data_to_help = data_to_help
    async def check(self, callback: CallbackQuery):
        if callback.data == 'Back to help':
            return self.data_to_help is True
        return self.data_to_help is False
class ExamFilter(BoundFilter):
    key = 'data_exam'

    def __init__(self, data_exam: bool):
        self.data_exam = data_exam
    async def check(self, callback: CallbackQuery):
        if callback.data.split(":")[0] == 'exam':
            return self.data_exam is True
        return self.data_exam is False