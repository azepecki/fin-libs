"""
Library module to compute compund annual growth rate
"""

"""
Calculate compound annaul growth rate

Args:
        first(float): starting value
        last(float): ending value
        years(int): number of years
"""


def calculate_compound_annual_growth_rate(first, last, years):
    if years < 1:
        raise Exception("Years cannot be less than 1")
    return ((last / first) ** (1 / years) - 1) * 100
