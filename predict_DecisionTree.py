import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('learned_colors_green.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

(X_train, X_test, y_train, y_test) = train_test_split(
X, y, test_size=0.3, random_state=0,)


lr = DecisionTreeClassifier()

lr.fit(X_train,y_train)

y_pred = lr.predict(X_test)
print('confusion matrix = \n', confusion_matrix(y_true=y_test, y_pred=y_pred))
print('accuracy = ', accuracy_score(y_true=y_test, y_pred=y_pred))
print('precision = ', precision_score(y_true=y_test, y_pred=y_pred))
print('recall = ', recall_score(y_true=y_test, y_pred=y_pred))
print('f1 score = ', f1_score(y_true=y_test, y_pred=y_pred))
