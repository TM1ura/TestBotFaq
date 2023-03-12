import aiosqlite
import codecs
from os import path

# Проверка существует ли БД
async def check_db(logger):
    if path.isfile('exams.db'):
        logger.info('exams.db already initiated')
    else:
        logger.info('Initialization exams.db')
        db = await aiosqlite.connect('exams.db')
        init =await codecs.open('tgBot/services/db_init.sql', encoding='utf-8', mode='r')
        insert =await codecs.open('tgBot/services/db_input.sql', encoding='utf-8', mode='r')

        query = "".join(init.readlines())
        await db.executescript(query)
        init.close()

        query = "".join(insert.readlines())
        await db.executescript(query)
        insert.close()

        await db.close()
        logger.info('exams.db initiated')
async def fetch_study_prog(exam1:str, exam2:str, exam_score:int, exam1_score:int, exam2_score:int) -> str:
    db = await aiosqlite.connect('exams.db')

    # Получаем список направлений для заданных экзаменов по выбору
    cursor = await db.execute(f'''SELECT Направление 
                                    FROM StudyProg 
                                    INNER JOIN Subjects as S on StudyProg.ЕГЭ_1 = S.id 
                                    INNER JOIN Subjects as Sb on StudyProg.ЕГЭ_2 =Sb.id
                                    INNER JOIN Subjects as Sbj on StudyProg.ЕГЭ_3 =Sbj.id  
                                    WHERE ((S.Предмет = {exam1} and S.Баллы <= {exam1_score}) and ((Sb.Предмет = {exam2} and Sb.Баллы <= {exam2_score}) or (Sbj.Предмет = {exam2} and Sbj.Баллы <= {exam2_score}))) 
                                        or ((S.Предмет = {exam2} and S.Баллы <= {exam2_score}) and ((Sb.Предмет = {exam1} and Sb.Баллы <= {exam1_score}) or (Sbj.Предмет = {exam1} and Sbj.Баллы <= {exam1_score})))
                                    ORDER BY ЕГЭ_1;''')
    rows = await cursor.fetchall()

    # Получаем проходня баллы для обязательного экзамена по рус.яз
    cursor = await db.execute('''SELECT Баллы
                                            FROM Subjects
                                            WHERE Предмет = 'Русский язык'; ''')
    rus_exam_score = int((await cursor.fetchone())[0])

    await cursor.close()
    await db.close()

    answer = ''.join(("//-" + row[0] + "\n\n") for row in rows )

    try:
        if (len(answer) > 0) and exam_score >= rus_exam_score:
            answer = "Вот на какие направления вы можете подать заявления: \n" + answer

        else:
            answer = "Я не нашел подходящие вам направления"

    except:
            answer = "Произошла ошибка, попробуйте снова"

    return answer