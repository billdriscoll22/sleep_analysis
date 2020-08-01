from math import isnan
from typing import Any, Callable, Dict, List, Tuple

import pandas as pd
import seaborn as sns

from constants import (COLUMN_NAME_MAPPINGS, COMBINED_COLUMNS, CSV_PATH,
                       OR_COLUMNS, PREV_COLUMNS, PREV_DAY_PREFIX)
from custom_columns import CUSTOM_COLUMNS
from filters import FILTERS
from transforms import TRANSFORMS


def calculate_correlation(ind: str, dep: str, df: pd.DataFrame) -> None:
    """
    Output a Pearson correlation coefficient and scatterplot for two given variables

    :param ind: Independent variable (can be arbitrary)
    :param dep: Dependent variable (can be arbitrary)
    :param df: DataFrame
    """

    ind_dep_filters = [(ind, FILTERS[ind]), (dep, FILTERS[dep])]

    for ind_dep_filter in ind_dep_filters:
        column_name, filters = ind_dep_filter

        for filter in filters:
            df = df[df.apply(lambda row: filter(row[column_name]), axis=1)]

    coeff = df[ind].corr(df[dep])
    print('Correlation Coefficient: ', coeff)

    sns.lmplot(x=ind, y=dep, data=df, fit_reg=True)


def add_custom_columns(custom_columns: List[Tuple[str, Callable[[Any], Any]]], df: pd.DataFrame) -> None:
    """
    Add caller-defined columns to a DataFrame

    :param custom_columns: A list of column-name/column-generator-function pairs
    :param df: DataFrame
    """

    for custom_col_name, generate_custom_col in custom_columns:
        df[custom_col_name] = df.apply(
            lambda row: generate_custom_col(row), axis=1)


def add_or_columns(or_columns: List[Tuple[str, str]], df: pd.DataFrame) -> None:
    """
    Insert 'or' columns into dataframe, whereby value is 1.0 if any user-defined column
    has a non-zero value and 0.0 otherwise

    :param or_columns: A list of column name pairs
    :param df: DataFrame
    """

    for or_column_pair in or_columns:
        first_col, second_col = or_column_pair

        def or_func(row):
            return 1.0 if row[first_col] + row[second_col] > 0.0 else 0.0

        new_column_name = f'{first_col}_or_{second_col}'

        df[new_column_name] = df.apply(or_func, axis=1)


def transform_vals(transforms: List[Tuple[str, Callable[[Any], Any]]], df: pd.DataFrame) -> None:
    """
    Apply caller-defined transforms to DataFrame columns

    :param transforms: A list of column-name/transform-function pairs
    :param df: Dataframe
    """
    for col_name, transform in transforms:
        df[col_name] = df.apply(lambda row: transform(row[col_name]), axis=1)


def add_combined_columns(combined_columns: List[Tuple[str, str]], df: pd.DataFrame) -> None:
    """
    Create new DataFrame columns whose values are the sum of user-defined constituent column pairs

    :param combined_columnss: A list of column-name pairs
    :param df: DataFrame
    """

    for combined_column_pair in combined_columns:
        first_col, second_col = combined_column_pair

        new_column_name = f'{first_col}_{second_col}'
        df[new_column_name] = df[first_col] + df[second_col]


def get_prev_day_key(key: str) -> str:
     """
     Get previous-day column name for given column name

    :param key: Column name

    :return str: Corresponding previous-day column name
    """

    return f'{PREV_DAY_PREFIX}_{key}'


def add_prev_column(column_name: str, df: pd.DataFrame) -> None:
    """
    Create previous-day column for given column

    :param column_name: Name of column for which to create a previous-day column
    :param df: DataFrame
    """

    new_column_name = get_prev_day_key(column_name)
    df[new_column_name] = df[column_name].shift(1)


def add_prev_columns(column_names: List[str], df: pd.DataFrame) -> None:
    """
    Create previous-day columns for given columns

    :param column_names: List of names of columns for which to create previous-day columns
    :param df: DataFrame
    """

    for column_name in column_names:
        add_prev_column(column_name, df)


def transform_column_names(df: object, column_names: Dict[str, str]) -> None:
    """
    Rename user-designated columns

    :param df: DataFrame
    :param column_names: Dict mapping old column names to new ones 
    """

    return df.rename(columns=column_names)


def read_data(path: str) -> pd.DataFrame:
    """
    Parse CSV into pandas Dataframe

    :param path: Path to CSV file
    
    :return pd.DataFrame: pandas DataFrame
    """

    return pd.read_csv(path, encoding='unicode_escape')


def main():
    """
    Read CSV data, apply various data transformations, and calculate correlation between column-pair values
    """

    pd.set_option('display.max_columns', 500)
    pd.set_option('display.max_rows', 500)

    sleep_df_raw_column_names = read_data(CSV_PATH)
    sleep_df = transform_column_names(
        sleep_df_raw_column_names, COLUMN_NAME_MAPPINGS)

    add_prev_columns(PREV_COLUMNS, sleep_df)
    add_combined_columns(COMBINED_COLUMNS, sleep_df)
    transform_vals(TRANSFORMS, sleep_df)
    add_or_columns(OR_COLUMNS, sleep_df)
    add_custom_columns(CUSTOM_COLUMNS, sleep_df)

    calculate_correlation('prev_day_steps',
                          'alertness', sleep_df.copy())


main()
