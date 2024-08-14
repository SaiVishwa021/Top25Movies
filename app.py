from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

# Route to serve the home page with the input form
@app.route('/', methods=['GET', 'POST'])
def index():
    movies_data = None
    error_message = None

    if request.method == 'POST':
        year = request.form.get('year')
        file_path = f'DataSets/IMDB_Top_25_{year}.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                movies_data = json.load(f)
        else:
            error_message = f"No data found for the year {year}. Please try another year between (1950 - present)."

    return render_template('index.html', movies_data=movies_data, error_message=error_message)

