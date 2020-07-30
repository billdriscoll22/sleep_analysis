from typing import List, Tuple

COLUMN_NAME_MAPPINGS = {
    'Steps': 'steps',
    'Alertness  (0=desperately, disgustingly tired, 1= exhausted, 2=dozing off, 3=a little sleepy, 4=normal, fine, 5=energetic) ': 'alertness',
    'Total Sleep Duration': 'sleep_duration',
    'Time to sleep': 'time_to_sleep',
    'Bedtime': 'bed_time',
    'Sleep time Converted': 'sleep_time',
    'Time in Bed': 'time_in_bed',
    'How tired? (0 = Completely wired, 1 = energetic, 2 = normal day as if it were not time for bed, 2.5 = relaxed but not particularly tired, 3 = sleepy but not tired, 4 = a bit tired, 5 = exhausted': 'how_tired',
    'Sun Durations': 'sun_duration',
    'Cumulative Exercise': 'cumulative_exercise',
    'Caffeine Amounts': 'caffeine',
    'Happiness': 'happiness',
    'Total Time Attempting to Sleep': 'total_time_attempting_to_sleep',
    'Food Sleep Difference': 'food_sleep_difference',
    'Wakeup Time': 'wakeup_time',
    'Weather Type': 'is_sunny',
    'Woken up by alarm': 'woken_up_by_alarm',
    'Awoken during dream': 'awoken_during_dream',
    'Nighttime Wakeup Durations': 'nighttime_wakeup_durations',
    'Creatine Amounts': 'creatine_amount',
    'Prev day caff amount': 'prev_day_caffeine_amount',
    'Diff between yesterday and two days ago': 'prev_day_caffeine_amount_difference',
    'Sugar Consumption': 'sugar_consumption',
    'Phone in Bed': 'phone_in_bed',
    'Pre-bed darkness': 'pre_bed_darkness',
    'Bedtime Converted': 'bedtime',
}

COMBINED_COLUMNS: List[Tuple[str, str]] = []

CSV_PATH = '/Users/bill/Projects/sleep/data/sleep.csv'

OR_COLUMNS: List[Tuple[str, str]] = []

PREV_COLUMNS = ['steps',
                'time_to_sleep',
                'how_tired',
                'cumulative_exercise',
                'food_sleep_difference',
                'wakeup_time',
                'creatine_amount',
                'sugar_consumption',
                'phone_in_bed',
                'sun_duration',
                'pre_bed_darkness',
                'sleep_time',
                'bedtime']

PREV_DAY_PREFIX = 'prev_day'
