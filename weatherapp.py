from flask import Flask, render_template, request


import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def weather():
    cityname = request.form['city']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+',us&appid=1a81752c52f1c658f56beb862f5a8dfd')
    data = r.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    
    return render_template('parameters.html',temp=temp, humidity=humidity)
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
