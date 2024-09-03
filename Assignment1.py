# ---------------------------------------------------------------------------------------------------------------------
# Name:        Assignment1.py
# Purpose:     Assignment Script for Assignment 1 that only includes questions and tasks. This version of the
#               assignment is recommended for students with a programming background and those who feel comfortable
#               coding in Python.
# Author:      Dr. Yoganand Korgaonkar
# Student Name:
# ---------------------------------------------------------------------------------------------------------------------
print("\n ##### ASSIGNMENT 1 ##### \n")  # Ignore this line
#######################################################################################################################
# TODO Q1: Your Name
#   In this question, you will create a variable and use string formatting methods to print out certain strings.
#   (a) Create a variable to store your first & last name as a single string.
#   (b) Print the contents of the variable from (a).
#   (c) Print your first & last name using the variable from (a) using the + operator for concatenation.
#   (d) Print your first & last name using the variable from (a) using the .format() method for concatenation.
#   (e) Print your first & last name using the variable from (a) using f-strings for concatenation.
#       Expected Output: Your print output for (c), (d) & (e) should look like this:
#       <bol>My name is Yoga Korgaonkar!<eol>
#       IMP: Output should print out three times with your name instead of mine.
#   Note: <bol> indicates "beginning of line", and <eol> indicates end of line. These are indicative of where
#   the line starts and where it ends. You do not have to print <bol> & <eol> in the output.
print("\n ##### Question 1 ################################################################### \n")  # Ignore this line
# Write your code below



# End Q1
#######################################################################################################################
# TODO Q2: Math Operations
#   In this question, you will perform math operations.
#   Given the four variables below (var_one, var_two, var_three & var_four) perform the following tasks.
#   (a) Determine and print the data type of each variable using the type() and print() functions.
#   (b) Create a new variable to store the result of adding all four numbers.
#   (c) Print the addition result in the following format.
#       Expected Output: Your print output for (b) should look like this:
#       <bol>Addition: 323 + 543.78 + 43 + 98.22 = 1008.0<eol>
#       IMP: Do not type the numbers, use only variables.
#   (d) Create a new variable to store the result of multiplying all four numbers.
#   (e) Print the multiplication result in the following format.
#       Expected Output: Your print output for (b) should look like this:
#       <bol>Multiplication: 323 * 543.78 * 43 * 98.22 = 741812484.4524<eol>
#       IMP: Do not type the numbers, use only variables.
#   Note: <bol> indicates "beginning of line", and <eol> indicates end of line. These are indicative of where
#   the line starts and where it ends. You do not have to print <bol> & <eol> in the output.
print("\n ##### Question 2 ################################################################### \n")  # Ignore this line
# Given variables. Do not modify these. Use these variables in your operations.
var_one = 323
var_two = 543.78
var_three = "43"
var_four = "98.22"

# Write your code below



# END Q2
#######################################################################################################################
# TODO Q3:  Strings & Lists
#   In this question, you will manipulate strings and lists.
#   Given the string literal stored in variable ws_path below, perform the following tasks.
#   a) Convert the given string to a list by splitting it on \\ and store the list in a new variable. Print the
#   contents of this new variable.
#   b) Access the following strings from the list using the correct index, and store it into a new variable.
#   Convert the cases as shown below as you access the items from the list. Print the contents of each new
#   variable.
#       (i) environmental (convert to all uppercase, i.e. ENVIRONMENTAL)
#       (ii) watersheds (convert to title case, i.e. Watersheds)
#       (iii) Assignment1.GDB (convert to all lowercase, i.e. assignment1.gdb)
#       IMP: Do not type out these words. Use the variable that stores the list with indices to access the list items.
#   c) Recreate the path shown below by concatenating all the modified strings using variables and store it in a
#   new variable. Print the contents of this new variable.
#       Expected Output: Your print output for (c) should look like this:
#       <bol>c:\workspace\gist\data\assignment1.gdb\ENVIRONMENTAL\Watersheds<eol>
#   IMP: Do not type out these words. Use variables to access these strings.
#   Note: <bol> indicates "beginning of line", and <eol> indicates end of line. These are indicative of where
#   the line starts and where it ends. You do not have to print <bol> & <eol> in the output.
print("\n ##### Question 3 ################################################################### \n")  # Ignore this line
# Given string stored in a variable. Do not modify this. Use this variable in order to complete all tasks.
ws_path = "c:\\workspace\\gist\\data\\Assignment1.GDB\\environmental\\watersheds"

# Write your code below



# END Q3
#######################################################################################################################
# TODO Q4: Lists
#   In this question, you will perform various operations on a list.
#   (a) Create a list with your first and last name as two items and store it in a variable. Print the list.
#   (b) Remove your last name from the list and store it in a variable. Print the list.
#   (c) Append the name of your city to the list. Print the list.
#   (d) Use the variable from (b) to insert your last name into the list at the second position, i.e. between your first
#     name and your city. Print the list.
#   (e) Print the index of your last name from the list.
print("\n ##### Question 4 ################################################################### \n")  # Ignore this line
# Write your code below



# END Q4
#######################################################################################################################
# TODO Q5: Formatting Strings
#   In this question, you will create variables, and manipulate/format the strings that they contain.
#   (a) Create a new variable to store your first name as a string in all lowercase.
#   (b) Create a new variable to store your last name as a string in all lowercase.
#   (c) Create a new variable to store a list with names of three different movies as items.
#   (d) Using variables from (a), (b) & (c), create and print the following. Your final output should display your
#   information from and you must preserve quotes, case as well as punctuation as they appear in the given output.
#   Do not modify the original variables created in (a), (b) and (c) for this question.
#       <bol>YOGA's last name is "Korgaonkar".<eol>
#       <bol>Here are my movies:<eol>
#       <bol> # |                       Movies |<eol>
#       <bol> - | ---------------------------- |<eol>
#       <bol> 1 |                   <Movie #1> |<eol>
#       <bol> 2 |                   <Movie #2> |<eol>
#       <bol> 3 |                   <Movie #3> |<eol>
#   The second column for the last five lines must be as wide as the longest name of your chosen movies.
#   Note: <bol> indicates "beginning of line", and <eol> indicates end of line. These are indicative of where
#   the line starts and where it ends. You do not have to print <bol> & <eol> in the output.
print("\n ##### Question 5 ################################################################### \n")  # Ignore this line
# You may write your code below this line



# END Q5
#######################################################################################################################
# TODO Q6: Concatenation of Paths
#   In this question, you will perform string concatenation to create paths.
#   Given the variables that store paths and filenames, create a new variable to store each of the following paths
#   using string concatenation. Print each variable.
#   a) c:/workspace/gist/python/data/r_elev
#   b) c:/workspace/gist/python/data/r_slope
#   c) c:/workspace/gist/python/data/r_lc
#   d) c:/workspace/gist/python/data/parcels.shp
#   e) c:/workspace/gist/python/data/census.dbf
print("\n ##### Question 6 ##### \n")  # Ignore this line
# Given variables. Do not modify these. Use these variables to perform all tasks.
var_workspace = "c:/workspace/gist/python/data"
list_of_rasters = ["r_elev", "r_slope", "r_lc"]
parcel_shp = "parcels.shp"
var_table = "census.dbf"

# You may write your code below this line



# End Q6
#######################################################################################################################
# END OF ASSIGNMENT 1
#######################################################################################################################
