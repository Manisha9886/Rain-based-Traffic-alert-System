from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


model1 = LogisticRegression(max_iter=1000)
model2 = DecisionTreeClassifier(max_depth=5)
model3 = SVC(probability=True)


hybrid_model = VotingClassifier(
    estimators=[
        ('lr', model1),
        ('dt', model2),
        ('svm', model3)
    ],
    voting='soft'   
)

hybrid_model.fit(X_train, y_train)


y_pred = hybrid_model.predict(X_test)


acc = accuracy_score(y_test, y_pred)

print("\n HYBRID MODEL (Voting Classifier)")
print("Accuracy:", acc * 100)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))