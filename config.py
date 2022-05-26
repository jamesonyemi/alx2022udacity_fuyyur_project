import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgresSQL12@localhost:5433/fuyyur_sound_city_db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
