from kedro.pipeline import Pipeline, node
from .nodes import feature_extraction, align_features

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=feature_extraction,
                inputs="preprocessed_data",
                outputs="features",
                name="extract_features_node",
            ),
            node(
                func=align_features,
                inputs=["features", "params:feature_columns"],
                outputs="aligned_features",
                name="align_features_node",
            )
        ]
    )

