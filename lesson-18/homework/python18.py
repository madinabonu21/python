import pandas as pd 


df = pd.read_csv('tackoverflow_qa.csv')

# 1.Find all questions that were created before 2014


df['creationdate']= pd.to_datetime(df['creationdate'], errors= 'coerce')

filtered_df = df[df['creationdate'] < '2014-01-01']

# print (filtered_df)

# 2.Find all questions with a score more than 50

filtered_score = df[df['score']> 50 ]
# print(filtered_score)

# 3.Find all questions with a score between 50 and 100

score_between = df[df['score'].between(50,100)]
# print(score_between)

# 4.Find all questions answered by Scott Boston

answer_by_scott = df[df['ans_name'] == 'Scott Boston']

# print (answer_by_scott)


# 5.Find all questions answered by the following 5 users

users = ['Scott Boston', 'unutbu', 'jezrael', 'Alexander', 'John Doe']

filtered = df[df['ans_name'].isin(users)]
questions = filtered[['id', 'title', 'quest_name']].drop_duplicates()

print(questions)
# 6.Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

mask_date = (df['creationdate'] >= '2014-03-01') & (df['creationdate'] <= '2014-10-31')
mask_user = df['ans_name'] == 'unutbu'
mask_score = df['score'] < 5
filtered_question = df[mask_date & mask_user & mask_score]
# print(filtered_question)


# 7.Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

between_5_and_10 = df['score'].between(5,10)
view_count_greater = df['viewcount'] > 10000

filtered = df[between_5_and_10 | view_count_greater]
# print(filtered)

# 8.Find all questions that are not answered by Scott Boston
answer_by_scott = df[df['ans_name'] != 'Scott Boston']


# Homework 3:

# Titanic data set, stored as CSV. The data consists of the following data columns:

import pandas as pd 

titanic_df = pd.read_csv("titanic.csv")


# 1.Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

mask = (titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1) & (titanic_df['Age'].between(20, 30))

female_class1_20_30 = titanic_df[mask]

# print(female_class1_20_30)

# 2.Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

fare_greater_than_100 = titanic_df[titanic_df['Fare'] >100]
# print(fare_greater_than_100)

# 3.Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

survived_alone = titanic_df[(titanic_df['Survived'] == 1) & (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)]

# print(survived_alone)

# 4.Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

df_filtered_4 = titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50)]
# print(df_filtered_4)


# 5.Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

df_filtered_5 = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]
# print(df_filtered_5)

# 6.Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

df_under15_nonsurvived = titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)]

# print(df_under15_nonsurvived)

# 7.Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

df_cabin_fare200 = titanic_df[titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)]

# print(df_cabin_fare200)

# 8.Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

df_odd_id = titanic_df[titanic_df['PassengerId'] % 2 == 1]

# print(df_odd_id)

# 9.Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

df_unique_ticket = titanic_df[~titanic_df['Ticket'].duplicated(keep=False)]

# print(df_unique_ticket)

# 10.Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

df_miss_class1 = titanic_df[(titanic_df['Name'].str.contains('Miss', case=False, na=False)) & (titanic_df['Pclass'] == 1)]

# print(df_miss_class1)
