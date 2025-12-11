import pandas as pd
#pandas라는 사람이 만든 분석 도구를 가져와서 pd라고 저장.


# Titanic 데이터 불러오기
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# dataframe = = “csv 파일을 읽어서 df라는 DataFrame에 저장한다”는 뜻.
# pd.read_csv : CSV 파일 → pandas DataFrame으로 변환


print(df.head())
#df.head() showing from the first to five lines in the dataset. df.head(10) -- we can also use like this.

print(df.info())
print(df.describe())
#이건 모든 숫자형 컬럼에 대해:
# count (데이터 개수)
# mean (평균)
# std (표준편차)
# min
# 25%, 50%, 75%
# max

df['Age']
df[['Name', 'Sex', 'Age', 'Fare']]
print(df['Age'].head(10))
print(df[['Name', 'Age', 'Fare']].head())


df[df['Age'] > 60]
df[df['Sex'] == 'female']

print(df[(df['Sex'] == 'female') & (df['Survived'] == 1)])
print(df[df['Survived'] == 1].head())
print(df[df['Age'] >= 70])


df.sort_values('Fare', ascending=False).head()
df.sort_values('Age', ascending=True).head()

print(df[df['Age'] > 30].head())

print(df.isnull().sum())

df = df.drop(columns=['Cabin'])  

print(df.head())

age_median = df['Age'].median()  # Find the median

df['Age'] = df['Age'].fillna(df['Age'].median())    # OR
df['Age'] = df['Age'].fillna(age_median)

print(df['Embarked'].value_counts())

print(df['Embarked'].mode())

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # [o] is the index number of the series.

print(df.isnull().sum())


print(df['Sex'].value_counts())


import matplotlib.pyplot as plt
import seaborn as sns



# plt.hist(df['Age'], bins=30)  # If you increase the number of bins, the histogram shows more detailed bars.
# plt.xlabel("Age")
# plt.ylabel("Count")
# plt.title("Age Distribution")
# # plt.show()


# plt.figure(figsize=(6, 4))
# sns.boxplot(x=df['Fare'])
# plt.title("Fare Boxplot")
# # plt.show()


plt.figure(figsize=(6,6))
plt.scatter(df['Age'], df['Fare'], alpha=0.5)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.show()