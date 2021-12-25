from  genie.testbed import load
from pprint import pprint
from pyats.topology import loader
from genie.utils import Dq
import pandas as pd
from tabulate import tabulate
import time

tb = loader.load('/var/mgtsservice/MGTS.yaml')

