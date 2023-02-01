-- Group 98: The Team
-- Group Members: Jia May Zheng, Wesley Jean-Charles
-- Project Step 6


------------------------------------------------
-- Retrieve and display all existing information from the tables
------------------------------------------------
-- Display all passenger's information.
SELECT * FROM Passengers;
-- Display all trip information.
SELECT * FROM Trips;
-- Display all meal plan information
SELECT * FROM MealPlans;
-- Display all cruise ship information.
SELECT * FROM CruiseShips;
-- Display all cabin information.
SELECT * FROM Cabins;
-- Display all trip history information
SELECT * FROM TripHistories;


------------------------------------------------
-- View trip history
------------------------------------------------
-- Get all trips associated with inputted passenger id.
SELECT * FROM Trips 
    JOIN TripHistories ON Trips.tripID = TripHistories.tripID
    JOIN Passengers ON TripHistories.passengerID = Passengers.passengerID 
    WHERE passengerID = :passengerIDInput;
-- GET all passengers associated with an inputted trip id.
SELECT * FROM Passengers
    JOIN TripHistories ON Passengers.passengerID = TripHistories.passengerID
    JOIN Trips ON TripHistories.tripID = Trips.tripID 
    WHERE tripID = :tripIDInput;


------------------------------------------------
-- Add new entry to tables
------------------------------------------------
-- Add a new passenger
INSERT INTO Passengers (firstName, lastName, gender, dob, email, phoneNumber)
    VALUES (:firstNameInput, :lastNameInput, :genderInput, :dobInput, :emailInput, 
    :phoneNumberInput);
-- Add a new trip
INSERT INTO Trips (startDate, cruiseShipID, mealID, cabinID)
	VALUES(:startDateInput, :cruiseShipIDInput, :mealIDInput, :cabinIDInput);
-- Associate a passenger with a trip (M-to-N relationship addition)
INSERT INTO TripHistories (passengerID, tripID) 
    VALUES (:passengerIDInput, :tripIDInput);
-- Add a new cruise ship
INSERT INTO CruiseShips(shipName, destination)
    VALUES (:shipNameInput, :destinationInput);
-- Add a new meal plan
INSERT INTO MealPlans(mealPackage, detail)
    VALUES (:mealPackageInput, :detailInput);
-- Add a new cabin type
INSERT INTO Cabins(cabinType, specialNeeds)
    VALUES (:cabinTypeInput, :specialNeedsInput);


------------------------------------------------
-- Update an existing entry's information
------------------------------------------------
-- Update a passenger's information and populate the fields with pre-existing data.
SELECT * FROM Passengers WHERE passengerID = :passengerIDInput;
UPDATE Passengers 
    SET firstName = :firstNameInput, lastName = :lastNameInput, gender = :genderInput, dob = :dobInput, 
        email = :emailInput, phoneNumber = :phoneNumberInput 
    WHERE passengerID = :passengerIDInput;
-- Update a trip's information and populate the fields with pre-existing data.
SELECT * FROM Trips WHERE tripID = :tripIDInput;
UPDATE Trips 
	SET startDate = :startDateInput, cruiseShipID = :cruiseShipIDInput, mealID = :mealIDInput, cabinID = cabinIDInput 
    WHERE tripID = :tripIDInput; 
-- Update a cruise ship's information and populate the fields with pre-existing data.
SELECT * FROM CruiseShips WHERE cruiseShipID = :cruiseShipIDInput;
UPDATE CruiseShips
    SET shipName = :shipNameInput, destination = :destinationInput
    WHERE cruiseShipID = :cruiseShipIDInput;
-- Update a meal plan's information and populate the fields with pre-existing data.
SELECT * FROM MealPlans WHERE mealID = :mealIDInput;
UPDATE MealPlans
    SET mealPackage = :mealPackageInput, description = :descriptionInput
    WHERE mealID = :mealIDInput;
-- Update a cabin's information and populate the fields with pre-existing data.
SELECT * FROM Cabins WHERE cabinID = :cabinIDInput;
UPDATE Cabins
    SET cabinType = :cabinTypeInput, specialNeeds = :specialNeedsInput
    WHERE cabinID = :cabinIDInput;

------------------------------------------------
-- Delete an entry from the tables
------------------------------------------------
-- Delete a passenger.
DELETE FROM Passengers WHERE passengerID = :passengerIDInput;
-- Disassociate a deleted passenger from all trips (M-to-N relationship deletion)
DELETE FROM TripHistories WHERE passengerID = :passengerIDInput;

-- Delete a trip that has not been taken yet.
DELETE FROM Trips WHERE tripID = :tripIDInput;
-- Diassociate a deleted trip from all passengers (M-to-N relationship deletion)
DELETE FROM TripHistories WHERE tripID = :tripIDInput;

-- Delete a cruiseship.
DELETE FROM CruiseShips WHERE cruiseShipID = :cruiseShipIDInput;

-- Delete a meal plan.
DELETE FROM MealPlans WHERE mealID = :mealIDInput;

-- Delete a cabin.
DELETE FROM Cabins WHERE cabinID = :cabinIDInput










