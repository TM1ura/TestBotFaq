from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton, WebAppInfo

kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
inlineKbHelp = InlineKeyboardMarkup(row_width=1)
inlineKbForm = InlineKeyboardMarkup(row_width=1)
inlineKb = InlineKeyboardMarkup(row_width=1)

# Ссылки для webApp
urlTime = WebAppInfo(url='https://www.masu.edu.ru/abit/rules/application/')
urlForm = WebAppInfo(url='https://www.masu.edu.ru/abit/reception/')

# Обычные кнопки
btnFaq = KeyboardButton('FAQ')
btnHelp = KeyboardButton('Полезная информация')
btnProfOrient = KeyboardButton('Тест на профориентацию')

# inline-кнопки
inlineHelp = InlineKeyboardButton('Сроки и правила подачи заявлений', web_app=urlTime)
inlineForm = InlineKeyboardButton('Форма', web_app=urlForm)
inlineYes = InlineKeyboardButton('Да, именно этот вопрос я и хотел задать', callback_data='Yes')
inlineNo = InlineKeyboardButton('Нет, я хотел задать другой вопрос', callback_data='No')

kb.add(btnFaq, btnHelp, btnProfOrient)
inlineKbHelp.add(inlineHelp)
inlineKbForm.add(inlineForm)
inlineKb.add(inlineYes, inlineNo)