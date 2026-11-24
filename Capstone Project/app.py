
import streamlit as st
import pandas as pd

from data_preprocessing import (
    load_dataset,
    clean_dataset,
    prepare_features
)

from model_training import train_model

from model_evaluation import evaluate_model

from intelligent_agent import monitor_water_demand

from allocation_optimizer import optimize_allocation


st.set_page_config(
    page_title="WaterWise AI",
    page_icon="💧",
    layout="wide"
)

st.title("💧 WaterWise")
st.subheader(
    "Intelligent Agent-Based Water Demand Forecasting "
    "and Optimization System using Linear Regression"
)

st.write(
    "Upload your water consumption dataset, train a "
    "Linear Regression model, monitor water demand "
    "and calculate sector-wise allocation."
)

st.sidebar.title("WaterWise Modules")

module = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Dataset Manager",
        "Demand Forecast",
        "Model Evaluation",
        "Intelligent Agent",
        "Allocation Optimizer"
    ]
)

if "model" not in st.session_state:
    st.session_state.model = None

if "metrics" not in st.session_state:
    st.session_state.metrics = None

if "predictions" not in st.session_state:
    st.session_state.predictions = None

if "actual" not in st.session_state:
    st.session_state.actual = None

if "columns" not in st.session_state:
    st.session_state.columns = None

if "dataset" not in st.session_state:
    st.session_state.dataset = None


st.sidebar.markdown("---")
uploaded_file = st.sidebar.file_uploader(
    "Upload Water Consumption CSV",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        raw_data = load_dataset(uploaded_file)
        cleaned_data = clean_dataset(raw_data)

        st.session_state.dataset = cleaned_data
        st.session_state.columns = cleaned_data.columns.tolist()

    except Exception as error:
        st.error(str(error))


if module == "Dashboard":

    st.header("Project Dashboard")

    if st.session_state.dataset is not None:
        data = st.session_state.dataset

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", len(data))
        col2.metric("Total Columns", len(data.columns))
        col3.metric("Missing Values", int(data.isna().sum().sum()))

        st.subheader("Dataset Preview")
        st.dataframe(data.head(10), use_container_width=True)

        st.subheader("Dataset Information")
        st.write(data.describe(include="all"))

    else:
        st.info("Upload a CSV dataset using the sidebar.")

    if st.session_state.metrics is not None:
        st.subheader("Latest Model Performance")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "R² Score",
            f"{st.session_state.metrics['R2 Score']:.4f}"
        )

        c2.metric(
            "MAE",
            f"{st.session_state.metrics['MAE']:.4f}"
        )

        c3.metric(
            "RMSE",
            f"{st.session_state.metrics['RMSE']:.4f}"
        )


elif module == "Dataset Manager":

    st.header("Dataset Manager")

    if st.session_state.dataset is not None:

        data = st.session_state.dataset

        st.success("Dataset uploaded successfully.")

        st.write("Dataset Shape:", data.shape)

        st.subheader("Dataset Preview")
        st.dataframe(data.head(20), use_container_width=True)

        st.subheader("Column Names")
        st.write(data.columns.tolist())

        st.subheader("Missing Values")
        st.dataframe(
            data.isnull().sum().rename("Missing Count")
        )

        st.subheader("Statistical Summary")
        st.dataframe(data.describe(include="all"))

    else:
        st.warning("Please upload a CSV file first.")


