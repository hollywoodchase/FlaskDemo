from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database connection
db = pymysql.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="bigNsmall",  # Replace with your MySQL password
    database="DB_Conference"  # Replace with your database name
)

@app.route('/')
def home():
    return render_template('index.html')

# Route for Countries table
@app.route('/countries')
def countries():
    cursor = db.cursor()
    cursor.execute("SELECT Country_ID, Country_Name FROM Countries")
    countries = cursor.fetchall()
    cursor.close()
    return render_template('countries.html', countries=countries)

# Route for Participants table
@app.route('/participants')
def participants():
    cursor = db.cursor()
    cursor.execute("""
        SELECT Participant_id, first_name, mid_name, last_name, company, address1, city, state, zip, Country_ID, Role_ID
        FROM Participants
    """)
    participants = cursor.fetchall()
    cursor.close()
    return render_template('participants.html', participants=participants)

# Route for Credit Card table
@app.route('/credit_cards')
def credit_card():
    cursor = db.cursor()
    cursor.execute("SELECT Credit_Card_ID, Participant_ID, Credit_Card_Number FROM Credit_Card")
    credit_cards = cursor.fetchall()
    cursor.close()
    return render_template('credit_cards.html', credit_cards=credit_cards)

# Route for Rooms table
@app.route('/rooms')
def rooms():
    cursor = db.cursor()
    cursor.execute("SELECT Rooms_ID, Room_Name, Rental_Fee, Maximum_Capacity, Projector, SmartBoard FROM Rooms")
    rooms = cursor.fetchall()
    cursor.close()
    return render_template('rooms.html', rooms=rooms)

# Route for Sessions table
@app.route('/sessions')
def sessions():
    cursor = db.cursor()
    cursor.execute("""
        SELECT Session_ID, Rooms_ID, Session_Mgr_ID, Subject_ID, Session_Date, Session_Time, Topic, Session_Fee
        FROM Sessions
    """)
    sessions = cursor.fetchall()
    cursor.close()
    return render_template('sessions.html', sessions=sessions)

if __name__ == '__main__':
    app.run(debug=True)
