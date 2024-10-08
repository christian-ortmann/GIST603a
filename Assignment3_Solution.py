# ---------------------------------------------------------------------------------------------------------------------
# Name:        Assignment3_Solution.py
# Purpose:     Solution Script for Assignment 3
# Author:      Dr. Yoganand Korgaonkar
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
import arcpy

print("\n ### Q1 (a) ### \n")  # Ignore this line
# Q1 (a) Set the arcpy environment property for workspace to the "data" folder on your computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data"
# Q1 (a) Print the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")

print("\n ### Q1 (b) ### \n")  # Ignore this line
# Q1 (b) New variable stores a list of xml file names returned by an arcpy list function. Use a wildcard to filter all
# xml files.
xml_list = arcpy.ListFiles("*.xml")
# Q1 (b) Use a for loop on the above list
print(f"*.xml files in {arcpy.env.workspace}:")
for xml in xml_list:  # Variable xml stores each item in the list for each iteration of the loop
    # Q1 (b) Print the name of the .xml file in the iteration
    print(f"\t{xml}")

print("\n ### Q1 (c) ### \n")  # Ignore this line
# Q1 (c) Set the arcpy environment property for workspace to the "data\ExploringSpatialData" folder on your computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data\ExploringSpatialData"
# Q1 (c) Print the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")
# Q1 (c) New variable stores a list of file geodatabase names returned by an appropriate arcpy list function. Use the
# workspace type parameter in the function to filter file geodatabases
gdb_list = arcpy.ListWorkspaces("", "FileGDB")
print(f"File geodatabases in {arcpy.env.workspace}:")
# Q1 (c) Use a for loop on the above list
for gdb in gdb_list:  # Variable gdb stores each item in the list for each iteration of the loop
    # Q1 (c) Print the name of the file geodatabase in the iteration
    print(f"\t{gdb}")

print("\n ### Q1 (d) ### \n")  # Ignore this line
# Q1 (d) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" folder on your
# computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data\ExploringSpatialData\Austin.gdb"
# Q1 (d) Print the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")
# Q1 (d) New variable stores a list of feature dataset names returned by an appropriate arcpy list function. Use the
# feature type parameter in the function to filter feature datasets
fd_list = arcpy.ListDatasets("", "Feature")
print(f"Feature datasets in {arcpy.env.workspace}:")
# Q1 (d) Use a for loop on the above list
for fd in fd_list:  # Variable fd stores each item in the list for each iteration of the loop
    # Q1 (d) Print the name of the feature dataset in the iteration
    print(f"\t{fd}")

print("\n ### Q1 (e) ### \n")  # Ignore this line
# Q1 (e) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# wildcard to filter names starting with the letter "P", use feature type to filter point feature classes and use the
# feature dataset parameter to list from the "Parks" feature dataset.
fc_list = arcpy.ListFeatureClasses("P*", "Point", "Parks")
print(f"Feature classes in {arcpy.env.workspace}\\Parks:")
# Q1 (e) Use a for loop on the above list
for fc in fc_list:  # Variable fc stores each item in the list for each iteration of the loop
    # Q1 (e) Print the name of the feature class in the iteration
    print(f"\t{fc}")

print("\n ### Q1 (f) ### \n")  # Ignore this line
# Q1 (f) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Sturgis.gdb" folder on your
# computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data\ExploringSpatialData\Sturgis.gdb"
# Q1 (f) Print the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")
# Q1 (f) New variable stores a list of raster names returned by an appropriate arcpy list function.
ra_list = arcpy.ListRasters()
print(f"Rasters in {arcpy.env.workspace}:")
# Q1 (f) Use a for loop on the above list
for ra in ra_list:  # Variable ra stores each item in the list for each iteration of the loop
    # Q1 (f) Print the name of the raster in the iteration
    print(f"\t{ra}")

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
import arcpy

# New variable stores the path to the "A3_Results" folder on your computer. You must manually create this folder.
out_fc = r"E:\workspace\PythonProgramming\Results\A3_Results"

print("\n ### Q2 (a) ### \n")  # Ignore this line
# Q2 (a) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" folder on your
# computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data\ExploringSpatialData\Austin.gdb"
# Q2 (a) Print the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")

