"""
This is a boilerplate pipeline 'data_unit_tests'
generated using Kedro 0.19.5
"""

from kedro.pipeline import Pipeline, pipeline


from kedro.pipeline import Pipeline, node
from .nodes import validate_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=validate_data,
                inputs="heart_data_raw",
                outputs=None,
                name="validate_data_node",
            ),
        ]
    )