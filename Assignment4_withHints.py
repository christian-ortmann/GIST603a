# ---------------------------------------------------------------------------------------------------------------------
# Name:        Assignment4_withHints.py
# Purpose:     Assignment Script for Assignment 4 that includes questions and tasks as well as hints to guide you
#               through writing code one line at a time. This script is recommended for beginners with no prior
#               programming experience.
# Author:      Dr. Yoganand Korgaonkar
# Student Name:
# ---------------------------------------------------------------------------------------------------------------------
print("\n ##### ASSIGNMENT 4 ##### \n")  # Ignore this line
#######################################################################################################################
# TODO Q1: Copy Data
#   In this question, you will create a new geodatabase and a feature dataset and copy over feature classes into them
#   before using cursors on them in the remaining questions.
#   (a) Create a folder called "A4_Results" on your computer. You can do this manually or use os.mkdir() in Python.
#   (b) Create a geodatabase called Assignment4.gdb in A4_Results using an appropriate ArcGIS geoprocessing tool.
#   (c) Create a feature dataset called "FeatureClasses" inside Assignment4.gdb using an appropriate ArcGIS
#   geoprocessing tool. Set the spatial reference to NAD 1983 StatePlane Texas Central FIPS 4203 (US Feet).
#   (d) Copy the following feature classes from ExploringSpatialData\Austin.gdb to Assignment4.gdb\FeatureClasses
#       (i) Facilities\facilities
#       (ii) Facilities\hospitals
#       (iii) Facilities\schools
#       (iv) Parks\restrooms
#       (v) Parks\tennis_courts
#       (vi) Parks\trails
print("\n ##### Question 1 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Import the os module

# Q1 (a) New variable stores the path to new folder called "A4_Results" on your computer

# Q1 (a) Create the folder using os.mkdir()

# Q1 (a) Print a message that it is created

# Q1 (b) Create a geodatabase called Assignment4.gdb in A4_Results using the CreateFileGDB tool and assign the result
# object to a new variable called gdb_result

# Q1 (c) Create a feature dataset called "FeatureClasses" inside Assignment4.gdb using the CreateFeatureDataset tool and
# assign the result to object to a new variable called fd_result. Set the spatial reference to NAD 1983 StatePlane Texas
# Central FIPS 4203 (US Feet)

# Q1 (c) Print ALL geoprocessing messages using the result object stored in the variable fd_result

# Q1 (d) New variable stores a list of all the given feature dataset names - Facilities and Parks

# Q1 (d) New variable stores a list of all the given feature class names - facilities, hospitals, schools, restrooms,
# tennis_courts and trails

# Q1 (d) Use a for loop on the list of feature dataset names

    # Set the arcpy environment property for workspace to the feature dataset in the iteration. Remember to concatenate
    # the full path to the feature dataset.

    # New variable stores a list of feature class names returned by an appropriate arcpy list function

    # Use a for loop on the list of feature class names

        # Check if the feature class name from the iteration is in the list of feature class names to be copied.

            # Print the name of the feature class

            # Copy the feature class to "A4_Results\Assignment4.gdb\FeatureClasses" using the CopyFeatures tool. The
            # output should have the same name and assign the result object to a variable called cf_result.

            # Print ALL geoprocessing messages using the result object stored in the variable cf_result

# End Q1
#######################################################################################################################
# TODO Q2: Search cursors - Retrieving Records
#   In this question, you will use search cursors and where clauses to retrieve information from the attribute tables of
#   various feature classes.
#   (a) Print the names, addresses and phone numbers of all hospitals in Austin that contain the word "Hospital" in
#   their name using the "hospitals" feature class.
#   (b) Print the names of the parks that have tennis courts without lights using the "tennis_courts" feature class.
print("\n ##### Question 2 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Set the arcpy environment property for workspace to the "A4_Results\Assignment4.gdb\FeatureClasses" feature dataset

# Q2 (a) New variable stores the where clause to search for the string "Hospital" in the "NAME" field

# Q2 (a) Print the where clause to verify if the quotations are correct.

# Q2 (a) Use the with statement to set up a search cursor on the hospitals feature class. Provide the "NAME", "ADDRESS"
# and the "PHONE_NUMB" fields to the cursor to retrieve the names, addresses and phone numbers respectively.

    # Use a for loop on the iterator of the records in the cursor

        # Print the name and address of the hospital using the variable of the iteration

# Q2 (b) New variable stores the where clause to search for the string "no" in the "LIGHTS" field

# Q2 (b) Print the where clause to verify if the quotations are correct.

# Q2 (b) Use the with statement to set up a search cursor on the tennis_courts feature class. Provide the "PARK_NAME"
# field to the cursor to retrieve the names of the parks.

    # Empty list will store the names of the park without lights. Using this list to only store unique names.

    # Use a for loop on the iterator of the records in the cursor

        # Check if the name of the park does not exist in the list

            # Append the name of the park to the list

    # Use a for loop on the list of park names without lights

        # Print the name of the parks

# End Q2
#######################################################################################################################
# TODO Q3: Update Cursors - Updating Records
#   In this question, you will use update cursors to update the attribute table of the "schools" feature class.
#   (a) Rename all high school names so that their names end with "HIGH SCHOOL". Search for "HIGH", "HS" and "H S".
#   Print the total count of records that were updated.
#   (b) Rename all middle school names so that their names end with "MIDDLE SCHOOL". Search for "MIDDLE", and "M S".
#   Print the total count of records that were updated.
#   (c) Rename all elementary school names so that their names end with "ELEMENTARY SCHOOL". Search for "ELEMENTARY" and
#   "EL". Print the total count of records that were updated.
#   NOTE: The field "CAMPNAME" stores the name of the school campuses in the "schools" feature class.
print("\n ##### Question 3 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Set the arcpy environment property for workspace to the "A4_Results\Assignment4.gdb\FeatureClasses" feature dataset

# Three new variables will store the count of each type of school updated later in the code



# Use the with statement to set up an update cursor on the schools feature class. Provide the "CAMPNAME"
# field to the cursor to retrieve the names of the schools.

    # Use a for loop on the iterator of the records in the cursor

        # Q3 (a) Check if the name of the school ends with "HIGH"

            # Use the .replace() method to replace it with "HIGH SCHOOL"

            # Increment the counter

        # Q3 (a) Check if the name of the school ends with "HS"

            # Use the .replace() method to replace it with "HIGH SCHOOL"

            # Increment the counter

        # Q3 (a) Check if the name of the school ends with "H S"

            # Use the .replace() method to replace it with "HIGH SCHOOL"

            # Increment the counter

        # Q3 (b) Check if the name of the school ends with "MIDDLE"

            # Use the .replace() method to replace it with "MIDDLE SCHOOL"

            # Increment the counter

        # Q3 (b) Check if the name of the school ends with "M S"

            # Use the .replace() method to replace it with "MIDDLE SCHOOL"

            # Increment the counter

        # Q3 (c) Check if the name of the school ends with "ELEMENTARY"

            # Use the .replace() method to replace it with "ELEMENTARY SCHOOL"

            # Increment the counter

        # Q3 (c) Check if the name of the school ends with "EL"

            # Use the .replace() method to replace it with "ELEMENTARY SCHOOL"

            # Increment the counter

# Print the total count of updated records for each type of school using the three counter variables



# End Q3
#######################################################################################################################
# TODO Q4: Update Cursors - Deleting Records
#   In this question, you will use update cursors to delete records in feature classes representing parks in Austin.
#   (a) Delete all records referencing Patterson park in restrooms, tennis_courts and trails feature classes.
#   (b) Delete all records referencing Westenfield park in restrooms, tennis_courts and trails feature classes.
#   (c) Print the total count of features remaining in all of these feature classes using the GetCount tool.
print("\n ##### Question 4 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Set the arcpy environment property for workspace to the "A4_Results\Assignment4.gdb\FeatureClasses" feature dataset

# New variable stores a list of the three feature class names - restrooms, tennis_courts and trails

# New variable stores a list of the two park names that will be deleted - Patterson and Westenfield

# Use a for loop on the list of feature class names

    # Use a for loop on the list of park names that will be deleted

        # New variable stores the where clause to search for the park name in the "PARK_NAME" field

        # Use the with statement to set up an update cursor on the feature class in the iteration. Provide the
        # "PARK_NAME" field to the cursor to retrieve the names of the park

            # Use a for loop on the iterator of the records in the cursor

                # Delete the row using the .deleteRow() method

    # Execute the Get Count tool using the given parameters and assign the result object to a variable called gc_result

    # Print the number of features using the result object stored in gc_result

# End Q4
#######################################################################################################################
# TODO Q5: Search cursor and CSV file
#   In this question, you will retrieve information using a search cursor and write this information into a CSV file
#   (a) Using a search cursor on the facilities feature class and the csv.DictWriter class, create a CSV file called
#   "AustinLibraries.csv" in the A4_Results folder that contains the X and Y coordinates, names and addresses of all
#   libraries.c
#   NOTE: The CSV file should contain four columns with names: X_COORD, Y_COORD, LIB_NAME, LIB_ADDRESS
#   (b) Using csv.DictReader, print the contents of the AustinLibraries.csv file.
print("\n ##### Question 5 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Import the csv module

# New variable stores the path and name for the "AustinLibraries.csv" file in your "A4_Results" folder

# Use the with statement to open the AustinLibraries CSV file in write mode.

    # New variable stores the list of column names for the CSV file - X_COORD, Y_COORD, LIB_NAME and LIB_ADDRESS

    # New variable stores a DictWriter object for the CSV file with the above column names

    # Write the column names to the CSV file

    # New variable stores a list of field names to provide to the search cursor - SHAPE@XY, FACILITY_N and FACILITY_A

    # New variable stores the where clause to search for the attribute "LIBRARY" in the "FACILITY_T" field

    # Use the with statement to set up a search cursor on the facilities feature class.

        # Use a for loop on the iterator of the records in the cursor

            # New variable stores the x coordinate from the record

            # New variable stores the y coordinate from the record

            # New variable stores the name of the library

            # New variable stores the address of the library

            # New variable stores a dictionary with 4 key-value pairs corresponding to the 4 columns in the CSV file

            # Write the above dictionary as a row into the CSV file using the .writerow() method

# Use the with statement to open the AustinLibraries CSV file in read mode.

    # New variable stores a DictReader object for the CSV file

    # Use a for loop to iterate over each row in the DictReader object

        # New variable stores the x coordinate from the row

        # New variable stores the y coordinate from the row

        # New variable stores the name of the library from the row

        # New variable stores the address of the library from the row

        # Print the contents of the above four variables

# END Q5
#######################################################################################################################
# END OF ASSIGNMENT 4
#######################################################################################################################