# Q2 (b) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# feature type parameter to filter point feature classes and the feature dataset parameter to list from the "Parks"
# feature dataset.
pt_fc_list = arcpy.ListFeatureClasses("", "Point", "Parks")
# Q2 (b) Use a for loop on the above list
for pt_fc in pt_fc_list:  # Variable pt_fc stores each item in the list for each iteration of the loop
    # Q2 (b) Print the name of the feature class in the iteration
    print("\n ### Q2 (b) ### \n")  # Ignore this line
    print(f"Feature Class Name: {pt_fc}")

    print("\n ### Q2 (c) ### \n")  # Ignore this line
    # Q2 (c) Execute the Create Thiessen Polygons tool using the given parameters and assign the result object to a
    # variable called tp_result
    tp_result = arcpy.analysis.CreateThiessenPolygons(in_features=pt_fc,
                                                      out_feature_class=f"{out_fc}\{pt_fc}",
                                                      fields_to_copy="ALL")
    # Q2 (c) Print all geoprocessing messages using the result object stored in variable tp_result.
    print(tp_result.getMessages())

    print("\n ### Q2 (d) ### \n")  # Ignore this line
    # Q2 (d) Execute the Get Count tool using the given parameters and assign the result object to a variable called
    # tp_count
    tp_count = arcpy.management.GetCount(tp_result)
    # Q2 (d) Print the number of polygons using the result object stored in tp_count
    print(f"Number of polygons in {pt_fc}: {tp_count[0]}\n")

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
import arcpy

print("\n ### Q3 (a) ### \n")  # Ignore this line
# Q3 (a) New variable stores the path and name of the "tracts" feature class in the Austin.gdb/Administrative feature
# dataset on your computer.
tracts_fc = r"E:\workspace\PythonProgramming\data\ExploringSpatialData\Austin.gdb\Administrative\tracts"
# Q3 (a) New variable stores a list of field objects returned by an appropriate arcpy list function.
tracts_fields = arcpy.ListFields(tracts_fc, "", "")
print(f"Fields in {tracts_fc}:")
# Q3 (a) Use a for loop on the above list
for fld in tracts_fields:  # Variable fld stores each item in the list for each iteration of the loop
    # Q3 (a) Use field object properties to print name and type
    print(f"Field {fld.name} of type {str(fld.type)}")

print("\n ### Q3 (b) ### \n")  # Ignore this line
# Q3 (b) New variable stores the path and name of the "addresspts" feature class in the Austin.gdb/Administrative
# feature dataset on your computer.
addresspts_fc = r"E:\workspace\PythonProgramming\data\ExploringSpatialData\Austin.gdb\Administrative\addresspts"
# Q3 (b) New variable stores a list of field objects returned by an appropriate arcpy list function. Use wildcard to
# filter names that contain the string "ADD".
addresspts_fc_fields = arcpy.ListFields(addresspts_fc, "*ADD*", "")
print(f"Fields in {addresspts_fc}:")
# Q3 (b) Use a for loop on the above list
for fld in addresspts_fc_fields:  # Variable fld stores each item in the list for each iteration of the loop
    # Q3 (b) Use field object properties to print name, type & length
    print(f"Field {fld.name} of type {str(fld.type)} has length {str(fld.length)}")

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
import arcpy

print("\n ### Q4 (a) ### \n")  # Ignore this line
# Q4 (a) Set the arcpy environment property for workspace to the "data\ExploringSpatialData\Austin.gdb" folder on your
# computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data\ExploringSpatialData\Austin.gdb"
# Q4 (a) Print the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")

# Q4 (b) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# feature dataset parameter to list from the "Transportation" feature dataset.
fc_list = arcpy.ListFeatureClasses("", "", "Transportation")
# Q4 (b) Use a for loop on the above list
for fc in fc_list:  # Variable fc stores each item in the list for each iteration of the loop
    # Q4 (b) Print the name of the feature class in the iteration
    print("\n ### Q4 (b) ### \n")  # Ignore this line
    print(f"Feature Class Name: {fc}")
    print("\n ### Q4 (c) ### \n")  # Ignore this line
    # Q4 (c) New variable stores a list of field objects returned by an appropriate arcpy list function. Use variable
    # from the loop as input dataset and field type to filter string fields
    fc_fields = arcpy.ListFields(fc, "", "String")
    # Q4 (c) Use a for loop on the above list
    for fld in fc_fields:  # Variable fld stores each item in the list for each iteration of the loop
        # Q4 (c) Use field object properties to print name & length
        print(f"Field {fld.name} has length {str(fld.length)}")

