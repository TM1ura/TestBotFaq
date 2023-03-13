from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

inline_kb_help = InlineKeyboardMarkup(row_width=1)
inline_kb_form = InlineKeyboardMarkup(row_width=1)
inline_kb_declaration = InlineKeyboardMarkup(row_width=1)
inline_kb_consert = InlineKeyboardMarkup(row_width=1)
inline_kb_exam = InlineKeyboardMarkup(row_width=2)
inline_kb_yes_no = InlineKeyboardMarkup(row_width=1)
inline_kb_back = InlineKeyboardMarkup(row_width=1)
inline_kb_dec_bachelor = InlineKeyboardMarkup(row_width=1)

# Ссылки для webApp
url_time = WebAppInfo(url='https://www.masu.edu.ru/abit/rules/application/')
url_form = WebAppInfo(url='https://www.masu.edu.ru/abit/reception/')
url_other_doc = WebAppInfo(url='https://www.masu.edu.ru/abit/admission/apply/')

# inline-кнопки
help = InlineKeyboardButton('Сроки и правила подачи заявлений',
                            web_app=url_time)
form = InlineKeyboardButton('Форма',
                            web_app=url_form)

back = InlineKeyboardButton('Назад',
                            callback_data='Back to main')

back_to_help = InlineKeyboardButton('Назад',
                                    callback_data='Back to help')

declaration_bachelor = InlineKeyboardButton('Заявление на поступление',
                                    url='https://www.masu.edu.ru/upload/iblock/baf/5e4gwvoan7c3e46fb8lomy6s97myrwot/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%B1%D0%B0%D0%BA%D0%B0%D0%BB%D0%B0%D0%B2%D1%80%D0%B8%D0%B0%D1%82%20%D0%B8%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%82%D0%B5%D1%82.doc')

declaration = InlineKeyboardButton('Заявление на поступление',
                                   callback_data='Declaration')
dec_bachelor = InlineKeyboardButton('Бакалавриат и специалитет',
                                    url='https://www.masu.edu.ru/upload/iblock/baf/5e4gwvoan7c3e46fb8lomy6s97myrwot/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%B1%D0%B0%D0%BA%D0%B0%D0%BB%D0%B0%D0%B2%D1%80%D0%B8%D0%B0%D1%82%20%D0%B8%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%82%D0%B5%D1%82.doc')
dec_magistracy = InlineKeyboardButton('Магистратура',
                                      url='https://www.masu.edu.ru/upload/iblock/18c/gpzyizrek88rllpv2q4u9lwn1n6k4xqu/%D0%91%D0%BB%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B2%20%D0%BC%D0%B0%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D1%83%D1%80%D1%83%20%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9.doc')
dec_postgraduate = InlineKeyboardButton('Аспирантура',
                                        url='https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc')
dec_spe = InlineKeyboardButton('Среднее Профессиональное Образование',
                               url='https://www.masu.edu.ru/upload/iblock/4ca/yh97z6hlfbyqf809gy50uiic4kwjb58l/zayavlenie-o-prieme-spo.pdf')


consert = InlineKeyboardButton('Согласие не зачисление',
                               callback_data='Consert')
cons_bac_mag = InlineKeyboardButton('Бакалавриат, специалитет, магистратура',
                                    url='https://www.masu.edu.ru/upload/iblock/5d1/pto9140kxmogqh5ibmqyoivvynlas2tf/%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(1).doc')
cons_postgraduate = InlineKeyboardButton('Аспирантура',
                                         url='https://www.masu.edu.ru/upload/iblock/292/nllq7ompskmr1ndcmeh1oee4760powkw/%D0%97%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%20%D0%BE%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D0%B8%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%9C%D0%90%D0%93%D0%A3%20(%D0%B0%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%B0).doc')


other_doc = InlineKeyboardButton('Другие документы ',
                                 web_app=url_other_doc)


exam_math = InlineKeyboardButton('Математика',
                                 callback_data="exam:'Математика'")
exam_ict = InlineKeyboardButton('ИКТ',
                                callback_data="exam:'ИКТ'")
exam_phys = InlineKeyboardButton('Физика',
                                 callback_data="exam:'Физика'")
exam_geo = InlineKeyboardButton('География',
                                callback_data="exam:'География'")
exam_bio = InlineKeyboardButton('Биология',
                                callback_data="exam:'Биология'")
exam_chem = InlineKeyboardButton('Химия',
                                 callback_data="exam:'Химия'")
exam_soc = InlineKeyboardButton('Обществознание',
                                callback_data="exam:'Обществознание'")
exam_lit = InlineKeyboardButton('Литература',
                                callback_data="exam:'Литература'")
exam_history = InlineKeyboardButton('История',
                                    callback_data="exam:'История'")
exam_for_lang = InlineKeyboardButton('Иностранный язык',
                                     callback_data="exam:'Иностранный язык'")


yes = InlineKeyboardButton('Да, именно этот вопрос я и хотел задать',
                           callback_data='Yes')
no = InlineKeyboardButton('Нет, я хотел задать другой вопрос',
                          callback_data='No')


inline_kb_help.add(help,
                   declaration,
                   consert,
                   other_doc)

inline_kb_form.add(form)

inline_kb_back.add(back)

inline_kb_dec_bachelor.add(declaration_bachelor)

inline_kb_declaration.add(dec_bachelor,
                          dec_magistracy,
                          dec_postgraduate,
                          dec_spe,
                          back_to_help)

inline_kb_consert.add(cons_bac_mag,
                      cons_postgraduate,
                      back_to_help)

inline_kb_exam.add(exam_math,
                   exam_ict,
                   exam_phys,
                   exam_geo,
                   exam_bio,
                   exam_chem,
                   exam_soc,
                   exam_lit,
                   exam_history,
                   exam_for_lang)

inline_kb_yes_no.add(yes,
                     no)