from compound_annual_growth_rate import calculate_compound_annual_growth_rate
import pytest


@pytest.mark.parametrize("first,last,years,expected"[(71, 100, 4, 8.9395), (2000, 10000, 5, 37.973)])
def test_compound_annual_growth_rate(first, last, years, expected):
    actual = calculate_compound_annual_growth_rate(first, last, years)
    assert expected == actual
