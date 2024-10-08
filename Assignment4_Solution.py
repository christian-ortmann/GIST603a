# ---------------------------------------------------------------------------------------------------------------------
# Name:        Assignment4_Solution.py
# Purpose:     Solution Script for Assignment 4
# Author:      Dr. Yoganand Korgaonkar
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
import arcpy
# Import the os module
import os

print("\n ### Q1 (a) ### - os.mkdir() \n")  # Ignore this line
# Q1 (a) New variable stores the path to new folder called "A4_Results" on your computer
folder_path = r"D:\workspace\PythonProgramming\Results\A4_Results"
# Q1 (a) Create the folder using os.mkdir()
os.mkdir(folder_path)
# Q1 (a) Print a message that it is created
print(f"Folder 'A4_Results' was created at {folder_path}")

print("\n ### Q1 (b) ### - CreateFileGDB \n")  # Ignore this line
# Q1 (b) Create a geodatabase called Assignment4.gdb in A4_Results using the CreateFileGDB tool and assign the result
# object to a new variable called gdb_result
gdb_result = arcpy.management.CreateFileGDB(out_folder_path=folder_path,
                                            out_name="Assignment4.gdb")
# Q1 (b) Print ALL geoprocessing messages using the result object stored in the variable gdb_result
print(gdb_result.getMessages())

print("\n ### Q1 (c) ### - CreateFeatureDataset \n")  # Ignore this line
# Q1 (c) Create a feature dataset called "FeatureClasses" inside Assignment4.gdb using the CreateFeatureDataset tool and
# assign the result to object to a new variable called fd_result. Set the spatial reference to NAD 1983 StatePlane Texas
# Central FIPS 4203 (US Feet)
fd_result = arcpy.management.CreateFeatureDataset(out_dataset_path=gdb_result,
                                                  out_name="FeatureClasses",
                                                  spatial_reference=arcpy.SpatialReference(2277))
# Q1 (c) Print ALL geoprocessing messages using the result object stored in the variable fd_result
print(fd_result.getMessages())

print("\n ### Q1 (b) ### - CopyFeatures \n")  # Ignore this line
# Q1 (d) New variable stores a list of all the given feature dataset names - Facilities and Parks
list_fds = ["Facilities", "Parks"]
# Q1 (d) New variable stores a list of all the given feature class names - facilities, hospitals, schools, restrooms,
# tennis_courts and trails
list_fcs = ["facilities", "hospitals", "schools", "restrooms", "tennis_courts", "trails"]
# Q1 (d) Use a for loop on the list of feature dataset names
for fd_name in list_fds:
    # Set the arcpy environment property for workspace to the feature dataset in the iteration. Remember to concatenate
    # the full path to the feature dataset.
    arcpy.env.workspace = f"D:\workspace\PythonProgramming\data\ExploringSpatialData\Austin.gdb\\{fd_name}"
    # New variable stores a list of feature class names returned by an appropriate arcpy list function
    fc_list = arcpy.ListFeatureClasses()
    # Use a for loop on the list of feature class names
    for fc_name in fc_list:
        # Check if the feature class name from the iteration is in the list of feature class names to be copied.
        if fc_name in list_fcs:
            # Print the name of the feature class
            print(f"Feature Class Name: {fc_name}")
            # Copy the feature class to "A4_Results\Assignment4.gdb\FeatureClasses" using the CopyFeatures tool. The
            # output should have the same name and assign the result object to a variable called cf_result.
            cf_result = arcpy.management.CopyFeatures(in_features=fc_name,
                                                      out_feature_class=f"{fd_result}\\{fc_name}")
            # Print ALL geoprocessing messages using the result object stored in the variable cf_result
            print(cf_result.getMessages())

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
import arcpy

# Set the arcpy environment property for workspace to the "A4_Results\Assignment4.gdb\FeatureClasses" feature dataset
arcpy.env.workspace = f"D:\workspace\PythonProgramming\Results\A4_Results\Assignment4.gdb\FeatureClasses"

print("\n ### Q2 (a) ### - hospitals \n")  # Ignore this line
# Q2 (a) New variable stores the where clause to search for the string "Hospital" in the "NAME" field
where_clause = f"\"NAME\" LIKE '%Hospital%'"
# Q2 (a) Print the where clause to verify if the quotations are correct.
print(f"Where Clause for hospitals: {where_clause}")
# Q2 (a) Use the with statement to set up a search cursor on the hospitals feature class. Provide the "NAME", "ADDRESS"
# and the "PHONE_NUMB" fields to the cursor to retrieve the names, addresses and phone numbers respectively.
with arcpy.da.SearchCursor("hospitals",["NAME", "ADDRESS", "PHONE_NUMB"], where_clause) as s_cursor:
    # Use a for loop on the iterator of the records in the cursor
    for row in s_cursor:
        # Print the name and address of the hospital using the variable of the iteration
        print(f"\t{row[0]} is located at {row[1]}. Phone: {row[2]}.")


