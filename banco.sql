
CREATE TABLE chamado(
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    cliente TEXT NOT NULL,
    contato TEXT NOT NULL,
    dataabertura TEXT NOT NULL,
    datafechamento TEXT,
    relato TEXT NOT NULL,
    status TEXT NOT NULL,
    fechamento TEXT
);


select * FROM  chamado
drop table chamado

