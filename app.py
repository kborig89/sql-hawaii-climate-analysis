import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect


from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session=Session(engine)
app = Flask(__name__)


@app.route("/")
def welcome():
    return (
        f"Welcome to SQLalchemy challenge API! We are looking at Hawaii precipitation<br/>"
        f"Available Routes are below:<br/>"
        f"Precipitation data by date can be found at /api/v1.0/precipitation<br/>"
        f"List of stations can be found at /api/v1.0/stations<br/>"
        f"List of tobs can be found at /api/v1.0/tobs<br/>"
        f"Statistics from the start date in format (yyyy-mm-dd) type / and date after temp: /api/v1.0/temp/<start><br/>"
        f"Statistics from the start date thru the end date / and date after temp:  /api/v1.0/temp/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    year_ago=dt.date(2017,8,23)-dt.timedelta(days=365)

    data=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=year_ago).all()
    precipitation={date:prcp for date,prcp in data}

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    
    results=session.query(Station.station).all()
    stations= list(np.ravel(results))

    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def tobs():
    year_ago=dt.date(2017,8,23)-dt.timedelta(days=365)
    temp_obv=session.query(Measurement.tobs).filter(Measurement.station=='USC00519281').\
    filter(Measurement.date>=year_ago).all()
    temps= list(np.ravel(temp_obv))

    return jsonify(temps)


@app.route("/api/v1.0/temp/<start>")
def stats(start):
   
    results=session.query(func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
    filter(Measurement.date>=start).all()
    temps= list(np.ravel(results))

    return jsonify(temps)

@app.route("/api/v1.0/temp/<start>/<end>")
def stats2(start,end):
   
    results=session.query(func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
    filter(Measurement.date>=start).\
    filter(Measurement.date<= end).all()
    temps= list(np.ravel(results))

    return jsonify(temps)


if __name__ == "__main__":
    app.run(debug=True)