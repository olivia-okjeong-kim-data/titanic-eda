# Titanic Data Analysis (Exploratory Data Analysis)

This project explores the Titanic dataset using Python, pandas, seaborn, and matplotlib.  
It was created to practice fundamental data analysis skills such as cleaning data, exploring distributions, and interpreting visual patterns.

---

## 1. Dataset Overview

The dataset contains information about 891 passengers, including:

- Demographics (Age, Sex)
- Ticket class (Pclass)
- Family information (SibSp, Parch)
- Fare
- Embarkation port (Embarked)
- Survival outcome

Some variables contain missing values, especially **Age**, **Cabin**, and **Embarked**, so a bit of preprocessing is required before analysis.

---

## 2. Data Cleaning

### Age  
The `Age` column had many missing values.  
I filled these using the **median**, since the age distribution is right-skewed and the median is more robust than the mean.

### Embarked  
Two missing values were replaced with the **mode ('S')**, which is the most common embarkation port.

### Cabin  
Most values were missing, so this column was removed from the analysis.

After cleaning, the dataset contained no missing values.

---

## 3. Visualizations and Interpretation

### 3.1 Histogram — Age Distribution  
The histogram shows that most passengers were between **20 and 40 years old**, indicating a relatively young population.  
There is a noticeable peak around **age 28**, and the distribution is **right-skewed**, with fewer older passengers extending toward ages 60–80.

### 3.2 Boxplot — Fare  
The boxplot reveals that most passengers paid **very low fares**, which explains why the entire box is concentrated on the left side.  
The median fare is also low, around 14.  
In contrast, there are many high-value outliers between 100 and 500, showing that a small number of passengers paid significantly more (likely first-class).  
This makes the Fare distribution strongly right-skewed.

### 3.3 Scatterplot — Age vs. Fare  
The scatterplot shows **no clear correlation** between Age and Fare.  
Most passengers, regardless of age, paid fares below 150.  
A few outliers appear around 500, but overall, the points are clustered in the lower-left area, suggesting that age did not strongly influence ticket price.

---

## 4. Tools Used

- Python  
- pandas  
- seaborn  
- matplotlib  
- VS Code  
- Git & GitHub  

---

## 5. Project Files

titanic-eda/
│── 10122025.py
│── age_hist.png
│── fare_boxplot.png
│── scatter_age_fare.png
└── README.md

---

## Summary

This project demonstrates basic techniques of exploratory data analysis, including handling missing data, visualizing distributions, identifying outliers, and summarizing trends.  
It is a good foundation for future machine learning or modeling work.
