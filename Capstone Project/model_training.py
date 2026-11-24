
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
import joblib


def train_model(X, y):
    """Train a Linear Regression model."""

    if len(X) < 5:
        raise ValueError(
            "At least 5 usable records are recommended for training."
        )

    numeric_features = X.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    if not numeric_features and not categorical_features:
        raise ValueError("No usable features are available.")

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    transformers = []

    if numeric_features:
        transformers.append(
            ("numeric", numeric_pipeline, numeric_features)
        )

    if categorical_features:
        transformers.append(
            ("categorical", categorical_pipeline,
             categorical_features)
        )

    preprocessor = ColumnTransformer(
        transformers=transformers
    )

    model_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model_pipeline.fit(X_train, y_train)

    predictions = model_pipeline.predict(X_test)

    joblib.dump(model_pipeline, "waterwise_model.pkl")

    return (
        model_pipeline,
        X_train,
        X_test,
        y_train,
        y_test,
        predictions
    )


def predict_demand(model, input_data):
    """Predict water demand for new input records."""
    return model.predict(input_data)
