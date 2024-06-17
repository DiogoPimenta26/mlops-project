from kedro.pipeline import Pipeline, node
from .nodes import remove_duplicates, remove_zero_bp, remove_zero_cholesterol, max_heart_rate_outliers, bin_age, bin_cholesterol

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=remove_duplicates,
                inputs="heart_data_raw",
                outputs="output_dataframe_after_duplicates_removal",
                name="remove_duplicates_node"
            ),
            node(
                func=remove_zero_bp,
                inputs="output_dataframe_after_duplicates_removal",
                outputs="output_dataframe_after_zero_bp_removal",
                name="remove_zero_bp_node"
            ),
            node(
                func=remove_zero_cholesterol,
                inputs="output_dataframe_after_zero_bp_removal",
                outputs="output_dataframe_after_zero_cholesterol_removal",
                name="remove_zero_cholesterol_node"
            ),
            node(
                func=max_heart_rate_outliers,
                inputs="output_dataframe_after_zero_cholesterol_removal",
                outputs="output_dataframe_after_max_hr_outliers_removal",
                name="max_heart_rate_outliers_node"
            ),
            node(
                func=bin_age,
                inputs="output_dataframe_after_max_hr_outliers_removal",
                outputs="output_dataframe_after_age_binning",
                name="bin_age_node"
            ),
            node(
                func=bin_cholesterol,
                inputs="output_dataframe_after_age_binning",
                outputs="preprocessed_data",
                name="bin_cholesterol_node"
            ),
        ]
    )