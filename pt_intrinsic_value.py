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

def get_pt_intrinsic_value(data):     
    """
    Less than 1 Overvalued
    Close to 1 - 1.5 Fairly Valued
    Close to 2 Under Valued
    Clost to 3 Very Under Valued. 
    """
    feps = data['forwardEps']
    teps = data['trailingEps']
    future_eps_growth = (feps / teps) - 1
    dividend_yield = data.get('dividendYield', 0) * 100 
    pe_ratio = data.get('trailingPE', data.get('forwardPE'))

    fy_eps_dy = future_eps_growth + dividend_yield
    result = fy_eps_dy / pe_ratio
    return result

tickers = ['VZ']
for t in tickers:
    data = get_data(t)
    value = get_pt_intrinsic_value(data)
    print(f"{t} value {value}")