import os
import sqlite3
from flask import Flask, request, render_template
from setupDB import start_database

app = Flask(__name__, static_folder='./static')


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/view_all')
def view_all():
    return render_template('view_all.html')



@app.route('/create_booking', methods=['GET', 'POST'])
def create_booking():
    return render_template('create_booking.html')



if __name__ == '__main__':
    start_database()
    app.run(debug=True)


