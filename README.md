# MEXICO CITY ECOBIKES MACHINE LEARNING PROJECT


![EcobiciLogo](https://github.com/user-attachments/assets/3bff4646-ce8d-4508-a367-71a824323822)


![ecobici_01-min](https://github.com/user-attachments/assets/8eb28503-ce71-4dba-a0c7-a591b8e18344)

# INTRODUCTION

Launched in 2010 with 85 stations and 1,114 bicycles
Operated by Mexico City's government through the Ministry of Mobility
Goal: To integrate bicycles into the public transport system as a sustainable and efficient option

**2025 STATS**


> [!TIP]
> 
> 689 stations
> 
> 9,300 bicycles
>
> 70,000 average weekday trips
>
> Over 165,000 active yearly memberships
>
> Coverage: Active in 4 boroughs: Cuauhtémoc, Miguel Hidalgo, Benito Juárez, and Coyoacán


# 1ST PART.- DATA VISUALIZATION WITH TABLEAU

![Screenshot 2025-04-04 at 9 06 05 p m](https://github.com/user-attachments/assets/845915e0-6e02-462e-a43b-2910887b342c)


We created some visualizations in Tableau to provide an initial analysis of which stations will be the largest in 2025, as well as to obtain some basic statistics.

You can find more detailed views of these visualizations at the following link:

https://public.tableau.com/app/profile/carlos.fernando.s.nchez.lozano/viz/Feb_2025_viz/Pick-UpsDashboard

# 2ND PART.- MACHINE LEARNING ALGORITHMS

In this section, we will use four different machine learning techniques, taking into account the data we have available, to address various areas of opportunity:

1. User Classification: Uses demographic data (gender and age) to predict user categories and usage patterns (for example, is a younger user more likely to use a bike at night?).
   
2. Route Analysis: We will attempt to create a profile of the most used routes and how they vary by time of day, which could help improve the station system.
  
3. Bicycle Demand Prediction: Analyzes pickup and drop-off patterns to predict which stations will require the most bikes at certain times of the day.

4. User Segmentation: Groups users into different segments based on their usage behavior, which can help with marketing campaigns or service improvements.


## 1. User Classification with Random Forest 

For the model we used demographic data (gender and age) to predict user categories and usage patterns like is a younger user more likely to use a bike at night?)

You can find the code to run this model on the folder Codes and the name of the file is Spark_RForest_Gcollab
In order to run this file you need to use the following csv that you download from this AWS Bucket:
https://mybucketbootcampjlg.s3.us-east-2.amazonaws.com/2025_02.csv

The model uses Spark in order to read the data.

In this model first we cleaned, normalized, and standardized prior to modeling

For this model we obtained a 96% accuracy

<img width="521" alt="Screenshot 2025-04-06 at 12 40 13 a m" src="https://github.com/user-attachments/assets/ac4cb774-d41b-4306-8efb-cb448bdb4787" />


## 2. Route Analysis with K Means Cluster model

For this model we sed the Kmeans method 

So following the same steps we first cleaned, normalized, and standardized prior to modeling

As some of the steps we calculated the clusters in order to get to the predicted results

<img width="700" alt="Screenshot 2025-04-06 at 12 53 32 p m" src="https://github.com/user-attachments/assets/1d762375-580b-4145-9a77-118a9a451a7b" />

![Screenshot 2025-04-06 at 1 14 25 p m](https://github.com/user-attachments/assets/dad5b393-446a-4763-ac90-4f068cb5fefb)



These are the TOP 10 most used predicted routes by the model :


<img width="1193" alt="Screenshot 2025-04-06 at 12 39 48 p m" src="https://github.com/user-attachments/assets/a3f750da-20e7-4006-a4b2-60f61ade137a" />



In this model the accuracy we got wasn't as good as on the 1st model.


Some of the results may be significant for these use cases:
Identification of high-demand areas. Areas with high concentrations of usage can be identified for the location of new stations or the adjustment of the size of current ones.

Bicycle redistribution. Understanding which stations tend to be used together or share usage patterns can help with transport logistics and bicycle redistribution.
Targeted marketing: Understanding the demographics and patterns of users who use stations in a cluster can inform more effective marketing campaigns.



# User Classification Linear Regression and Random Forest Models

These are some of the preliminary results

## Random Forest Model

![Screenshot 2025-03-30 at 9 38 50 p m](https://github.com/user-attachments/assets/92306cca-5a52-4d38-a7e6-11234007f16c)

## Gradient Boosting Classifier
![Screenshot 2025-03-30 at 9 39 12 p m](https://github.com/user-attachments/assets/3eb9ae15-de36-40ec-a92e-0d3c1b2f493c)

## 4. User Segmentation

5. ## Time duration

For this stage we used 6 different models in order to be able to compare results between them

1. Linear Regression
2. Ridge
3. Lasso Regression
4. Decision Tree Regressor
5. Random Forest Regressor
6. LGBM Regressor

<img width="1103" alt="Screenshot 2025-04-05 at 11 16 50 p m" src="https://github.com/user-attachments/assets/09a6ab52-fad0-4ff9-a941-01937bd867a9" />


<img width="1124" alt="Screenshot 2025-04-05 at 11 20 23 p m" src="https://github.com/user-attachments/assets/60f0714f-b771-4b0d-8358-4cc22afe7d67" />



## APPENDIX, CSV DATA JOINS 


