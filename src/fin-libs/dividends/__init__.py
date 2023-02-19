"""
Library module to compute dividend information
"""
from helpers import _fetch_ticker_data

"""
Calculate dividend rate

Args:
        ticker(str): name of the ticker
Returns:
        float: dividend rate
"""
def calculate_dividend_rate(ticker):
        tick = _fetch_ticker_data(ticker)
        return tick.info['dividendRate']


"""
Calculate dividend yield

Args:
        ticker(str): name of the ticker
Returns:
        float: dividend yield
"""
def calculate_dividend_yield():
        tick = _fetch_ticker_data(ticker)
        return tick.info['dividendYield']