from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton, WebAppInfo

kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
inlineKbHelp = InlineKeyboardMarkup(row_width=1)
inlineKbForm = InlineKeyboardMarkup(row_width=1)

urlTime = WebAppInfo(url='https://www.masu.edu.ru/abit/rules/application/')
urlForm = WebAppInfo(url='https://www.masu.edu.ru/abit/reception/')

btnFaq = KeyboardButton('FAQ')
btnHelp = KeyboardButton('Полезная информация')
btnProfOrient = KeyboardButton('Тест на профориентацию')

inlineHelp = InlineKeyboardButton('Сроки и правила подачи заявлений', web_app=urlTime)

inlineForm = InlineKeyboardButton('Форма', web_app=urlForm)

inlineKbForm.add(inlineForm)
inlineKbHelp.add(inlineHelp)
kb.add(btnFaq, btnHelp, btnProfOrient)