# Q4 (d) New variable stores a list of feature class names returned by an appropriate arcpy list function. Use the
# feature type parameter to filter polygon feature classes and the dataset parameter to list from the "Administrative"
# feature dataset.
fc_list = arcpy.ListFeatureClasses("", "Polygon", "Administrative")
# Q4 (d) Use a for loop on the above list
for fc in fc_list:  # Variable fc stores each item in the list for each iteration of the loop
    # Q4 (d) Print the name of the feature class in the iteration
    print("\n ### Q4 (d) ### \n")  # Ignore this line
    print(f"Feature Class Name: {fc}")
    print("\n ### Q4 (e) ### \n")  # Ignore this line
    # Q4 (e) New variable stores a list of field objects returned by an appropriate arcpy list function. Use variable
    # from the loop as input dataset
    fc_fields = arcpy.ListFields(fc, "", "")
    # Q4 (e) Use a for loop on the above list
    for fld in fc_fields:  # Variable fld stores each item in the list for each iteration of the loop
        # Q4 (e) Check if the type of the field is "Date" or if it is "Double" using field object properties
        if fld.type == "Date" or fld.type == "Double":
            # Q4 (e) Use field object properties to print name & type
            print(f"Field {fld.name} is of type {str(fld.type)}")

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
pi = dictionary_of_numbers["pi"]
circle = dictionary_of_numbers["circle"]
square = dictionary_of_numbers["square"]
triangle_base = dictionary_of_numbers["triangle"]["base"]
triangle_height = dictionary_of_numbers["triangle"]["height"]
conv_factor = dictionary_of_numbers["sq_m_2_sq_ft"]

print("\n ### Q5 (a) (i) & (ii) ### - No Output \n")  # Ignore this line
# Q5 (a) (i) New variable stores the area of the circle in square meters calculated using values from the dictionary
area_circle_m = round(pi * circle ** 2, 2)
# Q5 (a) (i) New variable stores the area of the circle converted to square feet
area_circle_ft = round(area_circle_m * conv_factor, 2)
# Q5 (a) (ii) Add the area of the circle in square meters to the dictionary using the key "c_area_m"
dictionary_of_numbers["c_area_m"] = area_circle_m
# Q5 (a) (ii) Add the area of the circle in square feet to the dictionary using the key "c_area_ft"
dictionary_of_numbers["c_area_ft"] = area_circle_ft
print("\n ### Q5 (a) (iii) ### \n")  # Ignore this line
# Q5 (a) (iii) Print the five lines as shown in the question
print(f" {'Radius of Circle':>19} = {circle} meters")
print(f" {'Area of Circle':>19} = \u03C0r\u00B2")
print(f" {' ':>19} = {pi} X ({circle} m)\u00B2")
print(f" {' ':>19} = {area_circle_m} sq m")
print(f" {' ':>19} = {area_circle_ft} sq ft")

print("\n ### Q5 (b) ### \n")  # Ignore this line
# Q5 (b) Print the contents of the dictionary
print(f"Contents of the dictionary in the format - <key>: <value>")
for key in dictionary_of_numbers.keys():  # Using a for loop to print key-value pairs
    print(f"\t'{key}': {dictionary_of_numbers[key]}")

print("\n ### Q5 (c) (i) & (ii) ### - No Output \n")  # Ignore this line
# Q5 (c) (i) New variable stores the area of the square in square meters calculated using values from the dictionary
area_square_m = round(square ** 2, 2)
# Q5 (c) (i) New variable stores the area of the square converted to square feet
area_square_ft = round(area_square_m * conv_factor, 2)
# Q5 (c) (ii) Add the area of the square in square meters to the dictionary using the key "sq_area_m"
dictionary_of_numbers["sq_area_m"] = area_square_m
# Q5 (c) (ii) Add the area of the square in square feet to the dictionary using the key "sq_area_ft"
dictionary_of_numbers["sq_area_ft"] = area_square_ft
print("\n ### Q5 (c) (iii) ### \n")  # Ignore this line
# Q5 (c) (iii) Print the five lines as shown in the question
print(f" {'Side of Square':>19} = {square} meters")
print(f" {'Area of Square':>19} = side\u00B2")
print(f" {' ':>19} = ({square} m)\u00B2")
print(f" {' ':>19} = {area_square_m} sq m")
print(f" {' ':>19} = {area_square_ft} sq ft")

