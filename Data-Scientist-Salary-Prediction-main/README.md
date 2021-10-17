# Data-Scientist-Salary-Prediction


## Table of Content
  * Linkdin Profile
  * Project Overview
  * How will this project help?
  * Resources Used
  * Exploratory Data Analysis (EDA) and Data Cleaning
  * Feature Engineering
  * Model Building and Evaluation
  * Model Prediction


## Linkdin Profile
For any queries regarding about this project contact me

Link : https://www.linkedin.com/in/anil-l-b023631b6/

![Dataset](https://img.shields.io/badge/Dataset-Ken_Jee-blue.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![library](https://img.shields.io/badge/Library-sklearn-orange.svg)

## Project Overview
• Created a machine learning model that **estimates salary of data scientist based on the features like rating, company_founded, etc.**<br/>
• Engineered features from the text of each job description to quantify the value companies put on python, excel, tableau and sql

## How will this project help?
• This project **helps data scientist/analyst to negotiate their income for an existing or a new job**

## Resources Used
• Packages: **pandas, numpy, sklearn, matplotlib, seaborn.**<br/>
• Dataset by **Ken Jee**: https://github.com/PlayingNumbers/ds_salary_proj

## Exploratory Data Analysis (EDA) and Data Cleaning
• **Removed unwanted columns**: 'Unnamed: 0'<br/>
• **Plotted bargraphs and countplots** for numerical and categorical features respectively for EDA<br/>
• **Numerical Features** (Rating, Founded): **Replaced NaN or -1 values with mean or meadian based on their distribution**<br/>
![rating](https://user-images.githubusercontent.com/71332138/136660105-8b3f4471-24ef-48b2-853d-f1b7cc7df14c.png)
![rating1](https://user-images.githubusercontent.com/71332138/136660109-cafcede3-8c9b-4b58-a7d8-34065a53e4d3.png)


• **Categorical Features: Replaced NaN or -1 values with 'Other'/'Unknown' category**<br/>
• **Removed unwanted alphabet/special characters from Salary feature**<br/>
• **Converted the Salary column into one scale** i.e from (per hour, per annum, employer provided salary) to (per annum)

## Feature Engineering
• **Creating new features** from existing features e.g. **job_in_headquaters from (job_location, headquarters)**, etc.<br/>
![jih](https://user-images.githubusercontent.com/71332138/136660172-918d13a3-2615-4d72-894e-3542845ef4cd.png)


• Trimming columns i.e. **Trimming features having more than 10 categories to reduce the dimensionality**<br/>
• **Handling ordinal and nominal categorical features**<br/>
• Feature Selection using **information gain (mutual_info_regression) and correlation matrix**<br/>
• Feature Scaling using **StandardScalar**

![infogain](https://user-images.githubusercontent.com/71332138/136661017-d20b34d3-44c9-4d5d-b9ae-bb8fd78c5532.png)

![corr1](https://user-images.githubusercontent.com/71332138/136661022-82bb83d6-6ad5-49bb-b79b-0cb3c3d10757.png)


## Model Building and Evaluation
Metric: Negative Root Mean Squared Error (NRMSE)<br/>
• Multiple Linear Regression: -27.523<br/>
• Lasso Regression: -27.993<br/>
• **Random Forest: -17.637**<br/>
• Gradient Boosting: -24.429<br/>
• Voting (Random Forest + Gradient Boosting): -19.136<br/>
_**Note: Evaluation scores are obtained using cross validation.**_

## Model Prediction
![prediction](https://user-images.githubusercontent.com/71332138/136661034-4f92cf71-abca-4e06-a748-41fc606e6977.PNG)





