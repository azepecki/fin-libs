__version__ = '0.1.0'

from .compound_annual_growth_rate import calculate_compound_annual_growth_rate
from .dividends import calculate_dividend_rate, calculate_dividend_yield
from .eps import calculate_eps
from .income import calculate_net_income
from .interest.compound import calculate_compound_interest
from .interest.simple import calculate_simple_interest
from .linear_least_squares import do_linear_least_squares_regression, plot_linear_least_squares_regression
from .price import calculate_price_to_earning, calculate_price_to_book_value
from .weighted_average import compute_weighted_average
