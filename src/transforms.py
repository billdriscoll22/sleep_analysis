from math import isnan


def clock_to_minutes(clock: str) -> float:
    try:
        hours_raw, minutes_raw = clock.split(':')

        hours = float(hours_raw)
        minutes = float(minutes_raw)

        return (hours * 60 + minutes) / 60
    except Exception:
        return float('nan')


def presence_of_value(val: str) -> float:
    if (isinstance(val, str)):
        return 1.0

    if isnan(val):
        return 0.0

    return 1.0


def weather_to_is_sunny(val: str) -> float:
    if val in ['Sunny', 'sunny', 'Mostly Sunny', 'Mostly sunny', 'mostly Sunny']:
        return 1.0

    if val == 'N/A':
        return float('nan')

    if isinstance(val, str):
        return 0.0

    if isnan(val):
        return val

    raise Exception('Unknown weather val')


def y_n_to_1_0(val: str) -> float:
    if val in ['Y', 'Yes', 'yes', 'y']:
        return 1.0

    if val in ['N', 'No', 'no', 'n']:
        return 0.0

    if isinstance(val, str):
        print(val)
        raise Exception('Unknown YN String')

    if isnan(val):
        return val

    raise Exception('Unknown YN type')


def range_to_float(val: str) -> float:
    if isinstance(val, float):
        if isnan(val):
            return val

    low_raw, high_raw = val.split('-')

    low = float(low_raw)
    high = float(high_raw)

    return (low + high) / 2.0


TRANSFORMS = [('sleep_duration', clock_to_minutes),
              ('prev_day_time_to_sleep', clock_to_minutes),
              ('total_time_attempting_to_sleep', clock_to_minutes),
              ('prev_day_food_sleep_difference', clock_to_minutes),
              ('wakeup_time', clock_to_minutes),
              ('prev_day_wakeup_time', clock_to_minutes),
              ('is_sunny', weather_to_is_sunny),
              ('woken_up_by_alarm', y_n_to_1_0),
              ('awoken_during_dream', y_n_to_1_0),
              ('nighttime_wakeup_durations', clock_to_minutes),
              ('prev_day_phone_in_bed', y_n_to_1_0),
              ('prev_day_pre_bed_darkness', y_n_to_1_0),
              ('prev_day_sleep_time', clock_to_minutes),
              ('prev_day_bedtime', clock_to_minutes)]
