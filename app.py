from django.contrib.sites import requests
from flask import Flask

app = Flask(__name__)

API_URL = ''

@app.route('/')
def index():
    roles = requests.get(f'{API_URL}/roles/')
    roles = roles.json()
    print(roles)
    return render_template('index.html', roles=roles)