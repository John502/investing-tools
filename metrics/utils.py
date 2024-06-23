import yfinance as yf
import json 
from pathlib import Path
from os import environ
from datetime import datetime

root_dir_env =  environ.get('root_dir', None)
root = Path(root_dir_env) if root_dir_env else Path(__file__).parent.parent
data_dir = root / 'data'
if not data_dir.exists():
    data_dir.mkdir()

def get_data(ticker, refresh=False):
 
    datestamp = datetime.now().strftime('%Y%m%d')
    path =  data_dir / f'{ticker}_stock_info_{datestamp}.json'

    if not path.exists() or refresh == True:
        stock = yf.Ticker(ticker)
        data = stock.info
        with open(path, 'w') as f:
            f.write(json.dumps(data, indent=4))
        return data
    else:
        with open(path, 'r') as f:
            return json.loads(f.read())