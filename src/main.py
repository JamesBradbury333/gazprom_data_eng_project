from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy


def main():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '\x18$*\xff!\t\x17\x01\xa5r9\x11a{\xc7\xcb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/gazprom_data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class SmartFileReadingsData(db.Model):
        smart_file_generation_number = db.Column(db.String(8), primary_key=True)
        meter_number = db.Column(db.String(9), unique=False, nullable=False)
        measurement_datetime = db.Column(db.DateTime, unique=False, nullable=False)
        consumption = db.Column(db.Float, unique=False, nullable=False)
        data_from_file_row = db.Column(db.Integer, nullable=False)

        def __repr__(self):
            return f"Smart_file_readings_data('{self.smart_file_generation_number}', '{self.meter_number}'," \
                   f" '{self.measurement_datetime}', '{self.consumption}', '{self.data_from_file_row}',"

    class SmartFileMetaData(db.Model):
        smart_file_generation_number = db.Column(db.String(8), primary_key=True)
        company_id = db.Column(db.String(), unique=False, nullable=False)
        file_creation_datetime = db.Column(db.DateTime, unique=False, nullable=False)
        file_received_datetime = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
        data_from_file_row = db.Column(db.Integer, nullable=False)
        # TODO: add relationship to readings_data_table. They should map with smart_file_generation_umbers
        smart_file_number =



        def __repr__(self):
            return f"Smart_file_readings_data('{self.smart_file_generation_number}', '{self.company_id}'," \
                   f" '{self.file_creation_datetime}', '{self.file_received_datetime}', '{self.data_from_file_row}'"


if __name__ == '__main__':
    main()
