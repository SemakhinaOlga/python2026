
CREATE TABLE Authors(
	AuthorID INTEGER PRIMARY KEY,
	FirstName TEXT,
	LastName TEXT
);

CREATE TABLE Books(
	BookID INTEGER PRIMARY KEY,
	Title TEXT,
	AuthorID INTEGER, ссфлка на автор????
	PRICE REALm
	FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

DELETE from Books;
DELETE from Authors;
