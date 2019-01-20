from flask import Flask
from flask import render_template

from flask import jsonify

import pandas as pd
import numpy as np

app = Flask(__name__)


def all_locations_median():
    locations = pd.read_csv("locations.csv")
    pickup_times =pd.read_csv("pickup_times.csv")

    pickup_times_by_location = pickup_times.groupby('location_id')
    location_medians = pickup_times_by_location['pickup_time'].median()

    location_indexes = location_medians.index.values
    location_medians = location_medians #.values.reshape(1,location_medians.shape[0])

    location_medians_with_index = pd.DataFrame(data={'location_id': location_indexes, 'median': location_medians}, columns=['location_id', 'median'])
    
    joined = location_medians_with_index.merge(locations, left_on='location_id', right_on='location_id', how='outer')

    return joined.to_json(orient='split')

@app.route('/')
def hello_world():
    return render_template('locationviz.html')


@app.route('/defaultdata')
def initialize_visualization():
    
    return all_locations_median()



@app.route('/updateddata')
def update_visualization():
    dictionary = {"a": "b", "c" : "d"}
    return jsonify(**dictionary)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)