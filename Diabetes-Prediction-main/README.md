# Diabetes-Prediction

## Table of Content
  * Demo
  * Overview
  * Motivation
  * Data Collection
  * EDA
  * Applied Machine Learning
  * Deployement on Azure
  * Installation and Run 
  * Future scope of the project
 
## Linkdin Profile
For any queries regarding about this project contact me

Link : https://www.linkedin.com/in/anil-l-b023631b6/

## Video Demo

https://user-images.githubusercontent.com/71332138/136748117-2e8a6d8a-928c-4b8e-9fc7-33e818ec576c.mov

## Overview
Diabaetes Prediction created as an AI module integrated with web app to predict the person have Diabetes or Not, Developed these POC for to get experience real time projects and Created API using Flask Framework and Deployed to the Azure Cloud platform

## Motivation
What to do when you are at home due to this pandemic situation? I started to learn Machine Learning model to get most out of it. I came to know mathematics behind all supervised models and unspurervised models. Finally it is important to work on application (real world application) to actually make a difference. To get a experience you have to work thats the reason to perform my favourable work done.


## Data Collection 
Diabetes Dataset Extracted from the Kaggle you can also extract the data from this link is given my main ipnyb file, Kaggle is an Open source and have a large community also they conduct competitions every month,Kaggle allows users to find and publish data sets, explore and build models in a web-based data-science environment, work with other data scientists and machine learning engineers, and enter competitions to solve data science challenges,Given the thousands of other people also doing them, it is becoming harder and harder for merely working through them to be enough to differentiate you. You'll learn a lot, but it won't make you stand out from your competition.Data scientists of all levels can benefit from the resources and community on Kaggle. Whether you are a beginner, looking to learn new skills and contribute to projects, an advanced data scientist looking for competitions, or somewhere in between, Kaggle is a good place to learn data science real world problems

Databse Link: [https://www.kaggle.com/uciml/pima-indians-diabetes-database]

## EDA

* Check the NULL values
* Check the Correlation with heatmap
* Handling Imbalanced dataset

## Applied Machine Learning

I tried 6 Machine Learning Alogrithms
* Logistic Regression
* Decision Tree
* Random Forest
* KNN
* SVM with Different Kernels
* Naive Bayes

![Screenshot 2021-10-11 at 1 09 04 PM](https://user-images.githubusercontent.com/71332138/136751064-585a4f86-efb5-4dab-bc28-8f9e9c6e8d40.png)

**Then After I choosed Random Forest it has good accuracy and also there is no overfitting problem but you can see Decsion tree has contain Overfitting Problem**


![ML](https://user-images.githubusercontent.com/71332138/136750757-d8c78643-bd70-409c-b13c-99ca0c6d8203.jpeg)


Introduction
Random forest is a Supervised Machine Learning Algorithm that is used widely in Classification and Regression problems. It builds decision trees on different samples and takes their majority vote for classification and average in case of regression.

One of the most important features of the Random Forest Algorithm is that it can handle the data set containing continuous variables as in the case of regression and categorical variables as in the case of classification. It performs better results for classification problems.

Real Life Analogy
Let’s dive into a real-life analogy to understand this concept further. A student named X wants to choose a course after his 10+2, and he is confused about the choice of course based on his skill set. So he decides to consult various people like his cousins, teachers, parents, degree students, and working people. He asks them varied questions like why he should choose, job opportunities with that course, course fee, etc. Finally, after consulting various people about the course he decides to take the course suggested by most of the people.

Working of Random Forest Algorithm
Before understanding the working of the random forest we must look into the ensemble technique. Ensemble simply means combining multiple models. Thus a collection of models is used to make predictions rather than an individual model.

### Important Features of Random Forest
1. Diversity- Not all attributes/variables/features are considered while making an individual tree, each tree is different.
2. Immune to the curse of dimensionality- Since each tree does not consider all the features, the feature space is reduced.
3. Parallelization-Each tree is created independently out of different data and attributes. This means that we can make full use of the CPU to build random forests.
4.  Train-Test split- In a random forest we don’t have to segregate the data for train and test as there will always be 30% of the data which is not seen by the decision tree.
5.  Stability- Stability arises because the result is based on majority voting/ averaging.


Deep Explanation of Random forest(Good Content) : https://www.analyticsvidhya.com/blog/2021/06/understanding-random-forest/
5 Types of Classification Algorithms in Machine Learning Explanation: [https://monkeylearn.com/blog/classification-algorithms/]


## Flask Framework

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. ... Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.

Flask Tutorial : [https://www.tutorialspoint.com/flask/index.htm]

## Deployement on Azure

What is Azure? At its core, Azure is a public cloud computing platform—with solutions including Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS) that can be used for services such as analytics, virtual computing, storage, networking, and much more.

![azure](https://user-images.githubusercontent.com/71332138/136748845-9de4d297-0790-49e2-bac7-01447be17220.jpeg)


## Screenshots of Project


--------------------------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot 2021-10-11 at 12 24 51 PM](https://user-images.githubusercontent.com/71332138/136748978-0effab6a-5b7a-4477-a78f-254074299320.png)



---------------------------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot 2021-10-11 at 12 25 12 PM](https://user-images.githubusercontent.com/71332138/136748992-3f270486-5302-49bc-9b1f-9cc4d198b603.png)


-------------------------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot 2021-10-11 at 12 25 30 PM](https://user-images.githubusercontent.com/71332138/136749002-64f393be-24c0-445c-a4b3-942b39ecb456.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![Screenshot 2021-10-11 at 12 26 03 PM](https://user-images.githubusercontent.com/71332138/136749024-f2b89c2f-b87e-4a73-b672-bd64196cc366.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------


## Installation and Run
The Code is written in Python 3.9 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

Install Required Libraries

     Step 1: pip install -r requirements.txt
     
Running Project

     Step 2: python main.py

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)  ![pandas](https://user-images.githubusercontent.com/71332138/134156736-9dcc4675-e588-42a6-9481-816ac08654ab.png).

![blog sklearn](https://user-images.githubusercontent.com/71332138/134540412-a009eb7d-f4fa-412f-bc1a-a5c89ba74aa4.png). ![numpy](https://user-images.githubusercontent.com/71332138/134540645-95fa9566-18ca-4719-8cc6-82153e96683c.png) 
                               ![flask](https://user-images.githubusercontent.com/71332138/136525463-d94befe6-f982-4f98-bd1c-833bdbd3c004.png)
   
         
                            
## Tools / IDE
I used Jupyter NoteBook (Google Colab) for model training. used spyder for model deployment on the local system. To use Jupyter NoteBook and Spyder, just install anaconda.

Software Requirments
* Python
* Pandas
* NumPy
* Flask
* Seaborn
* Matplot
* Sklearn
* Oversampling(SMOTETomek)

 
## Future Scope

* Optimize Flask app.py
* Add some Features
* Front-End 



