import requests

from flask import Flask, render_template

app = Flask('widget')

@app.route('/')
def hello_world():
  prices = requests.get('https://api.porssisahko.net/v1/latest-prices.json').json()
  return render_template('index.html', prices=prices)

if __name__ == '__main__':
  app.run(port=8000, host='0.0.0.0')