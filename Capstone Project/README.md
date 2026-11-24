
# WaterWise – Intelligent Agent-Based Water Demand Forecasting and Optimization System

## Project Overview

WaterWise is an AI-based water demand forecasting and optimization system developed using Linear Regression and intelligent agent concepts.

The system analyzes historical water consumption data, predicts future water demand, monitors the availability of water resources and calculates sector-wise water allocation.

## Objectives

1. Forecast water demand using Linear Regression.
2. Preprocess and analyze historical water consumption data.
3. Evaluate model performance using R2 Score, MAE and RMSE.
4. Monitor water demand and generate shortage alerts.
5. Optimize water distribution among household, agriculture and industry sectors.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS
- JavaScript
- Visual Studio Code
- GitHub

## Project Modules

1. Dataset Management
2. Data Preprocessing
3. Linear Regression Model Training
4. Water Demand Forecasting
5. Model Evaluation
6. Intelligent Agent Monitoring
7. Water Allocation Optimization

## Dataset

Upload the Global Water Consumption CSV dataset through the application.

The target column should be:

Total Water Consumption

The remaining usable columns are considered model input features.

## Installation

Install Python on your computer.

Open the project folder in VS Code.

Open the terminal and execute:

pip install -r requirements.txt

## Run the Application

Execute:

streamlit run app.py

The application will open in your web browser.

## Model Evaluation

The trained model is evaluated using:

- R2 Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## Expected Outcome

The system provides water demand predictions, model evaluation results, shortage monitoring and proportional sector-wise allocation calculations.

## Project Note

This is an academic prototype. Prediction quality depends on the uploaded dataset, selected target column and model validation. Allocation calculations are illustrative and should not replace real-world water policy decisions.

## Future Enhancements

- Live weather data integration
- Advanced machine learning models
- Real-time water monitoring
- Cloud database integration
- Automated shortage notifications
