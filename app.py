# flask_web/app.py

from flask import Flask
from  genie.testbed import load
from pprint import pprint
from pyats.topology import loader
from genie.utils import Dq
import pandas as pd
from tabulate import tabulate
import time


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
