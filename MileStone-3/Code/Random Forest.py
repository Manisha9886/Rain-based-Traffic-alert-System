import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
df = pd.read_excel("rain_traffic_dataset.xlsx")
print("Dataset Loaded!\n")

le = LabelEncoder()
df['Risk'] = le.fit_transform(df['Risk'])
print("\nEncoded Classes:", list(le.classes_))

X = df[['Rain', 'Traffic', 'Distance', 'Temperature',
        'Humidity', 'Visibility', 'Speed']]
y = df['Risk']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)model = RandomForestClassifier(
    n_estimators=100,     # number of trees
    max_depth=10,         # control complexity
    random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n🌲 RANDOM FOREST MODEL")
print("Accuracy: {:.2f}%".format(acc * 100))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
