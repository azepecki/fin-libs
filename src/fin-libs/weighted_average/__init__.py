"""
Library package to compute the weighted average
"""
import numpy
import pandas
from helpers import _fetch_df


"""
Compute weighted average 

Args:
        csv_file_path(str): file path string
        distr_col(str): column name for distribution
        weights_col(str): column name for weights
Returns:
        int: weighted average
"""


def compute_weighted_average(csv_file_path, distr_col, weights_col):
    df = _fetch_df(csv_file_path)
    distribution = df[distr_col]
    weights = df[weights_col]
    return _compute_weighted_average(distribution, weights)


"""
Helper function to calculate weighted average
"""


def _compute_weighted_average(distribution, weights):
    return round(sum([distribution[i] * weights[i] for i in range(len(distribution))] / sum(weights), 2))
