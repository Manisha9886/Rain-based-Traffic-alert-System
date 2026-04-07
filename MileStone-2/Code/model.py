import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_excel("rain_traffic_dataset.xlsx")

print("Dataset Loaded!")
print(df.head())

le = LabelEncoder()
df['Risk'] = le.fit_transform(df['Risk'])

print("\nRisk Classes:", list(le.classes_))

X = df[['Rain', 'Traffic', 'Distance', 'Temperature',
        'Humidity', 'Visibility', 'Speed']]

y = df['Risk']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


model = RandomForestClassifier(
    n_estimators=300,        
    max_depth=15,            
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("\n MODEL TRAINED")
print("Accuracy: {:.2f}%".format(accuracy * 100))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

joblib.dump(model, "high_accuracy_model.pkl")
print("\nModel saved as high_accuracy_model.pkl")

sample = [[3500, 1, 10, 30, 80, 20, 90]]

prediction = model.predict(sample)

print("\nSample Prediction (Encoded):", prediction)
print("Predicted Risk:", le.inverse_transform(prediction))