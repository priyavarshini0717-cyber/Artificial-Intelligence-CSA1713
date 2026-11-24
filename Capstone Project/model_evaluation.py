
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)
import numpy as np


def evaluate_model(actual, predicted):
    """Calculate Linear Regression evaluation metrics."""

    r2 = r2_score(actual, predicted)

    mae = mean_absolute_error(actual, predicted)

    rmse = np.sqrt(
        mean_squared_error(actual, predicted)
    )

    return {
        "R2 Score": r2,
        "MAE": mae,
        "RMSE": rmse
    }


def display_evaluation(metrics):
    """Display evaluation results."""

    print("\nMODEL EVALUATION RESULTS")
    print("------------------------")

    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")
