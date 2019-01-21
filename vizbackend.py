from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import pandas as pd
import numpy as np

app = Flask(__name__)


def all_locations_median(day, start_hour, end_hour):
    locations = pd.read_csv("locations.csv")
    pickup_times =pd.read_csv("pickup_times.csv")

    #Format
    #2019-01-13T19:00Z
    #2019-01-13T20:00Z

    start = "" + day + "T" + start_hour + "Z"
    end = "" + day + "T" + end_hour + "Z"

    pickup_times_slice = pickup_times[(pickup_times['iso_8601_timestamp'] > start) 
    & (pickup_times['iso_8601_timestamp'] <= end)]

    pickup_times_by_location = pickup_times_slice.groupby('location_id')
    location_medians = pickup_times_by_location['pickup_time'].median()

    location_indexes = location_medians.index.values
    location_medians = location_medians

    location_medians_with_index = pd.DataFrame(data={'location_id': location_indexes, 'median': location_medians},
     columns=['location_id', 'median'])
    
    joined = location_medians_with_index.merge(locations, left_on='location_id', right_on='location_id', how='outer')

    return joined.to_json(orient='columns')

@app.route('/')
def location_page():
    return render_template('locationviz.html')


@app.route('/visualizationdata', methods=['GET'])
def update_visualization():
    day = request.args.get('day-selected')
    start_time = request.args.get('start-time')
    end_time = request.args.get('end-time')

    if day != None and start_time != None and end_time != None:
        return all_locations_median(day, start_time,end_time)
    
    else:
        return all_locations_median("2019-01-07", "15:00","16:00")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)