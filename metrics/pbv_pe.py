import yfinance as yf
import json 
from pathlib import Path
from os import environ
from datetime import datetime

def get_pbv_mulitplier(data):     
    """
    If a stock pe * pbv < 22.5 it is undervalued 
    """
    pbv = {'fep_pbv': 0,
            'tep_pbv': 0}
    ocf = data['operatingCashflow']
    operating_cf = int(ocf)

    if operating_cf > 0:
        pricetobook = data['priceToBook']
        if data.get('trailingEps', None):
            teps = data['trailingEps']
            tep_pbv = teps * pricetobook 
            pbv['tep_pbv'] = tep_pbv
        if data.get('forwardEps', None):
            feps = data['forwardEps']
            pbv['fep_pbv'] = feps * pricetobook 

    return pbv
