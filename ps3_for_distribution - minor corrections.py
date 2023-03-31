# Problem Set 3

# This problem set will ask you to complete some basic data manipulation
# tasks using Python. Insert your code after each question. Submit a .py file
# as your submission.

# The problem set is graded using the following general benchmarks.

# A: 100% - perfect or very nearly perfect execution. Task completion aligns 
# with expected results with only trivial exceptions. The student has excellent
# command of the substance of the material.

# A-: 92% - There are more than trivial errors in the assignment, but the 
# assignment is mostly successful. The student understands the main concepts 
# and problem-solving techniques, but has some gaps in their understanding or execution.

# B+: 89% - The assignment is partially successful, but there are multiple 
# substantive errors in task completion spread throughout the assignment. 
# The student is not completely lost, but they require clarification of 
# concepts or methods.

# B: 86% - The assignment is not successful. The student exhibits poor 
# understanding of the methods being used. The student made an effort, but the 
# work is flawed and it is clear the student should seek additional support.

# B-: 82%- The assignment is seriously flawed, suggesting significant need for 
# remediation. The student has not gone in an entirely wrong or unproductive 
# direction, but the student needs to change their study habits or seek further
# support to clarify key concepts and techniques.

# C: 75% - Very little if anything is correct, suggesting failure to develop 
# fundamental proficiency with the subject matter.

# Question 1

# Use mathematical operators to perform addition, subtraction, multiplication,
# and division with Python. Each time, assign the results of the operation to 
# a new object and print the object.

# Question 2

# Create a character string in Python with the word "banana". Save
# the string to an object. Use the count() method to return the number of times
# the letter "a" is in the string. Use print() to print that value to the console.
# Hint: to see the methods associatd with a character string object, check out:
# https://www.w3schools.com/python/python_ref_string.asp

# Question 3

# Create three different objects in Python. Make one a tuple, make one a list,
# and make one a dict. Make sure each object has more than three values in it.
# Otherwise, create these objects with any content you like.

# Question 4

# Create an object in python named "start" and make it equal to 0.
# Create a list in Python called "my_values" and have it contain the values
# 10, 15, 20, and 25.
# Write a for loop in python that iterates over my_values and adds these
# to the object "start."
# After you run the code, the value of "start" should be 70.

# Question 5

# Create a list called "list5" with five elements. Use indexing to extract the 
# middle three elements.

# Question 6

# Write a function in Python that will accept as an argument a list with 5 items,
# removes the last item in the list, and returns the shortened list.

# Question 7

# Now, modify the function you wrote in question 6 so that it will remove the last
# item in a list of any length. To do this, you may want to use the len() function
# in Python (https://www.w3schools.com/python/ref_func_len.asp).

# Question 8

# Import the pandas library. Using a dict as a starting point, create a dataframe
# with two columns and 5 rows. The first column should have textual data and second 
# should have numeric data. Name the columns whatever you like and populate the 
# cells with whatever character and numeric values you like.

# Question 9

# Print the first column from the dataframe you created in Question 8.

# Question 10

# Add a column to the dataframe you created in Question 8, called "col3". The
# cells in the rows can have any value you like.

# Question 11

# Drop the column you added in Question 10

# Question 12

# Use the sum() method to calculate the sum of values of the second column
# (the one with numeric data)

# Question 13

# I have posted to GitHub several datasets. Use the code I include below to
# load the ps3_dat.csv dataset. Then, use logical operators to filter
# the data, creating a new object named new_dat that contains the rows where 
# the values in the second column are less than 50.

ps3_dat="https://raw.githubusercontent.com/jhudap/pdm_data/main/ps3_dat.csv"

dat=pd.read_csv(ps3_dat)

# Question 14

# Sort the item-cost dataframe (from question 13) in descending order by cost. Hint: You may want
# to look through the DataFrame methods to find an appropriate method.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

# Question 15

# Rename columns of the data frame so that item is renamed to inventory

# Question 16

# On GitHub, there is a .csv file called "grouped_data.csv". The code below
# loads the data.

# Notice that there is missing data in the "payment_amount" columns in rows where
# claim_paid equals "no." Use a pandas method to replace the NaN values with
# zero. 

# Hint: You may want to look through the DataFrame methods to find an appropriate method.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

claims_data_url="https://raw.githubusercontent.com/jhudap/pdm_data/main/claims_data.csv"

claims_data=pd.read_csv(claims_data_url)

# Question 17

# Use a pandas method to provide a frequency count of the different
# colors of cars in the table.

# Hint: You may want to look through the DataFrame methods to find an appropriate method.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

# Question 18

# Using grouping, calculate the mean values of cars from NJ and NY.

# Question 19

# Another .csv file has insurance premiums for each car in the table.
# Merge the two tables using the claim_id column. Note: the claim_id column is
# named slightly differently in the two files. You'll have to deal with that.

premiums_url="https://raw.githubusercontent.com/jhudap/pdm_data/main/premiums.csv"

premiums=pd.read_csv(premiums_url)

# Question 20

# This question will require a tiny bit of research on your part.

# Pandas has basic visualization tools. Use a pandas method to create 
# a scatterplot using the merged data from question 19. Put vehicle_cost on the
# x axis and premium on the y axis.







