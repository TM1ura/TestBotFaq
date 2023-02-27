from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton, WebAppInfo

kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
inlineKbHelp = InlineKeyboardMarkup(row_width=1)
inlineKbForm = InlineKeyboardMarkup(row_width=1)
inlineKbDeclaration = InlineKeyboardMarkup(row_width=1)
inlineKbConsert = InlineKeyboardMarkup(row_width=1)
inlineKb = InlineKeyboardMarkup(row_width=2)

# Ссылки для webApp
urlTime = WebAppInfo(url='https://www.masu.edu.ru/abit/rules/application/')
urlForm = WebAppInfo(url='https://www.masu.edu.ru/abit/reception/')
urlOtherDoc = WebAppInfo(url='https://www.masu.edu.ru/abit/admission/apply/')

# Обычные кнопки
btnFaq = KeyboardButton('FAQ')
btnHelp = KeyboardButton('Полезная информация')
btnProfOrient = KeyboardButton('Тест на профориентацию')

# inline-кнопки
inlineHelp = InlineKeyboardButton('Сроки и правила подачи заявлений', web_app=urlTime)
inlineForm = InlineKeyboardButton('Форма', web_app=urlForm)

inlineDeclaration = InlineKeyboardButton('Заявление на поступление', callback_data='Declaration')
inlineDecBachelor = InlineKeyboardButton('Бакалавриат и специалитет', url='https://www.masu.edu.ru/upload/iblock/baf/5e4gwvoan7c3e46fb8lomy6s97myrwot/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%B1%D0%B0%D0%BA%D0%B0%D0%BB%D0%B0%D0%B2%D1%80%D0%B8%D0%B0%D1%82%20%D0%B8%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%82%D0%B5%D1%82.doc')
inlineDecMagistracy = InlineKeyboardButton('Магистратура', url='https://www.masu.edu.ru/upload/iblock/18c/gpzyizrek88rllpv2q4u9lwn1n6k4xqu/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B2%20%D0%BC%D0%B0%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D1%83%D1%80%D1%83%20%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9.doc')
inlineDecPostgraduate = InlineKeyboardButton('Аспирантура', url='https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc')
inlineDecSPE = InlineKeyboardButton('Среднее Профессиональное Образование', url='https://www.masu.edu.ru/upload/iblock/4ca/yh97z6hlfbyqf809gy50uiic4kwjb58l/zayavlenie-o-prieme-spo.pdf')

inlineConsert = InlineKeyboardButton('Согласие не зачисление', callback_data='Consert')
inlineConsBM = InlineKeyboardButton('Бакалавриат, специалитет, магистратура', url='https://www.masu.edu.ru/upload/iblock/5d1/pto9140kxmogqh5ibmqyoivvynlas2tf/%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(1).doc')
inlineConsPostgraduate = InlineKeyboardButton('Аспирантура', url='https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc')

inlineOtherDoc = InlineKeyboardButton('Другие документы ', web_app=urlOtherDoc)

inlineYes = InlineKeyboardButton('Да, именно этот вопрос я и хотел задать', callback_data='Yes')
inlineNo = InlineKeyboardButton('Нет, я хотел задать другой вопрос', callback_data='No')

kb.add(btnFaq, btnHelp, btnProfOrient)
inlineKbHelp.add(inlineHelp, inlineDeclaration, inlineConsert, inlineOtherDoc)
inlineKbForm.add(inlineForm)
inlineKbDeclaration.add(inlineDecBachelor, inlineDecMagistracy, inlineDecPostgraduate, inlineDecSPE)
inlineKbConsert.add(inlineConsBM, inlineConsPostgraduate)
inlineKb.add(inlineYes, inlineNo)