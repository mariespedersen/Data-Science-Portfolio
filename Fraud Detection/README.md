# Fraud Detection
## Introduction
Fraud detection is a set of activities undertaken to prevent money or property from being obtained through false pretenses. Fraud detection is applied to many industries such as banking or insurance. In banking, fraud may include forging checks or using stolen credit cards. Other forms of fraud may involve exaggerating losses or causing an accident with the sole intent for the payout. Since the advent of e-commerce, fraud has become an increasingly common problem. In 2016 alone, the total value of fraudulent transactions was estimated to be over $12 billion. In this project, we will use machine learning algorithms to detect fraud. We will use a dataset of credit card transactions to build a model that can identify fraudulent activity. The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. The dataset has also been transformed using PCA to protect the privacy of the cardholders. The features are scaled and the names of the features are not disclosed. The only features which have not been transformed with PCA are 'Time' and 'Amount'. 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. 'Amount' is the transaction amount. 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. The dataset can be downloaded from Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data

## Objectives
The goal of this project is to build a model that can detect fraudulent activity. We will use machine learning algorithms to classify transactions as fraudulent or not fraudulent. We will evaluate the performance of the model using metrics such as accuracy, precision, recall, and F1 score.

## Data Preprocessing
1. Load the dataset
2. Check for missing values
3. Check for duplicate rows
4. Check for class imbalance
5. Split the data into features and target variable
6. Split the data into training and testing sets
7. Scale the features

## Exploratory Data Analysis
Because the features have been transformed using PCA, we will not perform exploratory data analysis.

## Model Selection
We will use the following machine learning algorithms to build the model: Logistic Regression. Becuase the dataset is highly unbalanced, we will use different approached to handle imbalanced data:
1. Adjust the `class_weight` parameter to handle the class imbalance. 
2. Oversample the minority class using the `RandomOverSampler` from the `imbalanced-learn` library.
3. Undersample the majority class using the `RandomUnderSampler` from the `imbalanced-learn` library.

## Evaluation Metrics
We will use the following metrics to evaluate the performance of the model:
1. Accuracy
2. Precision
3. Recall
4. F1 Score

## Conclusion
In this project, we used machine learning algorithms to detect fraud. We built a model that can classify transactions as fraudulent or not fraudulent. We evaluated the performance of the model using metrics such as accuracy, precision, recall, and F1 score. The model achieved an accuracy of 99.92%, precision of 88.89%, recall of 66.33%, and F1 score of 76.09%. The model performed well in detecting fraudulent activity. However, there is still room for improvement. We can further tune the hyperparameters of the model to improve its performance. We can also try other machine learning algorithms to see if they can achieve better results. Overall, the model is effective in detecting fraud and can be used to prevent fraudulent activity in the future.