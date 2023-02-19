"""
Helper function to create a pandas dataframe from a CSV file
"""
import pandas
import yfinance as yf

def _fetch_df(csv_file_path):
        df = pandas.read_csv(csv_file_path)
        return df

def _fetch_ticker(ticker):
        tick = yf.Ticker(ticker)
        return tick