print("\n ### Q5 (d) ### \n")  # Ignore this line
# Q5 (d) Print the contents of the dictionary
print(f"Contents of the dictionary in the format - <key>: <value>")
for key in dictionary_of_numbers.keys():  # Using a for loop to print key-value pairs
    print(f"\t'{key}': {dictionary_of_numbers[key]}")

print("\n ### Q5 (e) (i) & (ii) ### - No Output \n")  # Ignore this line
# Q5 (e) (i) New variable stores the area of the triangle in square meters calculated using values from the dictionary
area_triangle_m = round(triangle_base * triangle_height / 2, 2)
# Q5 (e) (i) New variable stores the area of the triangle converted to square feet
area_triangle_ft = round(area_triangle_m * conv_factor, 2)
# Q5 (e) (ii) Add the area of the triangle in square meters to the dictionary using the key "t_area_m"
dictionary_of_numbers["t_area_m"] = area_triangle_m
# Q5 (e) (ii) Add the area of the triangle in square feet to the dictionary using the key "t_area_ft"
dictionary_of_numbers["t_area_ft"] = area_triangle_ft
print("\n ### Q5 (e) (iii) ### \n")  # Ignore this line
# Q5 (e) (iii) Print the six lines as shown in the question
print(f" {'Base of Triangle':>19} = {triangle_base} meters")
print(f" {'Height of Triangle':>19} = {triangle_height} meters")
print(f" {'Area of Triangle':>19} = \u00BDbh")
print(f" {' ':>19} = \u00BD X {triangle_base} m X {triangle_height} m")
print(f" {' ':>19} = {area_triangle_m} sq m")
print(f" {' ':>19} = {area_triangle_ft} sq ft")

print("\n ### Q5 (f) ### \n")  # Ignore this line
# Q5 (f) Print the contents of the dictionary
print(f"Contents of the dictionary in the format - <key>: <value>")
for key in dictionary_of_numbers.keys():  # Using a for loop to print key-value pairs
    print(f"\t'{key}': {dictionary_of_numbers[key]}")

print("\n ### Q5 (g) ### \n")  # Ignore this line
# Q5 (g) Print the five lines as shown in the question
print(f" {'SHAPE':<10} | {'AREA (sq m)':>15} | {'AREA (sq ft)':>15} ")
print(f" {'':-<10} | {'':->15} | {'':->15} ")
print(f" {'Triangle':<10} | {dictionary_of_numbers['t_area_m']:>15} | {dictionary_of_numbers['t_area_ft']:>15} ")
print(f" {'Square':<10} | {dictionary_of_numbers['sq_area_m']:>15} | {dictionary_of_numbers['sq_area_ft']:>15} ")
print(f" {'Circle':<10} | {dictionary_of_numbers['c_area_m']:>15} | {dictionary_of_numbers['c_area_ft']:>15} ")

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

print("\n ### Q6 ### \n")  # Ignore this line
# Q6 Print the first two lines using any of the string formatting methods.
print(f" {'ID':>4} | {'WATERSHED':^19} | {'RECEIVING WATERSHED':^19}")
print(f" {'':->4} | {'':-^19} | {'':-^19}")
# Q6 Use a for loop on the list to access each dictionary
for dict in list_of_dicts:  # Variable dict stores each dictionary in the list for each iteration of the loop
    # Q6 New variable stores the ID value from each dictionary using the key "WATERSHED_". Convert the value to string.
    id = str(dict["WATERSHED_"])
    # Q6 New variable stores the watershed name value from each dictionary using the key "DISPLAY". Convert the value to
    # uppercase.
    wshed = dict["DISPLAY"].upper()
    # Q6 New variable stores the receiving watershed name value from each dictionary using the key "RECV_WATER". Convert
    # the value to uppercase.
    recv = dict["RECV_WATER"].upper()
    # Q6 Print the line using any of the string formatting methods.
    print(f" {id:>4} | {wshed:^19} | {recv:^19}")

# End Q6
#######################################################################################################################
# END OF ASSIGNMENT 3
#######################################################################################################################
