import yfinance as yf
import json 
from pathlib import Path
from os import environ
from datetime import datetime


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
