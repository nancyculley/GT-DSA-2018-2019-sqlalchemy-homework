## Step 2 - Climate App
# Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
# * Use FLASK to create your routes.
### Routes
# * `/`
#   * Home page.
#  * List all routes that are available.
# * `/api/v1.0/precipitation`
#  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
#  * Return the JSON representation of your dictionary.
# * `/api/v1.0/stations`
#  * Return a JSON list of stations from the dataset.
# * `/api/v1.0/tobs`
#  * query for the dates and temperature observations from a year from the last data point.
#  * Return a JSON list of Temperature Observations (tobs) for the previous year.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
       )


@app.route("/api/v1.0/precipitation")
def precip():
    """convert query results to dictionary using date as key and prcp as value"""
   
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Convert list of tuples into normal list
    results = list(np.ravel(results))

    return jsonify(results)

@app.route("/api/v1.0/stations")
def precip():
    """list stations"""
   
    stations = session.query(Stations.name).all()

    # Convert list of tuples into normal list
    stations = list(np.ravel(stations))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def precip():
    """query for the dates and temperature observations from a year from the last data point"""
   
    results = session.query(Measurement.tobs).filter(Measurement.date >= '2016-08-23').all()

    # Convert list of tuples into normal list
    results = list(np.ravel(results))

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
