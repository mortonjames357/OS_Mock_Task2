import os
import sqlite3
from flask import Flask, request, render_template
from setupDB import start_database
from queries.users_queries import *
from queries.bookings_queries import *
from queries.technician_queries import *
from queries.appointments_queries import *
from carbon_calc import calculate_carbon_footprint

app = Flask(__name__, static_folder='./static')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        reason = request.form.get('textInput')

        create_appoint(name, email, reason)
    return render_template('index.html')



@app.route('/view_all', methods=['GET', 'POST'])
def view_all():
    bookings = None
    users = None
    technicians = None
    appoints = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'ViewBookings':
            bookings = get_all_bookings()
            
        elif action == 'ViewUsers':
            users = get_all_users()
            
        elif action == 'ViewTechnicians':
            technicians = get_all_techs()

        elif action == "ViewAppointments":
            appoints = get_all_appointments()

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
    else:
        bookings = get_all_bookings()

    return render_template(
        'view_all.html', 
        bookings=bookings, 
        users=users, 
        technicians=technicians,
        appoints=appoints
    )



@app.route('/create_booking_page', methods=['GET', 'POST'])
def create_booking_page():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        address = request.form.get('address')
        date = request.form.get('date')
        time = request.form.get('time')
        booking_type = request.form.get('bookingType')
        booking_status = request.form.get('bookingStatus')
        tech_id = request.form.get('techID')

        create_booking(user_id, address, date, time, booking_type, booking_status, tech_id)
    return render_template('create_booking.html')



@app.route('/view_specific', methods=['GET', 'POST'])
def view_specific():
    booking = None
    user = None
    tech = None
    appoint = None

    if request.method == 'POST':
        id_input = request.form.get('idInput')
        entity_type = request.form.get('entityType')

        if entity_type == 'Booking':
            booking = get_booking_by_id(id_input)
        elif entity_type == 'User':
            user = get_user_by_id(id_input)
        elif entity_type == 'Technician':
            tech = get_tech_by_id(id_input)
        elif entity_type == 'Appointment':
            appoint = get_appoint_by_id(id_input)
            
    return render_template(
        'view_specific.html', 
        booking=booking, 
        user=user, 
        tech=tech,
        appoint=appoint
    )


@app.route('/carbon_calc', methods=['GET', 'POST'])
def carbon_calc():
    result = None
    score = None

    if request.method == 'POST':
        tranportMethod = request.form.get('transportMethod')
        transportAmount = int(request.form.get('transportAmount'))
        Ev = request.form.get('EV')
        renewType = request.form.get('renewableType')
        lights = request.form.get('lights')
        heating = request.form.get('heating')
        takeawayFreq = request.form.get('takeawayFreq')
        foodType = request.form.get('foodType')

        temp = calculate_carbon_footprint(tranportMethod, transportAmount, Ev, renewType, lights, heating, takeawayFreq, foodType)
        result = temp[0]
        score = temp[1]

    return render_template(
        'carbon_calc.html',
        result=result,
        score=score
        )

if __name__ == '__main__':
    start_database()
    app.run(debug=True)


