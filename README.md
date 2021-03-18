# Hawaii Climate Analysis

These visualizations use Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. The following analysis uses SQLAlchemy ORM queries, Pandas, and Matplotlib.


The data is provided in sqlite format.   hawaii.sqlite  


The webpage runs on  Flask.

List all routes that are available.
/api/v1.0/precipitation
Convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.
/api/v1.0/stations
Return a JSON list of stations from the dataset.
/api/v1.0/tobs
Query the dates and temperature observations of the most active station for the last year of data.
Return a JSON list of temperature observations (TOBS) for the previous year.
/api/v1.0/<start> and /api/v1.0/<start>/<end>


To run navigate to the folder in terminal and run the command python app.py.  Use the routes above, which also appear on the home page to navigate to the different pages and info.   For start and end enter date between 2016 and 2018.




