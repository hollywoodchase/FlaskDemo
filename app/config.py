import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bigNsmall@localhost/DB_Conference'  # Change as needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Environment variable for security
