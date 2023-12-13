"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template, request
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ciao'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend

class WineSearchForm(FlaskForm):
    vintage_min = IntegerField('Vintage Min', validators=[DataRequired()])
    vintage_max = IntegerField('Vintage Max', validators=[DataRequired()])
    submit = SubmitField('Search Wines')


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Fetch the date from the backend
    date_from_backend = fetch_date_from_backend()
    return render_template('index.html', date_from_backend=date_from_backend)


@app.route('/internal', methods=['GET', 'POST'])
def internal():
    """
    Render the internal page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    form = WineSearchForm()
    wines = None
    error_message = None

    if form.validate_on_submit():
        try:
            response = requests.get(
                f'{FASTAPI_BACKEND_HOST}/get-wines-json/',
                params={
                    'vintage_min': form.vintage_min.data,
                    'vintage_max': form.vintage_max.data
                }
            )
            response.raise_for_status()
            wines = response.json()
        except requests.exceptions.RequestException as e:
            error_message = str(e)
    
    return render_template('internal.html', form=form, wines=wines, error_message=error_message)

def fetch_date_from_backend():
    """
    Function to fetch the current date from the backend.

    Returns:
        str: Current date in ISO format or an error message.
    """
    backend_url = f'{FASTAPI_BACKEND_HOST}/get-date'  # Adjust the URL based on your backend configuration
    try:
        response = requests.get(backend_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('date', 'Date not available')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Date not available'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
