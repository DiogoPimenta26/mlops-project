"""
This is a boilerplate pipeline 'feature_selection_pipeline'
generated using Kedro 0.19.5
"""
# src/mlops_project/pipelines/feature_selection_pipeline/nodes.py

# src/mlops_project/pipelines/feature_selection_pipeline/nodes.py

import os
import pickle
import logging
import numpy as np
import pandas as pd
from typing import Dict, Any
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

def feature_selection(X_train: pd.DataFrame, y_train: pd.DataFrame, parameters: Dict[str, Any], plot: bool = True) -> pd.DataFrame:
    log = logging.getLogger(__name__)
    log.info(f"We start with: {len(X_train.columns)} columns")

    # Log the parameters to verify they are loaded correctly
    log.info(f"Parameters received: {parameters}")

    # Access the nested feature selection parameters
    feature_selection_params = parameters.get("parameters", {})
    feature_selection_method = feature_selection_params.get("feature_selection")
    baseline_model_params = feature_selection_params.get("baseline_model_params", {})

    if feature_selection_method == "rfe":
        y_train = np.ravel(y_train)
        # open pickle file with regressors
        try:
            with open(os.path.join(os.getcwd(), 'data', '06_models', 'champion_model.pkl'), 'rb') as f:
                classifier = pickle.load(f)
        except Exception as e:
            log.warning(f"Failed to load classifier from pickle file: {e}. Using RandomForestClassifier.")
            classifier = RandomForestClassifier(**baseline_model_params)

        rfe = RFE(classifier)
        rfe = rfe.fit(X_train, y_train)
        f = rfe.get_support(1)  # the most important features
        X_cols = X_train.columns[f].tolist()

        log.info(f"Number of best columns is: {len(X_cols)}")
        log.info(f"Selected columns are: {X_cols}")

        # Plotting feature importances
        if plot:
            importances = rfe.estimator_.feature_importances_
            indices = np.argsort(importances)[::-1]
            selected_importances = importances[indices][:len(X_cols)]
            selected_features = X_train.columns[indices][:len(X_cols)]

            plt.figure(figsize=(10, 8))
            sns.barplot(x=selected_importances, y=selected_features)
            plt.title("Feature Importances")
            plt.xlabel("Importance")
            plt.ylabel("Feature")
            plt.savefig('data/08_reporting/feature_importances.png')  # Save the plot to a file
            plt.show()  # Display the plot inline

    # Convert the list of columns to a DataFrame
    selected_features_df = pd.DataFrame(X_cols, columns=["selected_features"])
    log.info(f"DataFrame to be saved:\n{selected_features_df}")

    return selected_features_df


