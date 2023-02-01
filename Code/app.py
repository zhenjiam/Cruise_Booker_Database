# Adapted module from: https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/bsg_people_app/app.py
# Date: 06/06/2022

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_jeanchaw'
app.config['MYSQL_PASSWORD'] = '3644' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_jeanchaw'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes 

#route for the homepage of the directory
@app.route('/')
def home():
    return render_template("/home.j2")

#_____________________________________________________________
# Cabins

#route for cabins page
@app.route("/cabins", methods=["POST","GET"])
def cabin():

    #insert a cabin into the cabin entity
    if request.method == "POST":
        #user presses the add cabin button
        if request.form.get("Add_Cabin"):
            #grabs user inputs
            cabinType = request.form["cabinType"]
            specialNeeds = request.form["specialNeeds"]

            #mySQL query to insert a new cabin
            query = "INSERT INTO Cabins (cabinType, specialNeeds) VALUES (%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (cabinType, specialNeeds))
            mysql.connection.commit()

            return redirect("/cabins")

    if request.method == "GET":
        #mySQL query to grab all the cabins in Cabins
        query = "SELECT * FROM Cabins;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        Cabins = cur.fetchall()

    #render cabins page passing query data 
    return render_template("/cabins.j2", Cabins=Cabins)

#route for delete cabin
@app.route("/delete_cabin/<int:id>", methods=["POST", "GET"])
def delete_cabin(id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Cabins WHERE cabinID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to cabins page
    return redirect("/cabins")

#route for edit cabins
@app.route("/edit_cabin/<int:id>", methods=["POST", "GET"])
def edit_cabin(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Cabins WHERE cabinID = %s;" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        Cabins = cur.fetchall()

        # render edit_cabins page passing our query data to the edit_cabins template
        return render_template("edit_cabin.j2", Cabins=Cabins)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Cabin' button
        if request.form.get("Edit_Cabin"):
            # grab user form inputs
            id = request.form["cabinID"]
            cabinType = request.form["cabinType"]
            specialNeeds = request.form["specialNeeds"]

            # no null inputs
            query = "UPDATE Cabins SET Cabins.cabinType = %s, Cabins.specialNeeds = %s WHERE Cabins.cabinID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (cabinType, specialNeeds, id))
            mysql.connection.commit()

            # redirect back to cabins page after we execute the update query
            return redirect("/cabins")

#____________________________________________
# Meal Plan

@app.route("/mealplans", methods=["POST","GET"])
def mealplan():

    #insert a meal plan into the MealPlan entity
    if request.method == "POST":
        #user presses the add meal plan button
        if request.form.get("Add_MealPlan"):
            #grabs user inputs
            mealPackage = request.form["mealPackage"]
            detail = request.form["detail"]

            #mySQL query to insert a new meal plan
            query = "INSERT INTO MealPlans (mealPackage, detail) VALUES (%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (mealPackage, detail))
            mysql.connection.commit()

            return redirect("/mealplans")

    if request.method == "GET":
        #mySQL query to grab all the meal plans in MealPlans
        query = "SELECT * FROM MealPlans;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        MealPlans = cur.fetchall()

    #render meal plans page passing query data 
    return render_template("/mealplans.j2", MealPlans=MealPlans)

#route for delete meal plans
@app.route("/delete_mealplan/<int:id>", methods=["POST", "GET"])
def delete_mealplan(id):
    # mySQL query to delete the meal plan with our passed id
    query = "DELETE FROM MealPlans WHERE mealID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to mealplans page
    return redirect("/mealplans")

#route for edit Meal Plans
@app.route("/edit_mealplan/<int:id>", methods=["POST", "GET"])
def edit_mealplan(id):
    if request.method == "GET":
        # mySQL query to grab the info of the mealplan with our passed id
        query = "SELECT * FROM MealPlans WHERE mealID = %s;" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        MealPlans = cur.fetchall()

        # render edit_mealplan page passing our query data to the edit_meal_plans template
        return render_template("edit_mealplan.j2", MealPlans=MealPlans)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit MealPlan' button
        if request.form.get("Edit_MealPlan"):
            # grab user form inputs
            id = request.form["mealID"]
            mealPackage = request.form["mealPackage"]
            detail = request.form["detail"]

            # no null inputs
            query = "UPDATE MealPlans SET MealPlans.mealPackage = %s, MealPlans.detail = %s WHERE MealPlans.mealID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (mealPackage, detail, id))
            mysql.connection.commit()

            # redirect back to meal plans page after we execute the update query
            return redirect("/mealplans")


#___________________________________________________
# Cruise Ships


@app.route("/cruiseships", methods=["POST","GET"])
def cruiseship():

    #insert a cruise ship into the CruiseShips entity
    if request.method == "POST":
        #user presses the add cruise ship button
        if request.form.get("Add_CruiseShip"):
            #grabs user inputs
            shipName = request.form["shipName"]
            destination = request.form["destination"]

            #mySQL query to insert a new cruise ship
            query = "INSERT INTO CruiseShips (shipName, destination) VALUES (%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (shipName, destination))
            mysql.connection.commit()

            return redirect("/cruiseships")

    if request.method == "GET":
        #mySQL query to grab all the meal plans in CruiseShips
        query = "SELECT * FROM CruiseShips;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        CruiseShips = cur.fetchall()

    #render cruise ships page passing query data 
    return render_template("/cruiseships.j2", CruiseShips=CruiseShips)

#route for delete cruise ships
@app.route("/delete_cruiseship/<int:id>", methods=["POST", "GET"])
def delete_cruiseship(id):
    # mySQL query to delete the cruise ship with our passed id
    query = "DELETE FROM CruiseShips WHERE cruiseShipID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to cruise ships page
    return redirect("/cruiseships")

#route for edit Cruise Ships
@app.route("/edit_cruiseship/<int:id>", methods=["POST", "GET"])
def edit_cruiseship(id):
    if request.method == "GET":
        # mySQL query to grab the info of the cruise ship with our passed id
        query = "SELECT * FROM CruiseShips WHERE cruiseShipID = %s;" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        CruiseShips = cur.fetchall()

        # render edit_cruiseships page passing our query data to the edit_cruise_ship template
        return render_template("edit_cruiseship.j2", CruiseShips=CruiseShips)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit CruiseShips' button
        if request.form.get("Edit_CruiseShip"):
            # grab user form inputs
            id = request.form["cruiseShipID"]
            shipName = request.form["shipName"]
            destination = request.form["destination"]

            # no null inputs
            query = "UPDATE CruiseShips SET CruiseShips.shipName = %s, CruiseShips.destination = %s WHERE CruiseShips.cruiseShipID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (shipName, destination, id))
            mysql.connection.commit()

            # redirect back to cruiseships page after we execute the update query
            return redirect("/cruiseships")

#___________________________________________________
# Trips

@app.route("/trips", methods=["POST","GET"])
def trip():

    #insert a trip into the Trips entity
    if request.method == "POST":
        #user presses the add trips button
        if request.form.get("Add_Trip"):
            #grabs user inputs
            startDate = request.form["startDate"]
            cruiseShipID = request.form["cruiseShipID"]
            mealID = request.form["mealID"]
            cabinID = request.form["cabinID"]

            #mySQL query to insert a new trip
            query = "INSERT INTO Trips (startDate, cruiseShipID, mealID, cabinID) VALUES(%s, %s, %s, %s);" 
            cur = mysql.connection.cursor()
            cur.execute(query, (startDate, cruiseShipID, mealID, cabinID))
            mysql.connection.commit()

            return redirect("/trips")

    if request.method == "GET":
        #mySQL query to grab all the trips in Trips
        query = "SELECT * FROM Trips;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        Trips = cur.fetchall()

    #render trips page passing query data 
    return render_template("/trips.j2", Trips=Trips)

#route for delete trips
@app.route("/delete_trip/<int:id>", methods=["POST", "GET"])
def delete_trip(id):
    # mySQL query to delete the trip with our passed id
    query = "DELETE FROM Trips WHERE tripID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
     # redirect back to trips page
    return redirect("/trips")

#route for edit Trips
@app.route("/edit_trip/<int:id>", methods=["POST", "GET"])
def edit_trip(id):
    if request.method == "GET":
        # mySQL query to grab the info of the trip with our passed id
        query = "SELECT * FROM Trips WHERE tripID = %s;" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        Trips = cur.fetchall()

        # render edit_trip page passing our query data to the edit_trip template
        return render_template("edit_trip.j2", Trips=Trips)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Trip' button
        if request.form.get("Edit_Trip"):
            # grab user form inputs
            id = request.form["tripID"]
            startDate = request.form["startDate"]
            cruiseShipID = request.form["cruiseShipID"]
            mealID = request.form["mealID"]
            cabinID = request.form["cabinID"]

            # no null inputs
            query = "UPDATE Trips SET Trips.startDate = %s, Trips.cruiseShipID =  %s, Trips.mealID = %s, Trips.cabinID = %s WHERE tripID = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (startDate, cruiseShipID, mealID, cabinID, id))
            mysql.connection.commit()

            # redirect back to cabins page after we execute the update query
            return redirect("/trips")

#___________________________________________________________
# Passengers 

#route for Passengers page
@app.route("/passengers", methods=["POST","GET"])
def passenger():

    # insert a passenger into the Passengers entity
    if request.method == "POST":
        # user clicks "add passenger" button
        if request.form.get("Add_Passenger"):
            # takes user inputs
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            gender = request.form["gender"]
            dob = request.form["dob"]
            email = request.form["email"]
            phoneNumber = request.form["phoneNumber"]

            #MySQL query for inserting a new passenger
            query = "INSERT INTO Passengers (firstName, lastName, gender, dob, email, phoneNumber) VALUES (%s, %s, %s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (firstName, lastName, gender, dob, email, phoneNumber))
            mysql.connection.commit()

            return redirect("/passengers")

    if request.method == "GET":
        # MySQL query to get all the passengers in Passengers entity
        query = "SELECT * FROM Passengers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        Passengers = cur.fetchall()

    #render passengers page passing query data
    return render_template("/passengers.j2", Passengers=Passengers)

# route for deleting passengers
@app.route("/delete_passenger/<int:id>", methods=["POST", "GET"])
def delete_passenger(id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Passengers WHERE passengerID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to passengers page
    return redirect("/passengers")

#route for editting passengers
@app.route("/edit_passenger/<int:id>", methods=["POST", "GET"])
def edit_passenger(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Passengers WHERE passengerID = %s;" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        Passengers = cur.fetchall()

        # render edit_passengers page passing our query data to the edit_passengers template
        return render_template("edit_passenger.j2", Passengers=Passengers)

    if request.method == "POST":
        # user clicks the 'Edit Passengers' button
        if request.form.get("Edit_Passenger"):
            # grab user form inputs
            id = request.form["passengerID"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            gender = request.form["gender"]
            dob = request.form["dob"]
            email = request.form["email"]
            phoneNumber = request.form["phoneNumber"]

            # no null inputs
            query = "UPDATE Passengers SET Passengers.firstName = %s, Passengers.lastName = %s, Passengers.gender = %s," \
                    "Passengers.dob = %s, Passengers.email = %s, Passengers.phoneNumber = %s WHERE Passengers.passengerID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (firstName, lastName, gender, dob, email, phoneNumber, id))
            mysql.connection.commit()

            # redirect back to passengers page after we execute the update query
            return redirect("/passengers")

#___________________________________________________________
# TripHistories 

#route for TripHistories page
@app.route("/triphistories", methods=["POST","GET"])
def triphistory():

    # insert a tripHistory into the TripHistories entity
    if request.method == "POST":
        # user clicks "add trip history" button
        if request.form.get("Add_TripHistory"):
            # takes user inputs
            passengerID = request.form["passengerID"]
            tripID = request.form["tripID"]
            
            #MySQL query for inserting a new trip history
            query = "INSERT INTO TripHistories (passengerID, tripID) VALUES (%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (passengerID, tripID))
            mysql.connection.commit()

            return redirect("/triphistories")

    if request.method == "GET":
        # MySQL query to get all the triphistories in TripHistories entity
        query = "SELECT * FROM TripHistories"
        cur = mysql.connection.cursor()
        cur.execute(query)
        TripHistories = cur.fetchall()

    #render triphistories page passing query data
    return render_template("/triphistories.j2", TripHistories = TripHistories)

# route for deleting passengers
@app.route("/delete_triphistory/<int:id>", methods=["POST", "GET"])
def delete_triphistory(id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM TripHistories WHERE tripHistoryID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to passengers page
    return redirect("/triphistories")

#route for editting passengers
@app.route("/edit_triphistory/<int:id>", methods=["POST", "GET"])
def edit_triphistory(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM TripHistories WHERE tripHistoryID = %s;" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        TripHistories = cur.fetchall()

        # render edit_passengers page passing our query data to the edit_passengers template
        return render_template("edit_triphistory.j2", TripHistories=TripHistories)

    if request.method == "POST":
        # user clicks the 'Edit TripHistory' button
        if request.form.get("Edit_TripHistory"):
            # grab user form inputs
            passengerID = request.form["passengerID"]
            tripID = request.form["tripID"]

            # no null inputs
            query = "UPDATE TripHistories SET TripHistories.passengerID = %s, TripHistories.tripID = %s WHERE TripHistories.tripHistoryID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (passengerID, tripID, id))
            mysql.connection.commit()

            # redirect back to triphistories page after we execute the update query
            return redirect("/triphistories")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 11918)) 
    app.run(port=port, debug=True) 
