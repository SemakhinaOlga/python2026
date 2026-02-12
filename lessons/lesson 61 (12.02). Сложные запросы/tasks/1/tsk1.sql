DROP TABLE Orders;
DROP TABLE Customers;

CREATE TABLE Customers(
	CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT,
	LastName TEXT,
	Email TEXT
);

CREATE TABLE Orders(
	OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
	CustomerID INTEGER,
	OrderDate TEXT,
	TotalAmount REAL,
	FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Customers (CustomerID, FirstName, LastName, Email) VALUES (1, "John", "Doe", "johndoe@example.com");
INSERT INTO Customers (CustomerID, FirstName, LastName, Email) VALUES (2, "Jane", "Smith", "janesmith@example.com");

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (101, 1, "2025-02-01", 100.50);
INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (102, 2, "2025-02-02", 200.75);



SELECT Customers.FirstName, Customers.LastName, Orders.OrderID, Orders.TotalAmount from Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

SELECT Customers.FirstName, Customers.LastName, Orders.OrderID, Orders.TotalAmount from Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

SELECT FirstName, LastName, NULL AS OrderID, NULL AS TotalAmount From Customers
UNION
SELECT NULL,NULL, OrderID, TotalAmount
From Orders;

SELECT OrderID, CustomerID, OrderDate, TotalAmount from Orders
EXCEPT	
SELECT * from Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

