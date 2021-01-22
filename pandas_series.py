import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# 1. 
# Use pandas to create a Series from the following data:

# Name the variable that holds the series fruits.

data_fruit = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruit_series = pd.Series(data_fruit)

# Run .describe() on the series to see what describe returns for a series of strings.

fruit_series.describe()

# Run the code necessary to produce only the unique fruit names.

fruit_series.unique()

# Determine how many times each value occurs in the series.

fruit_series.value_counts()

# Determine the most frequently occurring fruit name from the series.
# Kiwi

# Determine the least frequently occurring fruit name from the series.
 
fruit_series.value_counts().sort_values()

# Write the code to get the longest string from the fruits series.

fruit_series.str.len()

# Find the fruit(s) with 5 or more letters in the name.

fruit_series[fruit_series.str.len() > 5]

# Capitalize all the fruit strings in the series.

fruit_series.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization)

fruit_series.str.count('a')

# Output the number of vowels in each and every fruit.

fruit_series.str.count(r'[aeiou]')

# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

fruit_series[fruit_series.apply(lambda row: row.count('o')) >= 2]

# Write the code to get only the fruits containing "berry" in the name

fruit_series[fruit_series.str.contains('berry')]

# Write the code to get only the fruits containing "apple" in the name

fruit_series[fruit_series.str.contains('apple')]

# Which fruit has the highest amount of vowels?

fruit_series[fruit_series.str.count(r'[aeiou]').max()]

# 2.
# Use pandas to create a Series from the following data:

data_money = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

money_series = pd.Series(data_money)

# What is the data type of the series?

type(money_series)
#pandas.core.series.Series

# Use series operations to convert the series to a numeric data type.

money_num_series = money_series.str.replace("$","").str.replace(",","").astype(float)

#What is the maximum value? The minimum?

money_num_series.max(), money_num_series.min()

# Bin the data into 4 equally sized intervals and show how many values fall into each bin.

money_num_series.value_counts(bins = 4)

# Plot a histogram of the data. Be sure to include a title and axis labels.

money_num_series.value_counts(bins = 4).plot.barh(color='green', 
                                   width=1, 
                                   ec='black')


plt.title('Money Bins')
plt.xlabel('Amount in bin')
plt.ylabel('USD ($)')

# reorder y-axis of horizontal bar chart
plt.gca().invert_yaxis()
plt.show()


# 3 
# Use pandas to create a Series from the following exam scores:

scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

exam_scores = pd.Series(scores)

#What is the minimum exam score? The max, mean, median?

exam_scores.describe()

# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
# Plot a histogram of the scores.
# Convert each of the numbers above into a letter grade. 
# For example, 86 should be a 'B' and 95 should be an 'A'.

#define bin edges
bin_edges = [0, 60, 70, 80, 90, 100]

# bin labels
bin_labels = ['F', 'D', 'C', 'B', 'A']

# CUT() to put everything in their bins and plot the graph
pd.cut(exam_scores, bins=bin_edges, labels=bin_labels).value_counts().sort_index().plot.bar(color='Green', width=1, ec='black')


plt.title('Exam Score Distribution')
plt.xlabel('Letter Grade')
plt.ylabel('Number of Students')

plt.xticks(rotation='horizontal')
plt.gca().invert_xaxis()

plt.show()

# Write the code necessary to implement a curve. 
# (I.e. that grade closest to 100 should be converted to a 100, 
# and that many points should be given to every other score as well.)

# Applying the curve
curve = 100 - exam_scores.max()
exam_scores_with_curve = exam_scores + curve

# CUT() to put everything in their bins and plot the graph
pd.cut(exam_scores_with_curve, bins=bin_edges, labels=bin_labels).value_counts().sort_index().plot.bar(color='Green', width=1, ec='black')


plt.title('Exam Scores with Curve Applied Distribution')
plt.xlabel('Letter Grade')
plt.ylabel('Number of Students')

plt.xticks(rotation='horizontal')
plt.gca().invert_xaxis()

plt.show()

# 4 
# Use pandas to create a Series from the following string:

string_series.describe()

# What is the most frequently occuring letter? Least frequently occuring?

string_series[string_series.value_counts().max()], string_series[string_series.value_counts().min()] 

# How many vowels are in the list?

sum(string_series.str.count(r'[aeiou]'))

# How many consonants are in the list?

len(string_series) - sum(string_series.str.count(r'[aeiou]'))

# Create a series that has all of the same letters, but uppercased

string_series.str.upper()

# Create a bar plot of the frequencies of the 6 most frequently occuring letters.

string_series.value_counts().head(6).plot.bar()

plt.title('Top 6 Letters and Their Frequency')
plt.xlabel('Letter')
plt.ylabel('Frequency')

plt.xticks(rotation='horizontal')

plt.show()

# 5.
# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

pfruits = pd.Series(fruits)
num_series = pd.Series(numbers)

# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]

pfruits.str.upper()

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

pfruits.str.capitalize()

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

pfruits[pfruits.str.count(r'[aeiou]') > 2]

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

pfruits[pfruits.str.count(r'[aeiou]') == 2]

# Exercise 5 - make a list that contains each fruit with more than 5 characters

pfruits[pfruits.str.len() > 5]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

pfruits[pfruits.str.len() == 5]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

pfruits[pfruits.str.len() < 5]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

pfruits.str.len()

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

pfruits[pfruits.str.contains('a')]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

num_series[num_series % 2 == 0]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

num_series[num_series % 2 != 0]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

num_series[num_series > 0]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

num_series[num_series < 0]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

num_series[(num_series <= -10) | (num_series >= 10)]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

num_series ** 2

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

num_series[(num_series < 0) & (num_series % 2 != 0)]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

num_series + 5



