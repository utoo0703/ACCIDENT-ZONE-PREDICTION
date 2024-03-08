import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import folium
from folium.plugins import MarkerCluster

# Load the datasets
accidents_df = pd.read_csv("data/AccidentsBig.csv", low_memory=False)
casualties_df = pd.read_csv("data/CasualtiesBig.csv", low_memory=False)
vehicles_df = pd.read_csv("data/VehiclesBig.csv", low_memory=False)

# Merge datasets
merged_df = pd.merge(accidents_df, casualties_df, on="Accident_Index")
merged_df = pd.merge(merged_df, vehicles_df, on="Accident_Index")

# Filter relevant columns
data = merged_df[['latitude', 'longitude', 'Accident_Severity', 'Number_of_Casualties']]

# Drop rows with missing values
data = data.dropna()

# Encode categorical variables
label_encoder = LabelEncoder()
data['Accident_Severity'] = label_encoder.fit_transform(data['Accident_Severity'])

# Split the data into features (X) and target variable (y)
X = data[['latitude', 'longitude', 'Number_of_Casualties']]
y = data['Accident_Severity']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a decision tree classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Make predictions for the entire dataset
data['Predicted_Accident_Severity'] = model.predict(X)

# Save the results to a new CSV file
data.to_csv("Accident_Predictions.csv", index=False)

# Load the predicted data
predictions_df = pd.read_csv("Accident_Predictions.csv")

# Create a map centered around India
prediction_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create a MarkerCluster for clustering nearby markers
marker_cluster = MarkerCluster().add_to(prediction_map)

# Function to add markers with clustering to the map
def add_markers_with_cluster(map_obj, df):
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Accident Index: {index}\nPredicted Severity: {row['Predicted_Accident_Severity']}",
            icon=folium.Icon(color='red' if row['Predicted_Accident_Severity'] == 1 else 'orange' if row['Predicted_Accident_Severity'] == 2 else 'green')
        ).add_to(marker_cluster)

# Add markers with clustering to the map
add_markers_with_cluster(prediction_map, predictions_df)

# Save the map as an HTML file in the maps directory
prediction_map.save('maps/clustered_prediction_map.html')
