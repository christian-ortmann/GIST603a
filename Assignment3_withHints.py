# ---------------------------------------------------------------------------------------------------------------------
# Name:        Assignment3_withHints.py
# Purpose:     Assignment Script for Assignment 3 that includes questions and tasks as well as hints to guide you
#               through writing code one line at a time. This script is recommended for beginners with no prior
#               programming experience.
# Author:      Dr. Yoganand Korgaonkar
# Student Name:
# ---------------------------------------------------------------------------------------------------------------------
print("\n ##### ASSIGNMENT 3 ##### \n")  # Ignore this line
#######################################################################################################################
# TODO Q1: arcpy list functions and for loops
#   In this question, you will use various arcpy list functions to identify and print out the names of different types
#   of files in the "data" folder on your computer.
#   (a) Set the arcpy environment property for workspace to the "data" folder for this class and print the property.
#   (b) Use the appropriate list function and a for loop to print all the xml files in this workspace.
#   (c) Use the appropriate list function and a for loop to print the names of all the file geodatabases in the
#   "data\ExploringSpatialData" folder.
#   (d) Use the appropriate list function and a for loop to print the names of all the feature datasets in the
#   "data\ExploringSpatialData\Austin.gdb" geodatabase.
#   (e) Use the appropriate list function and a for loop to print the names of all the point feature classes that begin
#   with the letter "P" or "p" in the "Parks" feature dataset in the "data\ExploringSpatialData\Austin.gdb" geodatabase.
#   (f) Use the appropriate list function and a for loop to print the names of all the rasters in the the
#   "data\ExploringSpatialData\Sturgis.gdb" geodatabase.
#   IMPORTANT: Remember to set the arcpy environment property for workspace before executing the list functions.
print("\n ##### Question 1 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Q1 (a) Set the arcpy environment property for workspace to the "data" folder on your computer

# Q1 (a) Print the arcpy environment property for workspace

# Q1 (b) New variable stores a list of xml file names returned by an arcpy list function. Use a wildcard to filter all
# xml files.

# Q1 (b) Use a for loop on the above list

    # Q1 (b) Print the name of the .xml file in the iteration

# Q1 (c) Set the arcpy environment property for workspace to the "data\ExploringSpatialData" folder on your computer

# Q1 (c) Print the arcpy environment property for workspace

# Q1 (c) New variable stores a list of file geodatabase names returned by an appropriate arcpy list function. Use the
# workspace type parameter in the function to filter file geodatabases

# Q1 (c) Use a for loop on the above list

    # Q1 (c) Print the name of the file geodatabase in the iteration

# Q1 (d) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" folder on your
# computer

# Q1 (d) Print the arcpy environment property for workspace

# Q1 (d) New variable stores a list of feature dataset names returned by an appropriate arcpy list function. Use the
# feature type parameter in the function to filter feature datasets

# Q1 (d) Use a for loop on the above list

    # Q1 (d) Print the name of the feature dataset in the iteration

# Q1 (e) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# wildcard to filter names starting with the letter "P", use feature type to filter point feature classes and use the
# feature dataset parameter to list from the "Parks" feature dataset.

# Q1 (e) Use a for loop on the above list

    # Q1 (e) Print the name of the feature class in the iteration

# Q1 (f) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Sturgis.gdb" folder on your
# computer

# Q1 (f) Print the arcpy environment property for workspace

# Q1 (f) New variable stores a list of raster names returned by an appropriate arcpy list function.

# Q1 (f) Use a for loop on the above list

    # Q1 (f) Print the name of the raster in the iteration

# End Q1
#######################################################################################################################
# TODO Q2: for loops and arcpy tools
#   In this question, you will be executing the Kernel Density tool on all the point feature classes in the "Parks"
#   feature dataset in the "data\ExploringSpatialData\Austin.gdb" geodatabase.
#   (a) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" geodatabase and
#   print the property.
#   (b) Use the appropriate list function and a for loop to print the names of all the point feature classes in the
#   "Parks" feature dataset in the "data\ExploringSpatialData\Austin.gdb" geodatabase.
#   (c) Inside the same for loop from (b), execute the Create Thiessen Polygons tool with the following parameters for
#   each of the feature classes from (b). Assign the result object from tool execution to a variable called tp_result.
#   Use the variable tp_result to print all geoprocessing messages from each tool execution.
#       in_features: feature class from (b)
#       out_feature_class: manually create a folder called A3_Results on your computer and store the output in this
#                           folder with the same name as the input feature class.
#       fields_to_copy: Ensure that all fields from the input feature are transferred to the output feature class
#   (d) Inside the same for loop from (b), execute the Get Count tool and store the result object in a variable called
#   tp_count. Use the variable tp_count to print out the number of polygons in each feature class.
print("\n ##### Question 2 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# New variable stores the path to the "A3_Results" folder on your computer. You must manually create this folder.

# Q2 (a) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" folder on your
# computer

# Q2 (a) Print the arcpy environment property for workspace

# Q2 (b) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# feature type parameter to filter point feature classes and the feature dataset parameter to list from the "Parks"
# feature dataset.

# Q2 (b) Use a for loop on the above list

    # Q2 (b) Print the name of the feature class in the iteration

    # Q2 (c) Execute the Create Thiessen Polygons tool using the given parameters and assign the result object to a
    # variable called tp_result

    # Q2 (c) Print all geoprocessing messages using the result object stored in variable tp_result.

    # Q2 (d) Execute the Get Count tool using the given parameters and assign the result object to a variable called
    # tp_count

    # Q2 (d) Print the number of polygons using the result object stored in tp_count

# End Q2
#######################################################################################################################
# TODO Q3: arcpy list fields and for loops
#   In this question you will use an arcpy list function to print out properties of certain fields in feature classes.
#   (a) Use the appropriate list function and a for loop to print the names and field types of all the fields in the
#   tracts feature class located in the Austin.gdb/Administrative feature dataset.
#   (b) Use the appropriate list function and a for loop to print the names, field type, and field length of all
#   fields with names that contain the string "ADD" in it in the addresspts feature class located in the
#   Austin.gdb/Administrative feature dataset.
print("\n ##### Question 3 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Q3 (a) New variable stores the path and name of the "tracts" feature class in the Austin.gdb/Administrative feature
# dataset on your computer.

# Q3 (a) New variable stores a list of field objects returned by an appropriate arcpy list function.

# Q3 (a) Use a for loop on the above list

    # Q3 (a) Use field object properties to print name and type

# Q3 (b) New variable stores the path and name of the "addresspts" feature class in the Austin.gdb/Administrative
# feature dataset on your computer.

# Q3 (b) New variable stores a list of field objects returned by an appropriate arcpy list function. Use wildcard to
# filter names that contain the string "ADD".

# Q3 (b) Use a for loop on the above list

    # Q3 (b) Use field object properties to print name, type & length

# End Q3
#######################################################################################################################
# TODO Q4: arcpy list functions & nested for loops
#   In this question, you will use various arcpy list functions to print out field names in the attribute tables of
#   various feature classes in the "data\ExploringSpatialData\Austin.gdb" folder on your computer.
#   (a) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" geodatabase and
#   print the property.
#   (b) Use the appropriate list function and a for loop to print the names of all the feature classes in the
#   "Transportation" feature dataset in the "data\ExploringSpatialData\Austin.gdb" geodatabase.
#   (c) Inside the same for loop from (b), use the appropriate list function and another for loop to print the field
#   names and field lengths of all string field types for all the feature classes from (b).
#   (d) Use the appropriate list function and a for loop to print the names of all the polygon feature classes in the
#   "Administrative" feature dataset in the "data\ExploringSpatialData\Austin.gdb" geodatabase.
#   (e) Inside the same for loop from (d), use the appropriate list function and another for loop to print the field
#   names and field types of all date or double field types for all the feature classes from (d).
print("\n ##### Question 4 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module

# Q4 (a) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" folder on your
# computer

# Q4 (a) Print the arcpy environment property for workspace

# Q4 (b) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# feature dataset parameter to list from the "Transportation" feature dataset.

# Q4 (b) Use a for loop on the above list

    # Q4 (b) Print the name of the feature class in the iteration

    # Q4 (c) New variable stores a list of field objects returned by an appropriate arcpy list function. Use variable
    # from the loop as input dataset and field type to filter string fields

    # Q4 (c) Use a for loop on the above list

        # Q4 (c) Use field object properties to print name & length

# Q4 (d) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# feature type parameter to filter polygon feature classes and the dataset parameter to list from the "Administrative"
# feature dataset.

# Q4 (d) Use a for loop on the above list

    # Q4 (d) Print the name of the feature class in the iteration

    # Q4 (e) New variable stores a list of field objects returned by an appropriate arcpy list function. Use variable
    # from the loop as input dataset

    # Q4 (e) Use a for loop on the above list

        # Q4 (e) Check if the type of the field is "Date" or if it is "Double" using field object properties

            # Q4 (e) Use field object properties to print name & type

# End Q4
#######################################################################################################################
# TODO Q5: Dictionaries
#   In this question, you are given a dictionary that stores geometries of certain shapes. Using this dictionary, you
#   will calculate areas of these shapes.
#   (a) (i) Calculate the area of the circle in square meters and square feet.
#       (ii) Add the areas of the circle to the original dictionary using the keys "c_area_m" for area in square meters
#       and "c_area_ft" for area in square feet.
#       (iii) Print the following lines using variables and keys.
#           <bol>   Radius of Circle = 4.89 meters<eol>
#           <bol>     Area of Circle = πr²<eol>
#           <bol>                    = 3.14 X (4.89 m)²<eol>
#           <bol>                    = 75.08 sq m<eol>
#           <bol>                    = 808.15 sq ft<eol>
#   (b) Print the contents of the dictionary.
#   (c) (i) Calculate the area of the square in square meters and square feet.
#       (ii) Add the areas of the square to the original dictionary using the keys "sq_area_m" for area in square meters
#       and "sq_area_ft" for area in square feet.
#       (iii) Print the following lines using variables and keys.
#           <bol>     Side of Square = 11.11 meters<eol>
#           <bol>     Area of Square = side²<eol>
#           <bol>                    = (11.11 m)²<eol>
#           <bol>                    = 123.43 sq m<eol>
#           <bol>                    = 1328.59 sq ft<eol>
#   (d) Print the contents of the dictionary.
#   (e) (i) Calculate the area of the triangle in square meters and square feet.
#       (ii) Add the areas of the triangle to the original dictionary using the keys "t_area_m" for area in square
#       meters and "t_area_ft" for area in square feet.
#       (iii) Print the following lines using variables and keys.
#           <bol>   Base of Triangle = 43.15 meters<eol>
#           <bol> Height of Triangle = 25.47 meters<eol>
#           <bol>   Area of Triangle = ½bh<eol>
#           <bol>                    = ½ X 43.15 m X 25.47 m<eol>
#           <bol>                    = 549.52 sq m<eol>
#           <bol>                    = 5914.98 sq ft<eol>
#   (f) Print the contents of the dictionary.
#   (g) Print the following using the dictionary.
#       <bol> SHAPE      |     AREA (sq m) |    AREA (sq ft) <eol>
#       <bol> ---------- | --------------- | --------------- <eol>
#       <bol> Triangle   |          549.52 |         5914.98 <eol>
#       <bol> Square     |          123.43 |         1328.59 <eol>
#       <bol> Circle     |           75.08 |          808.15 <eol>
#   IMPORTANT: Do not type out any of these numbers in your code. These numbers have been provided in the dictionary.
#   Use appropriate dictionary keys to access and use these numbers in your code.
#   Note: <bol> indicates "beginning of line", and <eol> indicates end of line. These are indicative of where
#   the line starts and where it ends. You do not have to print <bol> & <eol> in the output.
print("\n ##### Question 5 ################################################################### \n")  # Ignore this line
# Write your code below

# Given dictionary stored in a variable. Do not modify this. Use this variable in order to complete all tasks.
dictionary_of_numbers = {
    "triangle": {"base": 43.15, "height": 25.47},        # Stores a dictionary with base and height of triangle
    "square": 11.11,                                     # Stores the length of a side of a square
    "circle": 4.89,                                      # Stores the radius of a circle
    "pi": 3.14,                                          # Stores the value of Pi
    "sq_m_2_sq_ft": 10.7639                              # Stores the conversion factor to convert from sq m to sq ft
}

# Six new variables access and store six values from the dictionaries using appropriate keys






# Q5 (a) (i) New variable stores the area of the circle in square meters calculated using values from the dictionary

# Q5 (a) (i) New variable stores the area of the circle converted to square feet

# Q5 (a) (ii) Add the area of the circle in square meters to the dictionary using the key "c_area_m"

# Q5 (a) (ii) Add the area of the circle in square feet to the dictionary using the key "c_area_ft"

# Q5 (a) (iii) Print the five lines as shown in the question





# Q5 (b) Print the contents of the dictionary

# Q5 (c) (i) New variable stores the area of the square in square meters calculated using values from the dictionary

# Q5 (c) (i) New variable stores the area of the square converted to square feet

# Q5 (c) (ii) Add the area of the square in square meters to the dictionary using the key "sq_area_m"

# Q5 (c) (ii) Add the area of the square in square feet to the dictionary using the key "sq_area_ft"

# Q5 (c) (iii) Print the five lines as shown in the question





# Q5 (d) Print the contents of the dictionary

# Q5 (e) (i) New variable stores the area of the triangle in square meters calculated using values from the dictionary

# Q5 (e) (i) New variable stores the area of the triangle converted to square feet

# Q5 (e) (ii) Add the area of the triangle in square meters to the dictionary using the key "t_area_m"

# Q5 (e) (ii) Add the area of the triangle in square feet to the dictionary using the key "t_area_ft"

# Q5 (e) (iii) Print the six lines as shown in the question






# Q5 (f) Print the contents of the dictionary

# Q5 (g) Print the five lines as shown in the question





# End Q5
#######################################################################################################################
# TODO Q6: Lists, dictionaries and for loops
#  Given the following list of dictionaries, this task requires you to print three columns populated by the values
#  in the dictionaries.
#  Using one for loop, print the contents of the dictionary as follows:
#         <bol>   ID |      WATERSHED      | RECEIVING WATERSHED <eol>
#         <bol> ---- | ------------------- | ------------------- <eol>
#         <bol>   20 |       BEAR W        |     LAKE AUSTIN     <eol>
#         <bol>   34 |     COTTONMOUTH     |     ONION CREEK     <eol>
#         <bol>   35 |     COTTONWOOD      |   WILBARGER CREEK   <eol>
#         <bol>   47 |         ELM         |   GILLELAND CREEK   <eol>
#         <bol>   58 |   HARPER'S BRANCH   |      TOWN LAKE      <eol>
#         <bol>   62 |       JOHNSON       |      TOWN LAKE      <eol>
#         <bol>   65 |     LITTLE BEAR     |     BEAR CREEK      <eol>
#         <bol>   74 |      LOCKWOOD       |      WILBARGER      <eol>
#         <bol>   75 |        MAHA         |     CEDAR CREEK     <eol>
#         <bol>   88 |       RINARD        |     ONION CREEK 	 <eol>
#   IMPORTANT: Do not type out any of these strings, use variables and keys to access them from the dictionary.
#   Note: <bol> indicates "beginning of line", and <eol> indicates end of line. These are indicative of where
#   the line starts and where it ends. You do not have to print <bol> & <eol> in the output.
print("\n ##### Question 6 ################################################################### \n")  # Ignore this line
# Write your code below

# Given list stored in a variable. Do not modify this. Use this variable in order to complete all tasks.
# The following list stores 10 dictionaries and each dictionary stores one record from the attribute table of the
# "watersheds" feature class in the Austin.gdb/Environmental dataset
# The key for each dictionary is the column (or field) name
# The value corresponds to the attribute in the respective column (or field)
list_of_dicts = [
    {"DISPLAY": "Bear W", "RECV_WATER": "Lake Austin", "WATERSHED_": 20},
    {"DISPLAY": "Cottonmouth", "RECV_WATER": "Onion Creek", "WATERSHED_": 34},
    {"DISPLAY": "Cottonwood", "RECV_WATER": "Wilbarger Creek", "WATERSHED_": 35},
    {"DISPLAY": "Elm", "RECV_WATER": "Gilleland Creek", "WATERSHED_": 47},
    {"DISPLAY": "Harper's Branch", "RECV_WATER": "Town Lake", "WATERSHED_": 58},
    {"DISPLAY": "Johnson", "RECV_WATER": "Town Lake", "WATERSHED_": 62},
    {"DISPLAY": "Little Bear", "RECV_WATER": "Bear Creek", "WATERSHED_": 65},
    {"DISPLAY": "Lockwood", "RECV_WATER": "Wilbarger", "WATERSHED_": 74},
    {"DISPLAY": "Maha", "RECV_WATER": "Cedar Creek", "WATERSHED_": 75},
    {"DISPLAY": "Rinard", "RECV_WATER": "Onion Creek", "WATERSHED_": 88},
]

# Q6 Print the first two lines using any of the string formatting methods.


# Q6 Use a for loop on the list to access each dictionary

    # Q6 New variable stores the ID value from each dictionary using the key "WATERSHED_". Convert the value to string.

    # Q6 New variable stores the watershed name value from each dictionary using the key "DISPLAY". Convert the value to
    # uppercase.

    # Q6 New variable stores the receiving watershed name value from each dictionary using the key "RECV_WATER". Convert
    # the value to uppercase.

    # Q6 Print the line using any of the string formatting methods.

# End Q6
#######################################################################################################################
# END OF ASSIGNMENT 3
#######################################################################################################################



