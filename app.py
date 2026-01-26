import os
import sqlite3
from flask import Flask, request, render_template
from setupDB import start_database
from queries.users_queries import get_all_users, get_user_by_id, create_user, delete_user
from queries.bookings_queries import get_all_bookings, get_booking_by_id, create_booking, delete_booking
from queries.technician_queries import get_all_techs, get_tech_by_id, create_tech, delete_tech

app = Flask(__name__, static_folder='./static')


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/view_all', methods=['GET', 'POST'])
def view_all():
    bookings = None
    users = None
    technicians = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'ViewBookings':
            bookings = get_all_bookings()
            
        elif action == 'ViewUsers':
            users = get_all_users()
            
        elif action == 'ViewTechnicians':
            technicians = get_all_techs()

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
    else:
        bookings = get_all_bookings()

    return render_template(
        'view_all.html', 
        bookings=bookings, 
        users=users, 
        technicians=technicians
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



if __name__ == '__main__':
    start_database()
    app.run(debug=True)


