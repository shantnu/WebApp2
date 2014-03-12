from flask import Flask

app = Flask(__name__)
from app import views

app.config.from_object('config')
app.config.from_object('config_sec')