elif module == "Demand Forecast":

    st.header("Water Demand Forecast")

    if st.session_state.dataset is not None:

        data = st.session_state.dataset

        target_column = st.selectbox(
            "Select target column",
            data.columns.tolist(),
            index=(
                data.columns.get_loc("Total Water Consumption")
                if "Total Water Consumption" in data.columns
                else len(data.columns) - 1
            )
        )

        if st.button("Train Linear Regression Model"):

            try:
                X, y = prepare_features(data, target_column)

                result = train_model(X, y)

                model, X_train, X_test, y_train, y_test, predictions = result

                metrics = evaluate_model(y_test, predictions)

                st.session_state.model = model
                st.session_state.metrics = metrics
                st.session_state.predictions = predictions
                st.session_state.actual = y_test
                st.session_state.feature_columns = X.columns.tolist()
                st.session_state.target_column = target_column

                st.success("Model trained successfully!")

                st.subheader("Model Performance")

                c1, c2, c3 = st.columns(3)

                c1.metric("R² Score", f"{metrics['R2 Score']:.4f}")
                c2.metric("MAE", f"{metrics['MAE']:.4f}")
                c3.metric("RMSE", f"{metrics['RMSE']:.4f}")

            except Exception as error:
                st.error(f"Model training failed: {error}")

        if st.session_state.model is not None:

            st.subheader("Predict using a dataset record")

            feature_columns = st.session_state.feature_columns

            input_values = {}

            for column in feature_columns:

                if pd.api.types.is_numeric_dtype(data[column]):
                    default_value = float(
                        pd.to_numeric(
                            data[column], errors="coerce"
                        ).median()
                    )

                    if pd.isna(default_value):
                        default_value = 0.0

                    input_values[column] = st.number_input(
                        column,
                        value=default_value
                    )

                else:
                    choices = data[column].dropna().astype(str).unique().tolist()

                    if choices:
                        input_values[column] = st.selectbox(
                            column,
                            choices
                        )
                    else:
                        input_values[column] = st.text_input(column)

            if st.button("Predict Water Demand"):

                try:
                    input_data = pd.DataFrame(
                        [input_values],
                        columns=feature_columns
                    )

                    prediction = st.session_state.model.predict(
                        input_data
                    )[0]

                    st.success(
                        f"Predicted water demand: {prediction:.2f}"
                    )

                except Exception as error:
                    st.error(f"Prediction failed: {error}")

    else:
        st.warning("Upload your dataset before forecasting.")


elif module == "Model Evaluation":

    st.header("Model Evaluation")

    if st.session_state.metrics is not None:

        metrics = st.session_state.metrics

        c1, c2, c3 = st.columns(3)

        c1.metric("R² Score", f"{metrics['R2 Score']:.4f}")
        c2.metric("MAE", f"{metrics['MAE']:.4f}")
        c3.metric("RMSE", f"{metrics['RMSE']:.4f}")

        st.subheader("Actual vs Predicted Values")

        comparison = pd.DataFrame({
            "Actual": st.session_state.actual,
            "Predicted": st.session_state.predictions
        })

        st.dataframe(comparison, use_container_width=True)

        st.line_chart(comparison)

        st.download_button(
            "Download Evaluation Results",
            comparison.to_csv(index=False),
            file_name="waterwise_predictions.csv",
            mime="text/csv"
        )

    else:
        st.info(
            "Train the Linear Regression model in the Demand Forecast module first."
        )


elif module == "Intelligent Agent":

    st.header("Intelligent Agent Monitoring")

    demand = st.number_input(
        "Predicted Water Demand (BCM)",
        min_value=0.0,
        value=128.4
    )

    supply = st.number_input(
        "Available Water Supply (BCM)",
        min_value=0.0,
        value=118.0
    )

    threshold = st.number_input(
        "Shortage Alert Threshold (%)",
        min_value=0.0,
        value=5.0
    )

    if st.button("Run Monitoring Agent"):

        result = monitor_water_demand(
            demand,
            supply,
            threshold
        )

        st.subheader("Agent Decision")

        st.write("Status:", result["Agent Status"])
        st.write("Demand:", result["Predicted Demand"])
        st.write("Supply:", result["Available Supply"])
        st.write("Supply Gap:", result["Supply Gap"])
        st.write(
            "Shortage Percentage:",
            result["Shortage Percentage"]
        )

        if result["Agent Status"] == "SHORTAGE ALERT":
            st.error(result["Message"])

        elif result["Agent Status"] == "MONITOR":
            st.warning(result["Message"])

        else:
            st.success(result["Message"])


elif module == "Allocation Optimizer":

    st.header("Water Allocation Optimizer")

    supply = st.number_input(
        "Available Supply (BCM)",
        min_value=0.0,
        value=118.0
    )

    household = st.number_input(
        "Household Priority Weight",
        min_value=0,
        value=40
    )

    agriculture = st.number_input(
        "Agriculture Priority Weight",
        min_value=0,
        value=40
    )

    industry = st.number_input(
        "Industry Priority Weight",
        min_value=0,
        value=20
    )

    if st.button("Optimize Water Allocation"):

        try:
            result = optimize_allocation(
                supply,
                household,
                agriculture,
                industry
            )

            st.subheader("Recommended Allocation")

            for sector, values in result.items():

                st.write(
                    f"{sector}: "
                    f"{values['Allocated Water']:.2f} BCM"
                )

                st.progress(
                    values["Percentage"] / 100
                )

                st.caption(
                    f"{values['Percentage']:.2f}%"
                )

            st.success("Allocation calculation completed.")

        except Exception as error:
            st.error(str(error))


st.markdown("---")
st.caption(
    "WaterWise | AI-Based Water Demand Forecasting "
    "and Optimization | Academic Project"
)
