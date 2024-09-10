"""
times.py

This module provides functions to get the current time in Japan and in a
specified
timezone.
It also provides a function to calculate the time difference between Japan
and a
Country.

This module is intended to be used as a template for applying a linter. 
Create a copy of this module and apply the linter to the copy. 
Afterwards, compare the linted copy to this original file to understand
the
changes made
by the linter.

Functions:
    get_current_time_in_japan: Returns the current time in Japan.
    get_current_time_in_country: Returns the current time in a specified
    timezone.
    calculate_time_difference: Returns the time difference between
    Japan and
    a Country in
    hours.
"""

from datetime import datetime
import pytz

import pandas as pd

def pandas_version():
    """
    Print pandas version.

    Returns:
        string: pandas version.
    """
    print(pd.__version__)

def get_current_time_in_japan():
    """
    Get the current time in Japan.

    Returns:
        datetime: The current time in Japan.
    """
    japan_tz = pytz.timezone('Asia/Tokyo')
    japan_time = datetime.now(japan_tz)
    return japan_time

def get_current_time_in_country(timezone):
    """
    Get the current time in a specified timezone.

    Args:
        timezone (str): The timezone to get the current time for.

    Returns:
        datetime: The current time in the specified timezone.
    """
    specified_tz = pytz.timezone(timezone)
    specified_time = datetime.now(specified_tz)
    return specified_time

def calculate_time_difference():
    """
    Calculate the time difference between Japan and the specified Country.

    Returns:
        int: The time difference between Japan and the specified Country.
    """
    japan_time = get_current_time_in_japan()
    country_time = get_current_time_in_country('Europe/Berlin')

    # Only consider the hour part of the time
    time_difference_in_hours = japan_time.hour - country_time.hour

    # If the result is negative, add 24 to get the correct time difference
    if time_difference_in_hours < 0:
        time_difference_in_hours += 24

    return time_difference_in_hours

if __name__ == '__main__':
    print(get_current_time_in_japan())
    print(get_current_time_in_country('Europe/Berlin'))
    print(f"Time difference in hours: {calculate_time_difference()}")
    
