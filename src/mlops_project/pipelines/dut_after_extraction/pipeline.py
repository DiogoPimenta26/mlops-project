"""
This is a boilerplate pipeline 'dut_after_extraction'
generated using Kedro 0.19.5
"""


from kedro.pipeline import node, Pipeline
from .nodes import validate_data

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=validate_data,
                inputs="aligned_features",
                outputs=None,
                name="validate_data_node"
            ),
            
        ]
    )