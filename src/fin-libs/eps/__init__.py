"""
Library module to compute earnings per share
"""
from helpers import _fetch_ticker

"""
Calculate Earnings per Share

Args:
        ticker(str): the ticker for which we should calculate the EPS
Returns:
        float: the EPS
"""
def calculate_eps(ticker):
        tick = _fetch_ticker(ticker)
        return tick.info['forwardEps']