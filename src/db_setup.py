from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x18$*\xff!\t\x17\x01\xa5r9\x11a{\xc7\xcb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/smart_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SmartFileMetaData(db.Model):
    smart_file_generation_number = db.Column(db.String(8), primary_key=True)
    company_id = db.Column(db.String(), unique=False, nullable=False)
    file_creation_datetime = db.Column(db.DateTime, unique=False, nullable=False)
    file_received_datetime = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    data_from_file_row = db.Column(db.Integer, nullable=False)
    smart_file_readings = db.relationship('SmartFileReadingsData', backref='smart_file_generation_number',
                                          lazy=True)

    def __repr__(self):
        return f"Smart_file_readings_data('{self.smart_file_generation_number}', '{self.company_id}'," \
               f" '{self.file_creation_datetime}', '{self.file_received_datetime}', '{self.data_from_file_row}'"

class SmartFileReadingsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meter_number = db.Column(db.String(9), unique=False, nullable=False)
    measurement_datetime = db.Column(db.DateTime, unique=False, nullable=False)
    consumption = db.Column(db.Float, unique=False, nullable=False)
    data_from_file_row = db.Column(db.Integer, nullable=False)
    smart_file_generation_number = db.Column(db.String(8),
                                             db.ForeignKey('smart_file_meta_data.smart_file_generation_number'),
                                             nullable=False)

    def __repr__(self):
        return f"Smart_file_readings_data('{self.smart_file_generation_number}', '{self.meter_number}'," \
               f" '{self.measurement_datetime}', '{self.consumption}', '{self.data_from_file_row}',"


if __name__ == '__main__':
    main()
