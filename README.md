# Titanic: Machine Learning Project

## Problem Statement
The sinking of the Titanic in 1912 remains one of the worst disasters in history. This project aims to develop a predictive model to determine whether a passenger survived based on various factors.

## Objective
To deploy artificial intelligence techniques, specifically machine learning models, to predict whether a passenger survived or not during the Titanic disaster.

## Data Preprocessing
- **Import Libraries**: Utilized libraries such as Pandas, NumPy, Seaborn, and Matplotlib.
- **Handling Missing Data**: Imputed missing values using the mode and dropped irrelevant columns.
- **Encoding**: Encoded categorical features (gender and embarked locations) into numerical values.
- **Visualization**: Created count plots and heatmaps to visualize data distributions and correlations.

## Model Development
- **Features**: `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`, `isMale`
- **Models Used**:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors (KNN)
  - Decision Tree
  - Random Forest
- **Pipeline**: Utilized `ColumnTransformer` and `Pipeline` from scikit-learn for preprocessing and model training.
- **Performance**: Compared accuracy of models before and after applying the pipeline.

## Results
The project successfully implemented and compared different machine learning models, showing improved accuracy after applying the preprocessing pipeline.
