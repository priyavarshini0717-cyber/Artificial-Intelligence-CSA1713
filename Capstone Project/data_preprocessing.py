
import pandas as pd


def load_dataset(file):
    """Load a CSV dataset from a file path or uploaded file."""
    try:
        data = pd.read_csv(file)
        if data.empty:
            raise ValueError("The uploaded dataset is empty.")
        return data
    except Exception as error:
        raise ValueError(f"Unable to load dataset: {error}")


def clean_dataset(data):
    """Clean the dataset before model training."""
    data = data.copy()

    data.columns = data.columns.str.strip()

    data = data.drop_duplicates()

    data = data.dropna(axis=1, how="all")

    return data


def prepare_features(data, target_column):
    """Separate features and target and handle missing values."""
    if target_column not in data.columns:
        raise ValueError(
            f"Target column '{target_column}' was not found. "
            f"Available columns: {list(data.columns)}"
        )

    data = data.copy()

    data[target_column] = pd.to_numeric(
        data[target_column], errors="coerce"
    )

    data = data.dropna(subset=[target_column])

    X = data.drop(columns=[target_column])
    y = data[target_column]

    X = X.drop(columns=[
        col for col in X.columns
        if X[col].isna().all()
    ])

    if X.empty:
        raise ValueError("No usable input features were found.")

    return X, y
