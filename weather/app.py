from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = ''  

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        print(f"City entered: {city}")
        weather_data = get_weather(city)
        print(f"Weather data: {weather_data}")
        if weather_data is None:
            error_message = "City not found. Please try again."
            return render_template('index.html', error=error_message)
    return render_template('index.html', weather=weather_data)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(f"API Response: {data}")
    if data.get('cod') == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
