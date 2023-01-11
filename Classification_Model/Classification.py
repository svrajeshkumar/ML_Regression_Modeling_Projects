import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load dataset
data = load_breast_cancer()


label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# Look at our data
print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])

# Split our data
train, test, train_labels, test_labels = train_test_split(features,labels, test_size=0.33,random_state=42)