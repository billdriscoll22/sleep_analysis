from math import isnan
from typing import Any


def is_int(val: Any) -> bool:
    """
    Ascertain whether or not a given value is an integer

    :param val: Value to be tested

    :return bool: Whether or not the value is an integer
    """

    return isinstance(val, int)


def is_float(val: Any) -> bool:
    """
    Ascertain whether or not a given value is a float

    :param val: Value to be tested

    :return float: Whether or not the value is a float
    """

    return isinstance(val, float)


def is_not_nan(val: Any) -> bool:
    """
    Ascertain whether a given value is 'not nan'

    :param val: Value to be tested

    :return float: Whether or not the value is 'not nan'
    """

    return (not isnan(val))


FILTERS = {
    'steps': [is_float, is_not_nan],
    'prev_day_steps': [is_float, is_not_nan],
    'alertness': [is_float, is_not_nan],
    'sleep_duration': [is_float, is_not_nan],
    'prev_day_time_to_sleep': [is_float, is_not_nan],
    'how_tired': [is_float, is_not_nan],
    'prev_day_how_tired': [is_float, is_not_nan],
    'cumulative_exercise': [is_float, is_not_nan],
    'prev_day_cumulative_exercise': [is_float, is_not_nan],
    'total_time_attempting_to_sleep': [is_float, is_not_nan],
    'food_sleep_difference': [is_float, is_not_nan],
    'prev_day_food_sleep_difference': [is_float, is_not_nan],
    'wakeup_time': [is_float, is_not_nan],
    'prev_day_wakeup_time': [is_float, is_not_nan],
    'wakeup_time_difference_from_prev': [is_float, is_not_nan],
    'is_sunny': [is_float, is_not_nan],
    'woken_up_by_alarm': [is_float, is_not_nan],
    'awoken_during_dream': [is_float, is_not_nan],
    'nighttime_wakeup_durations': [is_float, is_not_nan],
    'prev_day_creatine_amount': [is_float, is_not_nan],
    'prev_day_caffeine_amount': [is_float, is_not_nan],
    'prev_day_caffeine_amount_difference': [is_float, is_not_nan],
    'prev_day_sugar_consumption': [is_float, is_not_nan],
    'prev_day_phone_in_bed': [is_float, is_not_nan],
    'prev_day_sun_duration': [is_float, is_not_nan],
    'prev_day_pre_bed_darkness': [is_float, is_not_nan],
    'prev_day_sleep_time': [is_float, is_not_nan],
    'prev_day_bedtime': [is_float, is_not_nan],
}
