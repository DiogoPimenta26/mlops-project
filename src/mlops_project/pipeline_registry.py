# pipeline registry file

from kedro.pipeline import Pipeline
from typing import Dict

from mlops_project.pipelines import (
    data_processing as dp,
    feature_extraction_alignment as fea, train_test_split as tts , data_unit_tests as data_unit_tests_pipeline
)

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.

    Returns:
    A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = dp.create_pipeline()
    
    feature_extraction_alignment_pipeline = fea.create_pipeline()
    train_test_split_pipeline = tts.create_pipeline()
    

    return {
        "data_unit_tests": data_unit_tests_pipeline.create_pipeline(),
        "data_processing": data_processing_pipeline,
        "feature_extraction_alignment": feature_extraction_alignment_pipeline,
        "tts": train_test_split_pipeline
    }