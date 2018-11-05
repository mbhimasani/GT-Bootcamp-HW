import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"- When given the start and the end date (YYYY-MM-DD), calculate the MIN/AVG/MAX temperature for dates between the start and end date inclusive<br/>"

@app.route("/api/v1.0/precipitation")
def precipitation():
    #Query for the dates and temperature observations from the last year
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    last_year_info = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year).all()

    #Convert the query results to a Dictionary using date as the key and tobs as the value
    all_precipitation = []
    for precipitation in last_year_info:
        precipitation_dict = {}
        precipitation_dict["date"] = precipitation.date
        precipitation_dict["prcp"] = precipitation.prcp
        all_precipitation.append(precipitation_dict)
   #Return the JSON representation of your dictionary
    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.name, Station.station)
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Return a JSON list of Temperature Observations (tobs) for the previous year.
    last_yr_tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= last_year).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_tobs = []
    for tobs in last_yr_tobs:
        tobs_dict = {}
        tobs_dict["date"] = tobs.date
        tobs_dict["tobs"] = tobs.tobs
        all_tobs.append(tobs_dict)
   #Return the JSON representation of your dictionary
    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def trip1(start):

    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    trip1_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    trip1 = list(np.ravel(trip1_data))
    return jsonify(trip1)

@app.route("/api/v1.0/<start>/<end>")
def trip2(start,end):

    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    end_date= dt.datetime.strptime(end,'%Y-%m-%d')
    trip2_data = session.query(func.min(Measurements.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    trip2 = list(np.ravel(trip2_data))
    return jsonify(trip2)

if __name__ == '__main__':
    app.run(debug=True)
