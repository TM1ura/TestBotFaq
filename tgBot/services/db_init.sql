CREATE TABLE Subjects (
    id int NOT NULL PRIMARY KEY,
    Предмет varchar(12) NOT NULL UNIQUE,
    Баллы int DEFAULT 0
);

CREATE TABLE StudyProg (
    id int NOT NULL PRIMARY KEY,
    Направление varchar(200) NOT NULL,
    ЕГЭ_1 int NOT NULL REFERENCES Subjects (id),
    ЕГЭ_2 int NOT NULL REFERENCES Subjects (id),
    ЕГЭ_3 int REFERENCES Subjects (id)
);

