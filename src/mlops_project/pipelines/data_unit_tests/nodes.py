"""
This is a boilerplate pipeline 'data_unit_tests'
generated using Kedro 0.19.5
"""
import pandas as pd
import great_expectations as ge
import logging

def validate_data(data: pd.DataFrame) -> None:
    # Convert the pandas DataFrame to a Great Expectations DataFrame
    pd_df_ge = ge.from_pandas(data)

    # Define the expected number of columns
    assert pd_df_ge.expect_table_column_count_to_equal(12).success, "Column count does not match expected value"

    # Define the columns to check for existence
    expected_columns = [
        'age', 'sex', 'chest pain type', 'resting bp s', 'cholesterol',
        'fasting blood sugar', 'resting ecg', 'max heart rate', 'exercise angina',
        'oldpeak', 'ST slope', 'target'
    ]

    # Check if each expected column exists
    for column in expected_columns:
        assert pd_df_ge.expect_column_to_exist(column).success, f"Column {column} does not exist"

    # Define expected data types for each column
    expected_types = {
        'age': 'int',
        'sex': 'int',
        'chest pain type': 'int',
        'resting bp s': 'int',
        'cholesterol': 'int',
        'fasting blood sugar': 'int',
        'resting ecg': 'int',
        'max heart rate': 'int',
        'exercise angina': 'int',
        'oldpeak': 'float',
        'ST slope': 'int',
        'target': 'int'
    }

    # Check the data type of each column
    for column, expected_type in expected_types.items():
        assert pd_df_ge.expect_column_values_to_be_of_type(column, expected_type).success, f"{column} is not of type {expected_type}"

    # Check for missing values in critical columns
    critical_columns = ['age', 'sex', 'chest pain type', 'resting bp s', 'cholesterol', 'max heart rate', 'target']
    for column in critical_columns:
        assert pd_df_ge.expect_column_values_to_not_be_null(column).success, f"Column {column} contains null values"



    # Check categorical columns contain only expected values
    expected_values = {
        'sex': [0, 1],
        'chest pain type': [1, 2, 3, 4],
        'fasting blood sugar': [0, 1],
        'exercise angina': [0, 1],
        'target': [0, 1]
    }

    for column, values in expected_values.items():
        assert pd_df_ge.expect_column_values_to_be_in_set(column, values).success, f"Column {column} contains unexpected values"

    log = logging.getLogger(__name__)
    log.info("Data passed the unit tests")

    print("Data validation passed")



