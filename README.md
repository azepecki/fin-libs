# fin-libs
Financial analytics toolkit

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) ![Issues](https://img.shields.io/github/issues/azepecki/fin-libs)
[![Build Status](https://github.com/ColumbiaOSS/example-project-python/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/azepecki/fin-libs/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/azepecki/fin-libs/branch/main/graph/badge.svg)](https://codecov.io/gh/azepecki/fin-libs)
[![PyPI](https://img.shields.io/pypi/v/fin-libs)](https://pypi.org/project/fin-libs/)
[![Docs](https://inch-ci.org/github/dwyl/hapi-auth-jwt2.svg?branch=master)](https://azepecki.github.io/fin-libs/)
![Releases](https://img.shields.io/github/v/release/azepecki/fin-libs)


## Overview

Python library that exposes tools for financial analytics. This includes functions to:
- calculate simple and compound interest
- compound annual growth rate 
- weighted average
- linear least squares
- earning per share
- net income

## Installation

This library can be installed by running `pip install fin_libs`. This will pull the latest version of the library.

## Usage

This library is meant to be used for financial analytics purposes. You can import specific functionality from modules in the library. Example usage of each module can be found at the documentation site linked above.

### Example

```
import fin_libs
rate = fin_libs.compound_annual_growth_rate.calculate_compound_annual_growth_rate(71, 100, 4)
```