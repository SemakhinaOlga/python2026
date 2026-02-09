DROP TABLE StudData;
DROP TABLE Empl;
DROP TABLE Shop;

CREATE TABLE StudData(
	id INTEGER,
	name TEXT,
	age INTEGER
);

INSERT INTO StudData (id, name, age) VALUES (1,"Иван",20);
INSERT INTO StudData (id, name, age) VALUES (2,"Мария",22);
INSERT INTO StudData (id, name, age) VALUES (3,"Петр",19);

SELECT * from StudData;

CREATE TABLE Empl(
	id INTEGER,
	name TEXT,
	position TEXT,
	salary INTEGER
);

INSERT INTO Empl (id, name, position, salary) VALUES (1,"Анна", "разработчик", 50000);
INSERT INTO Empl (id, name, position, salary) VALUES (2,"Олег", "Менеджер", 60000);
INSERT INTO Empl (id, name, position, salary) VALUES (3,"Елена", "Дизайнер", 45000);

UPDATE Empl set salary = 65000 WHERE id=2;

SELECT * from Empl;

CREATE TABLE Shop(
	id INTEGER,
	name TEXT,
	price INTEGER,
	quantity INTEGER
);

INSERT INTO Shop (id, name, price, quantity) VALUES (1,"Ноутбук", 45000, 10);
INSERT INTO Shop (id, name, price, quantity) VALUES (2,"Мышь", 1500, 50);
INSERT INTO Shop (id, name, price, quantity) VALUES (3,"Клавиатура", 3000, 25);
INSERT INTO Shop (id, name, price, quantity) VALUES (4,"Монитор", 12000, 15);

DELETE FROM Shop WHERE id=3;
SELECT * from Shop
