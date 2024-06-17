# pipeline registry file

from kedro.pipeline import Pipeline
from typing import Dict

from mlops_project.pipelines import (
    data_processing as dp,
)

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.

    Returns:
    A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = dp.create_pipeline()

    return {
        "data_processing": data_processing_pipeline,
    }