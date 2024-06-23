import yfinance as yf
import json 
from pathlib import Path
from os import environ
from datetime import datetime

root_dir_env =  environ.get('root_dir', None)
root = Path(root_dir_env) if root_dir_env else Path(__file__).parent

def get_data(ticker, refresh=False):
 
    datestamp = datetime.now().strftime('%Y%m%d')
    path =  root / 'data' / f'{ticker}_stock_info_{datestamp}.json'

    if not path.exists() or refresh == True:
        stock = yf.Ticker(ticker)
        data = stock.info
        with open(path, 'w') as f:
            f.write(json.dumps(data, indent=4))
        return data
    else:
        with open(path, 'r') as f:
            return json.loads(f.read())

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


tickers = ['CB', 'OXY', 'AAPL', 'AVGO', 'FCEL', 'CVGW', 'YEXT']


tickers = ['ALGM', 'SYNA', 'LSCC', 'ALAB', 'ARM', 'KLAC', 'TXN', 'CRUS', 'WOLF', 'AOSL']
tickers = ['VZ']

for t in tickers:
    data = get_data(t)
    pbv_ratio = get_pbv_mulitplier(data)
    print(f"{t} tep {pbv_ratio['tep_pbv']} fep {pbv_ratio['fep_pbv']} ")
    # value = get_pt_intrinsic_value(data)
    # print(f"{t} value {value}")