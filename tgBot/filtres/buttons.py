from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

# Фильтры для кнопок
class FaqFilter(BoundFilter):
    key = 'is_faq'

    def __init__(self, is_faq: bool):
        self.is_faq = is_faq
    async def check(self, message: Message):
        if message.text == "FAQ":
            return self.is_faq is True
        return self.is_faq is False

class HelpFilter(BoundFilter):
    key = 'is_help'

    def __init__(self, is_help: bool):
        self.is_help = is_help
    async def check(self, message: Message):
        if message.text == "Полезная информация":
            return self.is_help is True
        return self.is_help is False

class TestFilter(BoundFilter):
    key = 'is_test'

    def __init__(self, is_test: bool):
        self.is_test = is_test
    async def check(self, message: Message):
        if message.text == "Тест на профориентацию":
            return self.is_test is True
        return self.is_test is False

class CalculatorFilter(BoundFilter):
    key = 'is_calculator'

    def __init__(self, is_calculator: bool):
        self.is_calculator = is_calculator
    async def check(self, message: Message):
        if message.text == "Калькулятор ЕГЭ":
            return self.is_calculator is True
        return self.is_calculator is False