import fin_libs
import pytest
import pandas
from unittest.mock import Mock, patch


@pytest.mark.parametrize("first,last,years,expected", [(71, 100, 4, 8.940), (2000, 10000, 5, 37.973)])
def test_calculate_compound_annual_growth_rate(first, last, years, expected):
    actual = fin_libs.calculate_compound_annual_growth_rate(first, last, years)
    assert expected == round(actual, 3)


def test_calculate_compound_annual_growth_rate_error():
    with pytest.raises(Exception) as e:
        fin_libs.calculate_compound_annual_growth_rate(1, 2, 0)


@patch("yfinance.Ticker")
@pytest.mark.parametrize("ticker,expected", [("AAPL", 2), ("TSLA", 3)])
def test_calculate_dividend_rate(mock_yfinance, ticker, expected):
    mock_yfinance.return_value.info = {"dividendRate": expected}
    actual = fin_libs.calculate_dividend_rate(ticker)
    assert actual == expected


@patch("yfinance.Ticker")
@pytest.mark.parametrize("ticker,expected", [("AAPL", 2), ("TSLA", 3)])
def test_calculate_dividend_yield(mock_yfinance, ticker, expected):
    mock_yfinance.return_value.info = {"dividendYield": expected}
    actual = fin_libs.calculate_dividend_yield(ticker)
    assert actual == expected


@patch("yfinance.Ticker")
@pytest.mark.parametrize("ticker,expected", [("AAPL", 2), ("TSLA", 3)])
def test_calculate_eps(mock_yfinance, ticker, expected):
    mock_yfinance.return_value.info = {"forwardEps": expected}
    actual = fin_libs.calculate_eps(ticker)
    assert actual == expected


@patch("pandas.read_csv")
@pytest.mark.parametrize("values,expected", [([1, 2, 3, 4, 5], 15), ([5, 7, 3, 2], 17)])
def test_calculate_eps(mock_pandas, values, expected):
    mock_pandas.return_value = {"col": values}
    actual = fin_libs.calculate_net_income("test", "col")
    assert actual == expected


@pytest.mark.parametrize("principal,rate,time,expected", [(100, 5, 2, 10.25), (5000, 5, 50, 52337.00)])
def test_calculate_compound_interest(principal, rate, time, expected):
    actual = fin_libs.calculate_compound_interest(principal, rate, time)
    assert round(actual, 2) == expected


@pytest.mark.parametrize("principal,rate,time,expected", [(100, 5, 2, 10), (5000, 5, 50, 12500)])
def test_calculate_simple_interest(principal, rate, time, expected):
    actual = fin_libs.calculate_simple_interest(principal, rate, time)
    assert actual == expected


@patch("yfinance.Ticker")
@pytest.mark.parametrize("ticker,expected", [("AAPL", 2), ("TSLA", 3)])
def test_calculate_price_to_book_value(mock_yfinance, ticker, expected):
    mock_yfinance.return_value.info = {"bookValue": expected}
    actual = fin_libs.calculate_price_to_book_value(ticker)
    assert actual == expected