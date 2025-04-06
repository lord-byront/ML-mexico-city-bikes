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

In this model 
## 2. Route Analysis:

In this model we used 


# 4. User Segmentation



# Route Analysis K Means Cluster model

The data we are using contains a year's worth of trips at Mexico City stations.
The data contains 22 million rows representing trips made over a year.
In this first part, we will use the K-means machine learning method to identify different clusters using the geographic coordinates of the stations and the time of the routes to identify patterns. In the first case, we will use the pickup stations to identify different clusters.

In order to run this file you need to use the following csv that you download from this AWS Bucket:
https://mybucketbootcampjlg.s3.us-east-2.amazonaws.com/archivo_ordenado.csv




This are some of our results:

Pickup Stations:

![Screenshot 2025-03-29 at 6 27 26 p m](https://github.com/user-attachments/assets/a46d6b4a-f95f-4c99-967b-b76c2f71ccf8)

![Screenshot 2025-03-29 at 6 31 33 p m](https://github.com/user-attachments/assets/ce4091a0-7703-48a2-82cd-0283e92139e3)

End Stations:

![Screenshot 2025-03-30 at 4 24 28 p m](https://github.com/user-attachments/assets/89071681-3486-4dc1-be42-f57087ebe095)

![Screenshot 2025-03-30 at 4 25 06 p m](https://github.com/user-attachments/assets/d33d1c18-e4b1-4e65-a49d-b41ab54d25e7)


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


# Time duration

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


