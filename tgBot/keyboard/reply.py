from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

# Обычные кнопки
btnFaq = KeyboardButton('FAQ')
btnHelp = KeyboardButton('Полезная информация')
btnProfOrient = KeyboardButton('Тест на профориентацию')
btnEge = KeyboardButton('Калькулятор ЕГЭ')

kb.add(btnFaq,
       btnHelp,
       btnProfOrient,
       btnEge)
