# ACCIDENT ZONE PREDICTION

## Overview

The ACCIDENT ZONE PREDICTION project aims to predict accident severity based on geographical coordinates and the number of casualties. This machine learning model utilizes decision tree classification to analyze historical accident data, providing insights into potential accident-prone areas.

## Problem Statement

Traffic accidents are a significant concern globally, leading to injuries, fatalities, and economic losses. Predicting accident severity can aid in proactive measures, such as improving road infrastructure or enhancing emergency response systems. The ACCIDENT ZONE PREDICTION project addresses this issue by leveraging machine learning techniques to forecast the severity of accidents.

## How it Works

1. **Data Preprocessing:**
   - Merging datasets: Combining accident, casualties, and vehicles data.
   - Feature selection: Choosing relevant columns for analysis.
   - Handling missing values: Removing rows with incomplete data.
   - Encoding categorical variables: Transforming non-numeric data into numerical format.

2. **Model Training:**
   - Splitting data: Dividing the dataset into training and testing sets.
   - Decision tree classifier: Employing a machine learning model for accident severity prediction.
   - Accuracy evaluation: Assessing the model's performance using accuracy metrics.

3. **Geospatial Visualization:**
   - Creating a geospatial map: Utilizing Folium to visualize accident predictions.
   - Marker clustering: Enhancing map readability by clustering nearby markers.
   - HTML export: Saving the interactive map as an HTML file for easy sharing.

## Project Report

For a detailed project report, you can refer to [Project Report PDF]
## Project Structure

|-- venv/
|-- code/
| |-- accident_prediction.py
|-- data/
| |-- AccidentsBig.csv
| |-- CasualtiesBig.csv
| |-- VehiclesBig.csv
|-- images/
|-- maps/
|-- Accident_Predictions.csv
|-- .gitignore
|-- README.md
|-- requirements.txt


## Libraries Used

- Pandas: Data manipulation and analysis.
- Scikit-learn: Machine learning model development.
- Folium: Geospatial data visualization.
- Matplotlib and Seaborn: Additional data visualization tools.

## Project Visualization
![image](https://github.com/utoo0703/ACCIDENT-ZONE-PREDICTION/assets/78578594/c4564563-9547-47bd-8ed1-3ee2b5803725)

![Screenshot 2024-03-08 100901](https://github.com/utoo0703/ACCIDENT-ZONE-PREDICTION/assets/78578594/3a56a6f0-8c41-4706-b9e0-44e32e6f1745)

![image](https://github.com/utoo0703/ACCIDENT-ZONE-PREDICTION/assets/78578594/41329134-a47d-497a-b537-e596fe09b602)