print("\n ### Q2 (b) ### - tennis_courts \n")  # Ignore this line
# Q2 (b) New variable stores the where clause to search for the string "no" in the "LIGHTS" field
where_clause = f"\"LIGHTS\" = 'no'"
# Q2 (b) Print the where clause to verify if the quotations are correct.
print(f"Where Clause for tennis_courts: {where_clause}")
# Q2 (b) Use the with statement to set up a search cursor on the tennis_courts feature class. Provide the "PARK_NAME"
# field to the cursor to retrieve the names of the parks.
with arcpy.da.SearchCursor("tennis_courts",["PARK_NAME"], where_clause) as s_cursor:
    # Empty list will store the names of the park without lights. Using this list to only store unique names.
    list_no_lights = []
    # Use a for loop on the iterator of the records in the cursor
    for row in s_cursor:
        # Check if the name of the park does not exist in the list
        if row[0] not in list_no_lights:
            # Append the name of the park to the list
            list_no_lights.append(row[0])
    # Use a for loop on the list of park names without lights
    for row in list_no_lights:
        # Print the name of the parks
        print(f"\t{row} has no lights on tennis courts.")

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
import arcpy

# Set the arcpy environment property for workspace to the "A4_Results\Assignment4.gdb\FeatureClasses" feature dataset
arcpy.env.workspace = f"D:\workspace\PythonProgramming\Results\A4_Results\Assignment4.gdb\FeatureClasses"

# Three new variables will store the count of each type of school updated later in the code
hs_count = 0
ms_count = 0
es_count = 0
# Use the with statement to set up an update cursor on the schools feature class. Provide the "CAMPNAME"
# field to the cursor to retrieve the names of the schools.
with arcpy.da.UpdateCursor("schools", ["CAMPNAME"]) as u_cursor:
    # Use a for loop on the iterator of the records in the cursor
    for row in u_cursor:
        # Q3 (a) Check if the name of the school ends with "HIGH"
        if row[0].endswith(" HIGH"):
            # Use the .replace() method to replace it with "HIGH SCHOOL"
            row[0] = row[0].replace(" HIGH"," HIGH SCHOOL")
            # Increment the counter
            hs_count += 1
        # Q3 (a) Check if the name of the school ends with "HS"
        elif row[0].endswith(" HS"):
            # Use the .replace() method to replace it with "HIGH SCHOOL"
            row[0] = row[0].replace(" HS", " HIGH SCHOOL")
            # Increment the counter
            hs_count += 1
        # Q3 (a) Check if the name of the school ends with "H S"
        elif row[0].endswith("H S"):
            # Use the .replace() method to replace it with "HIGH SCHOOL"
            row[0] = row[0].replace("H S", "HIGH SCHOOL")
            # Increment the counter
            hs_count += 1
        # Q3 (b) Check if the name of the school ends with "MIDDLE"
        elif row[0].endswith(" MIDDLE"):
            # Use the .replace() method to replace it with "MIDDLE SCHOOL"
            row[0] = row[0].replace(" MIDDLE", " MIDDLE SCHOOL")
            # Increment the counter
            ms_count += 1
        # Q3 (b) Check if the name of the school ends with "M S"
        elif row[0].endswith("M S"):
            # Use the .replace() method to replace it with "MIDDLE SCHOOL"
            row[0] = row[0].replace("M S", "MIDDLE SCHOOL")
            # Increment the counter
            ms_count += 1
        # Q3 (c) Check if the name of the school ends with "ELEMENTARY"
        elif row[0].endswith(" ELEMENTARY"):
            # Use the .replace() method to replace it with "ELEMENTARY SCHOOL"
            row[0] = row[0].replace(" ELEMENTARY", " ELEMENTARY SCHOOL")
            # Increment the counter
            es_count += 1
        # Q3 (c) Check if the name of the school ends with "EL"
        elif row[0].endswith(" EL"):
            # Use the .replace() method to replace it with "ELEMENTARY SCHOOL"
            row[0] = row[0].replace(" EL", " ELEMENTARY SCHOOL")
            # Increment the counter
            es_count += 1
        # Update the row with the new school name using the .updateRow() method to save changes
        u_cursor.updateRow(row)

# Print the total count of updated records for each type of school using the three counter variables
print(f"Total high school names updated: {hs_count}")
print(f"Total middle school names updated: {ms_count}")
print(f"Total elementary school names updated: {es_count}")

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
import arcpy

