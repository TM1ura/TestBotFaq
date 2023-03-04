import aiosqlite
async def fetchEGE(ege1, ege2):
    db = await aiosqlite.connect('EGE.db')
    cursor = await db.execute(f'''SELECT Направление 
                                    FROM StudyProg 
                                    INNER JOIN Subjects as S on StudyProg.ЕГЭ_1 = S.id 
                                    INNER JOIN Subjects as Sb on StudyProg.ЕГЭ_2 =Sb.id
                                    INNER JOIN Subjects as Sbj on StudyProg.ЕГЭ_3 =Sbj.id  
                                    WHERE S.Предмет = {ege1} and (Sb.Предмет = {ege2} or Sbj.Предмет = {ege2})
                                    ORDER BY ЕГЭ_1''')
    rows = await cursor.fetchall()
    await cursor.close()
    await db.close()

    answer = ''.join(("//-" + row[0] + "\n\n") for row in rows )

    return answer