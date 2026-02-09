SELECT * FROM train;
SELECT Name from train WHERE Age > 30;
SELECT Name from train WHERE Sex = 'female' AND Pclass = 1;

SELECT Name, Age  from train WHERE Survived = 1 ORDER BY Age;
SELECT Name from train WHERE SibSp = 0 AND Parch = 0;
SELECT Name, Pclass from train WHERE Fare > 100;

SELECT Name, Pclass, Age from train WHERE Pclass != 1 AND Age > 18;
SELECT * from train WHERE Survived = 0 AND SibSp = 0 AND Parch = 0;
SELECT Name, Fare, Pclass from train WHERE Fare < 10 And Pclass != 3;
