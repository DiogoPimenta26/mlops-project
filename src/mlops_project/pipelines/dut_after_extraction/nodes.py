"""
This is a boilerplate pipeline 'dut_after_extraction'
generated using Kedro 0.19.5
"""

import pandas as pd
import great_expectations as ge
import logging

def validate_data(data: pd.DataFrame) -> None:
    # Convert the pandas DataFrame to a Great Expectations DataFrame
    pd_df_ge = ge.from_pandas(data)

    # Define the expected number of columns
    assert pd_df_ge.expect_table_column_count_to_equal(26).success, "Column count does not match expected value"

    # Define the columns to check for existence
    expected_columns = ['sex','resting bp s','fasting blood sugar','max heart rate',
                        'exercise angina','oldpeak','target', 'age_0-40', 'age_41-50', 'age_51-60',
                        'age_61-70', 'age_71-80', 'cholesterol_borderline high', 'cholesterol_high',
                        'cholesterol_normal', 'chest pain type_1', 'chest pain type_2', 'chest pain type_3',
                        'chest pain type_4', 'resting ecg_0', 'resting ecg_1', 'resting ecg_2', 'ST slope_0',
                        'ST slope_1', 'ST slope_2', 'ST slope_3']
    
    # Check if each expected column exists
    for column in expected_columns:
        assert pd_df_ge.expect_column_to_exist(column).success, f"Column {column} does not exist"

    # Define expected data types for each column 
    expected_data_types = {
        'sex': 'int64',
        'resting bp s': 'int64',
        'fasting blood sugar': 'int64',
        'max heart rate': 'int64',
        'exercise angina': 'int64',
        'oldpeak': 'float64',
        'target': 'int64',
        'age_0-40': 'int64',
        'age_41-50': 'int64',
        'age_51-60': 'int64',
        'age_61-70': 'int64',
        'age_71-80': 'int64',
        'cholesterol_borderline high': 'int64',
        'cholesterol_high': 'int64',
        'cholesterol_normal': 'int64',
        'chest pain type_1': 'int64',
        'chest pain type_2': 'int64',
        'chest pain type_3': 'int64',
        'chest pain type_4': 'int64',
        'resting ecg_0': 'int64',
        'resting ecg_1': 'int64',
        'resting ecg_2': 'int64',
        'ST slope_0': 'int64',
        'ST slope_1': 'int64',
        'ST slope_2': 'int64',
        'ST slope_3': 'int64'
    }

    # Check the data type of each column
    for column, expected_type in expected_data_types.items():
        assert pd_df_ge.expect_column_values_to_be_of_type(column, expected_type).success, f"{column} is not of type {expected_type}"

    # Check for missing values in columns
    for column in expected_columns:
        assert pd_df_ge.expect_column_values_to_not_be_null(column).success, f"Column {column} contains null values"

    # Define expected values for all columns
    expected_values = {
        'sex': [0, 1],
        'fasting blood sugar': [0, 1],
        'exercise angina': [0, 1],
        'target': [0, 1],
        'age_0-40': [0, 1],
        'age_41-50': [0, 1],
        'age_51-60': [0, 1],
        'age_61-70': [0, 1],
        'age_71-80': [0, 1],
        'cholesterol_borderline high': [0, 1],
        'cholesterol_high': [0, 1],
        'cholesterol_normal': [0, 1],
        'chest pain type_1': [0, 1],
        'chest pain type_2': [0, 1],
        'chest pain type_3': [0, 1],
        'chest pain type_4': [0, 1],
        'resting ecg_0': [0, 1],
        'resting ecg_1': [0, 1],
        'resting ecg_2': [0, 1],
        'ST slope_0': [0, 1],
        'ST slope_1': [0, 1],
        'ST slope_2': [0, 1],
        'ST slope_3': [0, 1]
    }


    # Check the values in each column
    for column, values in expected_values.items():
        assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column, values).success, f"{column} contains unexpected values"

    # Check for outliers in 'resting bp s' column
    assert pd_df_ge.expect_column_min_to_be_between('resting bp s', 70, 200).success, "Outliers found in 'resting bp s' column"

    # Check for outliers in 'max heart rate' column
    assert pd_df_ge.expect_column_min_to_be_between('max heart rate', 60, 200).success, "Outliers found in 'max heart rate' column"

    # Check for outliers in 'oldpeak' column
    assert pd_df_ge.expect_column_min_to_be_between('oldpeak', -2, 6).success, "Outliers found in 'oldpeak' column"


    for column, values in expected_values.items():
        assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column, values).success, f"{column} contains unexpected values"

    log = logging.getLogger(__name__)
    log.info("Data passed the unit tests")

    print("Data validation passed")
        
        



