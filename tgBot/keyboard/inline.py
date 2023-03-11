from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

inlineKbHelp = InlineKeyboardMarkup(row_width=1)
inlineKbForm = InlineKeyboardMarkup(row_width=1)
inlineKbDeclaration = InlineKeyboardMarkup(row_width=1)
inlineKbConsert = InlineKeyboardMarkup(row_width=1)
inlineKbExam = InlineKeyboardMarkup(row_width=2)
inlineKbYesNo = InlineKeyboardMarkup(row_width=1)

# Ссылки для webApp
urlTime = WebAppInfo(url='https://www.masu.edu.ru/abit/rules/application/')
urlForm = WebAppInfo(url='https://www.masu.edu.ru/abit/reception/')
urlOtherDoc = WebAppInfo(url='https://www.masu.edu.ru/abit/admission/apply/')

# inline-кнопки
help = InlineKeyboardButton('Сроки и правила подачи заявлений',
                                  web_app=urlTime)
form = InlineKeyboardButton('Форма',
                                  web_app=urlForm)


declaration = InlineKeyboardButton('Заявление на поступление',
                                         callback_data='Declaration')
decBachelor = InlineKeyboardButton('Бакалавриат и специалитет',
                                         url='https://www.masu.edu.ru/upload/iblock/baf/5e4gwvoan7c3e46fb8lomy6s97myrwot/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%B1%D0%B0%D0%BA%D0%B0%D0%BB%D0%B0%D0%B2%D1%80%D0%B8%D0%B0%D1%82%20%D0%B8%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%82%D0%B5%D1%82.doc')
decMagistracy = InlineKeyboardButton('Магистратура',
                                           url='https://www.masu.edu.ru/upload/iblock/18c/gpzyizrek88rllpv2q4u9lwn1n6k4xqu/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B2%20%D0%BC%D0%B0%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D1%83%D1%80%D1%83%20%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9.doc')
decPostgraduate = InlineKeyboardButton('Аспирантура',
                                             url='https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc')
decSPE = InlineKeyboardButton('Среднее Профессиональное Образование',
                                    url='https://www.masu.edu.ru/upload/iblock/4ca/yh97z6hlfbyqf809gy50uiic4kwjb58l/zayavlenie-o-prieme-spo.pdf')


consert = InlineKeyboardButton('Согласие не зачисление',
                                     callback_data='Consert')
consBM = InlineKeyboardButton('Бакалавриат, специалитет, магистратура',
                                    url='https://www.masu.edu.ru/upload/iblock/5d1/pto9140kxmogqh5ibmqyoivvynlas2tf/%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(1).doc')
consPostgraduate = InlineKeyboardButton('Аспирантура',
                                              url='https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc')


otherDoc = InlineKeyboardButton('Другие документы ',
                                      web_app=urlOtherDoc)


examMath = InlineKeyboardButton('Математика',
                                callback_data="exam:'Математика'")
examICT = InlineKeyboardButton('ИКТ',
                                callback_data="exam:'ИКТ'")
examPhys = InlineKeyboardButton('Физика',
                                callback_data="exam:'Физика'")
examGeo = InlineKeyboardButton('География',
                               callback_data="exam:'География'")
examBio = InlineKeyboardButton('Биология',
                                callback_data="exam:'Биология'")
examChem = InlineKeyboardButton('Химия',
                                callback_data="exam:'Химия'")
examSoc = InlineKeyboardButton('Обществознание',
                                callback_data="exam:'Обществознание'")
examLit = InlineKeyboardButton('Литература',
                                callback_data="exam:'Литература'")
examHistory = InlineKeyboardButton('История',
                                    callback_data="exam:'История'")
examForLang = InlineKeyboardButton('Иностранный язык',
                                    callback_data="exam:'Иностранный язык'")


yes = InlineKeyboardButton('Да, именно этот вопрос я и хотел задать',
                                 callback_data='Yes')
no = InlineKeyboardButton('Нет, я хотел задать другой вопрос',
                                callback_data='No')


inlineKbHelp.add(help,
                 declaration,
                 consert,
                 otherDoc)

inlineKbForm.add(form)

inlineKbDeclaration.add(decBachelor,
                        decMagistracy,
                        decPostgraduate,
                        decSPE)

inlineKbConsert.add(consBM,
                    consPostgraduate)

inlineKbExam.add(examMath,
                 examICT,
                 examPhys,
                 examGeo,
                 examBio,
                 examChem,
                 examSoc,
                 examLit,
                 examHistory,
                 examForLang)

inlineKbYesNo.add(yes,
                  no)