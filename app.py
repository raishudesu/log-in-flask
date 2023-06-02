from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__,  template_folder='templateFiles', static_folder='staticFiles')
CORS(app)