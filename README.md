# Titanic: Machine Learning Project

## Problem Statement
The sinking of the Titanic in 1912 remains one of the most disastrous events in history. This project aims to develop a predictive model to determine whether a passenger survived based on various factors.

## Objective
To deploy artificial intelligence techniques, specifically machine learning models, to predict whether a passenger survived or not during the Titanic disaster.

## Data Preprocessing
- **Imports Libraries**: Used libraries such as Pandas, NumPy, Seaborn, and Matplotlib.
- **Handling Missing Data**: Imputed missing values and dropped irrelevant columns.
- **Encoding**: Encoded categorical features to numerical values.
- **Visualization**: Created count plots and heatmaps to visualize data distributions and correlations.

## Model Development
- **Features**: `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`, `isMale`
- **Models Used**:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors (KNN)
  - Decision Tree
  - Random Forest
- **Pipeline**: Preprocessing pipeline using `ColumnTransformer` and `Pipeline` from scikit-learn.
- **Performance**: Compared accuracy of models before and after applying the pipeline.

## Results
The project successfully implemented and compared different machine learning models, with significant improvement in accuracy after applying the preprocessing pipeline.

## Instructions
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Titanic-Machine-Learning-Project.git
   cd Titanic-Machine-Learning-Project
