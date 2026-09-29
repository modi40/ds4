import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv('online_gaming_behavior_dataset.csv')

print("Dataset Info:")
print(df.info())

X = df[['daily_play_time', 'achievements_unlocked', 'in_game_purchases', 'gaming_level']]
y = df['gamer_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label='Professional'))
print("Recall:", recall_score(y_test, y_pred, pos_label='Professional'))
print("F1-Score:", f1_score(y_test, y_pred, pos_label='Professional'))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
