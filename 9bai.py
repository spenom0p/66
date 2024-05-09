import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load the Iris dataset
df = pd.read_csv('IRIS.csv')

# Drop any rows with missing values
df = df.dropna(axis=1, how='any')

# Encode the target variable 'species'
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])

# Prepare the features (X) and target (y)
X = df.iloc[:, 0:3]  # Selecting first three columns as features (sepal_length, sepal_width, petal_length)
y = df['species']  # Target variable is 'species'

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into train, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_validate, X_test, y_validate, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Train Gaussian Naive Bayes classifier
bayes = GaussianNB()
bayes.fit(X_train, y_train)

# Validate the model on the validation set
validation_score = bayes.score(X_validate, y_validate)
print("Validation Accuracy:", validation_score)

# Test the model on the test set
test_score = bayes.score(X_test, y_test)
print("Test Accuracy:", test_score)