# Set the arcpy environment property for workspace to the "A4_Results\Assignment4.gdb\FeatureClasses" feature dataset
arcpy.env.workspace = f"D:\workspace\PythonProgramming\Results\A4_Results\Assignment4.gdb\FeatureClasses"
# New variable stores a list of the three feature class names - restrooms, tennis_courts and trails
park_fc_list = ["restrooms", "tennis_courts", "trails"]
# New variable stores a list of the two park names that will be deleted - Patterson and Westenfield
park_del = ["Patterson", "Westenfield"]
# Use a for loop on the list of feature class names
for fc in park_fc_list:
    # Use a for loop on the list of park names that will be deleted
    for park in park_del:
        # New variable stores the where clause to search for the park name in the "PARK_NAME" field
        where_clause = f"\"PARK_NAME\" = '{park}'"
        # Use the with statement to set up an update cursor on the feature class in the iteration. Provide the
        # "PARK_NAME" field to the cursor to retrieve the names of the park
        with arcpy.da.UpdateCursor(fc,"PARK_NAME", where_clause) as u_cursor:
            # Use a for loop on the iterator of the records in the cursor
            for row in u_cursor:
                # Delete the row using the .deleteRow() method
                u_cursor.deleteRow()
    # Execute the Get Count tool using the given parameters and assign the result object to a variable called gc_result
    gc_result = arcpy.management.GetCount(fc)
    # Print the number of features using the result object stored in gc_result
    print(f"Number of features in {fc}: {gc_result}")

# End Q4
#######################################################################################################################
# TODO Q5: Search cursor and CSV file
#   In this question, you will retrieve information using a search cursor and write this information into a CSV file
#   (a) Using a search cursor on the facilities feature class and the csv.DictWriter class, create a CSV file called
#   "AustinLibraries.csv" in the A4_Results folder that contains the X and Y coordinates, names and addresses of all
#   libraries.
#   NOTE: The CSV file should contain four columns with names: X_COORD, Y_COORD, LIB_NAME, LIB_ADDRESS
#   (b) Using csv.DictReader, print the contents of the AustinLibraries.csv file.
print("\n ##### Question 5 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module
import arcpy
# Import the csv module
import csv

# New variable stores the path and name for the "AustinLibraries.csv" file in your "A4_Results" folder
csv_file_path = r"D:\workspace\PythonProgramming\Results\A4_Results\AustinLibraries.csv"
# Use the with statement to open the AustinLibraries CSV file in write mode.
with open(csv_file_path, "w", newline = "") as csv_file:
    # New variable stores the list of column names for the CSV file - X_COORD, Y_COORD, LIB_NAME and LIB_ADDRESS
    csv_columns = ["X_COORD", "Y_COORD", "LIB_NAME", "LIB_ADDRESS"]
    # New variable stores a DictWriter object for the CSV file with the above column names
    d_writer = csv.DictWriter(csv_file, csv_columns)
    # Write the column names to the CSV file
    d_writer.writeheader()
    # New variable stores a list of field names to provide to the search cursor - SHAPE@XY, FACILITY_N and FACILITY_A
    field_names = ["SHAPE@XY", "FACILITY_N", "FACILITY_A"]
    # New variable stores the where clause to search for the attribute "LIBRARY" in the "FACILITY_T" field
    where_clause = f"\"FACILITY_T\" = 'LIBRARY'"
    # Use the with statement to set up a search cursor on the facilities feature class.
    with arcpy.da.SearchCursor("facilities", field_names, where_clause) as s_cursor:
        # Use a for loop on the iterator of the records in the cursor
        for row in s_cursor:
            # New variable stores the x coordinate from the record
            x_coord = row[0][0]
            # New variable stores the y coordinate from the record
            y_coord = row[0][1]
            # New variable stores the name of the library
            library_name = row[1]
            # New variable stores the address of the library
            library_add = row[2]
            # New variable stores a dictionary with 4 key-value pairs corresponding to the 4 columns in the CSV file
            csv_dict = {csv_columns[0]:x_coord,
                        csv_columns[1]:y_coord,
                        csv_columns[2]:library_name,
                        csv_columns[3]:library_add
                        }
            # Write the above dictionary as a row into the CSV file using the .writerow() method
            d_writer.writerow(csv_dict)

# Use the with statement to open the AustinLibraries CSV file in read mode.
with open(csv_file_path, "r", newline = "") as csv_file:
    # New variable stores a DictReader object for the CSV file
    d_reader = csv.DictReader(csv_file)
    # Use a for loop to iterate over each row in the DictReader object
    for row in d_reader:
        # New variable stores the x coordinate from the row
        x_coord = row["X_COORD"]
        # New variable stores the y coordinate from the row
        y_coord = row["Y_COORD"]
        # New variable stores the name of the library from the row
        library_name = row["LIB_NAME"]
        # New variable stores the address of the library from the row
        library_add = row["LIB_ADDRESS"]
        # Print the contents of the above four variables
        print(f"{library_name} at {library_add}\n\tX: {x_coord}, Y: {y_coord}")

# END Q5
#######################################################################################################################
# END OF ASSIGNMENT 4
#######################################################################################################################
