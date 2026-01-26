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

    return render_template(
        'view_all.html', 
        bookings=bookings, 
        users=users, 
        technicians=technicians
    )




@app.route('/create_booking', methods=['GET', 'POST'])
def create_booking():
    return render_template('create_booking.html')



if __name__ == '__main__':
    start_database()
    app.run(debug=True)


