"""
Library module to compute net income
"""
import pandas
from helpers import _fetch_df

"""
Calculate net income

Args:
        csv_file_path(str): expect csv_file_path to have column with
                 positive and negative values for money in & out
        col_name(str): name of the column
Returns:
        net_income(float)
"""


def calculate_net_income(csv_file_path, col_name):
    df = _fetch_df(csv_file_path)
    amounts = df[col_name]
    return sum(amounts)
