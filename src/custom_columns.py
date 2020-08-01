from typing import Any


# Don't know how to get a "row" typing from pandas
def wakeup_time_difference_from_prev(row: Any) -> float:
    """
    Return difference between today and yesterday's wakeup times

    :param row: Row in a pandas Dataframe

    :return float: Difference between today and yesterday's wakeup times
    """

    return row['wakeup_time'] - row['prev_day_wakeup_time']


CUSTOM_COLUMNS = [('wakeup_time_difference_from_prev',
                   wakeup_time_difference_from_prev)]
