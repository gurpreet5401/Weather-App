from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    api_key = 'YOUR_API_KEY'
    api_url = 'https://api.openweathermap.org/data/2'
