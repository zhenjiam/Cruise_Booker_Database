SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 1;

DROP TABLE IF EXISTS TripHistories;
DROP TABLE IF EXISTS Passengers;
DROP TABLE IF EXISTS Trips;
DROP TABLE IF EXISTS Cabins;
DROP TABLE IF EXISTS CruiseShips;
DROP TABLE IF EXISTS MealPlans;

CREATE TABLE Passengers (
	passengerID int(11) AUTO_INCREMENT PRIMARY KEY,
	firstName varchar(100) NOT NULL,
	lastName varchar(100) NOT NULL,
	gender CHAR(1) NOT NULL,
	dob date NOT NULL,
	email varchar(255) NOT NULL,
	phoneNumber varchar(15) NOT NULL
);

CREATE TABLE Cabins (
	cabinID int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
	cabinType varchar(100) NOT NULL UNIQUE,
	specialNeeds boolean NOT NULL
);

CREATE TABLE CruiseShips (
	cruiseShipID int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
	shipName varchar(255) NOT NULL UNIQUE,
	destination varchar(100) NOT NULL
);

CREATE TABLE MealPlans (
	mealID int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
	mealPackage varchar(100) NOT NULL UNIQUE,
	detail varchar(225) NOT NULL
);

CREATE TABLE Trips (
	tripID int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
	startDate date NOT NULL,
	cruiseShipID int,
	mealID int,
	cabinID int,
	FOREIGN KEY (cruiseShipID) REFERENCES CruiseShips(cruiseShipID),
	FOREIGN KEY (mealID) REFERENCES MealPlans(mealID),
	FOREIGN KEY (cabinID) REFERENCES Cabins(cabinID)
	ON DELETE CASCADE
);

CREATE TABLE TripHistories (
	tripHistoryID int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
	tripID int NOT NULL,
	passengerID int,
	FOREIGN KEY (tripID) REFERENCES Trips(tripID),
	FOREIGN KEY (passengerID) REFERENCES Passengers(passengerID)
	ON DELETE CASCADE
);

SET FOREIGN_KEY_CHECKS=1;

INSERT INTO Passengers (firstName, lastName, gender, dob, email, phoneNumber) VALUES
("Anna", "Smith", 'F', '1998/04/03', "asmith@gmail.com", 1231234),
("Bob", "Miller", 'M', '1997/05/15', "bmiller@gmail.com", 1235678),
("Cathy", "Evans", 'F', '2000/06/28', "cevans@bing.com", 1239012);

INSERT INTO Cabins (cabinType, specialNeeds) VALUES
("Basic - Lower Deck", '0'),
("Balcony - Upper Deck", '1'),
("Suite - Upper Deck", '1');

INSERT INTO MealPlans (mealPackage, detail) VALUES
("Basic Dining", "3 meals a day at Main Dining Hall. Drinks included" ),
("Chop’s Grille", "Basic Dining + A dinner at Chop’s Grille specialty restaurant" ),
("3-Nights Specialty Dining", "Basic Dining + Dinner at any 3 specialty restaurants"),
("Unlimited Dining", "Basic Dining + A specialty restaurant dinner every night (plus lunch on sea days) for fixed price.");

INSERT INTO CruiseShips (shipName, destination) VALUES
("Stars N Sea", "Puerto Rico"),
("Teressa", "Caribbeans"),
("Sea Wonder", "Bahamas");

INSERT INTO Trips (startDate, cruiseshipID, mealID, cabinID) VALUES
('2021/03/14', 3, 2, 2),
('2020/04/15', 2, 1, 3),
('2020/07/20', 1, 1, 1);

INSERT INTO TripHistories (tripID, passengerID) VALUES
(3, 1),
(2, 2),
(2, 3);

COMMIT;

