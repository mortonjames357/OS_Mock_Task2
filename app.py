# Imports
import os
import sqlite3
from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from setupDB import start_database
from queries.users_queries import *
from queries.bookings_queries import *
from queries.technician_queries import *
from queries.appointments_queries import *
from calculators.carbon_calc import calculate_carbon_footprint
from calculators.energy_calc import calculate_energy

# Creating the flask app
app = Flask(__name__, static_folder='./static')
app.secret_key= "secret_key"

# Route for home
@app.route('/', methods=['GET', 'POST'])
def home():
    # Getting data for create appointment function from home page
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        reason = request.form.get('textInput')

        create_appoint(name, email, reason)
    # Rendering the page
    return render_template('index.html')


# Route for view all page
@app.route('/view_all', methods=['GET', 'POST'])
def view_all():
    # Setting the data as none
    bookings = None
    users = None
    technicians = None
    appoints = None

    # Getting data from form
    if request.method == 'POST':
        action = request.form.get('action')

        # Setting data dependant on the button pressed
        if action == 'ViewBookings':
            bookings = get_all_bookings()
            
        elif action == 'ViewUsers':
            users = get_all_users()
            
        elif action == 'ViewTechnicians':
            technicians = get_all_techs()

        elif action == "ViewAppointments":
            appoints = get_all_appointments()

        # Delere form actions
        elif action == 'Delete':
            delete_type = request.form.get('deleteType')
            id_input = request.form.get('idInput')
            
            if delete_type == 'Booking':
                delete_booking(id_input)
                bookings = get_all_bookings()
            elif delete_type == 'User':
                delete_user(id_input)
                users = get_all_users()
            elif delete_type == 'Technician':
                delete_tech(id_input)
                technicians = get_all_techs()
            elif delete_type == "Appointment":
                delete_appoint(id_input)
                appoints = get_all_appointments()
    # Setting bookings data before any buttons have been pressed
    else:
        bookings = get_all_bookings()

    # Rendering the page and data in the page
    return render_template(
        'view_all.html', 
        bookings=bookings, 
        users=users, 
        technicians=technicians,
        appoints=appoints
    )


# Route to create a booking page
@app.route('/create_booking_page', methods=['GET', 'POST'])
def create_booking_page():
    # Gathering data for create booking
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        address = request.form.get('address')
        date = request.form.get('date')
        time = request.form.get('time')
        booking_type = request.form.get('bookingType')
        booking_status = request.form.get('bookingStatus')
        tech_id = request.form.get('techID')
        
        # Creating booking with data
        create_booking(user_id, address, date, time, booking_type, booking_status, tech_id)
    # Rendering page
    return render_template('create_booking.html')


# Route for view specific page
@app.route('/view_specific', methods=['GET', 'POST'])
def view_specific():
    # Setting data to none
    booking = None
    user = None
    tech = None
    appoint = None

    # Gathering form data
    if request.method == 'POST':
        id_input = request.form.get('idInput')
        entity_type = request.form.get('entityType')

        # Setting data based on form inputs
        if entity_type == 'Booking':
            booking = get_booking_by_id(id_input)
        elif entity_type == 'User':
            user = get_user_by_id(id_input)
        elif entity_type == 'Technician':
            tech = get_tech_by_id(id_input)
        elif entity_type == 'Appointment':
            appoint = get_appoint_by_id(id_input)
    
    # Rendering the page     
    return render_template(
        'view_specific.html', 
        booking=booking, 
        user=user, 
        tech=tech,
        appoint=appoint
    )

# Route for the carbon calculator
@app.route('/carbon_calc', methods=['GET', 'POST'])
def carbon_calc():
    # Setting data as empty
    result = ""
    score = ""
    # Gathering data from form
    if request.method == 'POST':
        tranportMethod = request.form.get('transportMethod')
        transportAmount = int(request.form.get('transportAmount'))
        Ev = request.form.get('EV')
        renewType = request.form.get('renewableType')
        lights = request.form.get('lights')
        heating = request.form.get('heating')
        takeawayFreq = request.form.get('takeawayFreq')
        foodType = request.form.get('foodType')

        # Calculating the footprint
        temp = calculate_carbon_footprint(tranportMethod, transportAmount, Ev, renewType, lights, heating, takeawayFreq, foodType)
        # Getting the result and score from temp tuple
        result = temp[0]
        score = temp[1]

    # Rendering template
    return render_template(
        'carbon_calc.html',
        result=result,
        score=score
        )

# Route for energy calculator 
@app.route('/energy_calc', methods=['GET', 'POST'])
def energy_calc():
    # Setting data to nothing
    cost = ""

    # Getting data from form
    if request.method == "POST":
        wattage = int(request.form.get('wattage'))
        hours = int(request.form.get('hours'))
        price = float(request.form.get('price'))
        cost = calculate_energy(wattage, hours, price)

    # Rendering page and data
    return render_template(
        'energy_calc.html',
        cost=cost
        )

# Starting the database and the app
if __name__ == '__main__':
    start_database()
    app.run(debug=True)


