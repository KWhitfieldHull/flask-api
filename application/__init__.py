from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nlmhboti:bJlZvn0NtV9WK0yd9LimY7AAUUIUwx4M@trumpet.db.elephantsql.com/nlmhboti'
db = SQLAlchemy(app)
from application import routes