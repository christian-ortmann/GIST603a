# ---------------------------------------------------------------------------------------------------------------------
# Name:        Assignment2_Solution.py
# Purpose:     Solution Script for Assignment 2
# Author:      Dr. Yoganand Korgaonkar
# ---------------------------------------------------------------------------------------------------------------------
print("\n ##### ASSIGNMENT 2 ##### \n")  # Ignore this line
#######################################################################################################################
# TODO Q1: Your Grade
#   In this question, you will print a letter grade based on your expected final score (out of 250) in this class.
#   (a) Create a variable to store your expected final score as an integer and print its contents.
#   (b) Create a new variable to store the percentage of your final score using the variable from (a) and by dividing
#   it by 250 and multiplying the result by 100. Print its contents.
#   (c) Write if, elif and/or else statements to check for all of the following conditions and perform the necessary
#   actions as stated below.
#           (i) If your percentage is greater than or equal to 90%, print <bol>Final Grade: A<eol>
#           (ii) If your percentage is greater than or equal to 80% and less than 90%, print <bol>Final Grade: B<eol>
#           (iii) If your percentage is greater than or equal to 70% and less than 80%, print <bol>Final Grade: C<eol>
#           (iv) If your percentage is greater than or equal to 60% and less than 70%, print <bol>Final Grade: D<eol>
#           (v) If your percentage is less than 60%, print <bol>Final Grade: E<eol>
#   (d) Test your code by running your code block for each of the following final scores: 64, 151, 189, 200, 249
#       You can do this by changing the value of the variable from (a) and running the code block multiple times.
#       Ensure that your code handles all test cases correctly.
#   Note: <bol> indicates "beginning of line", and <eol> indicates end of line. These are indicative of where
#   the line starts and where it ends. You do not have to print <bol> & <eol> in the output.
print("\n ##### Question 1 ################################################################### \n")  # Ignore this line
# Write your code below

print("\n ### Q1 (a) ### \n")  # Ignore this line
# Q1 (a) New variable that stores your expected final score as an integer.
final_score = 250  # Expected final score out of 250. Change this score for test cases in (d) and re-run the code
# Q1 (a) Print the contents of the new variable
print(f"My expected final score: {final_score}/250")

print("\n ### Q1 (b) ### \n")  # Ignore this line
# Q1 (b) New variable that stores the percentage of your final score by dividing it by 250 and multiplying by 100.
final_pct = (final_score / 250) * 100
# Q1 (b) Print the contents of the new variable
print(f"My expected final percentage: {final_pct}%")

print("\n ### Q1 (c) ### \n")  # Ignore this line
# Q1 (c) (i) Check if percentage is greater than or equal to 90%
if final_pct >= 90:  # Condition checks the percentage
    # Q1 (c) (i) If True: print <bol>Final Grade: A<eol>
    print("Final Grade: A")  # Final grade is an A
# Q1 (c) (ii) Use elif to check if percentage is greater than or equal to 80% and less than 90%
elif final_pct >= 80 and final_pct < 90:
    # Q1 (c) (ii) If True: print <bol>Final Grade: B<eol>
    print("Final Grade: B")  # Final grade is an B
# Q1 (c) (iii) Use elif to check if percentage is greater than or equal to 70% and less than 80%
elif final_pct >= 70 and final_pct < 80:
    # Q1 (c) (ii) If True: print <bol>Final Grade: C<eol>
    print("Final Grade: C")  # Final grade is an C
# Q1 (c) (iv) Use elif to check if percentage is greater than or equal to 60% and less than 70%
elif final_pct >= 60 and final_pct < 70:
    # Q1 (c) (ii) If True: print <bol>Final Grade: D<eol>
    print("Final Grade: D")  # Final grade is an D
# Q1 (c) (v) Use else to check for all other values (including less than 60%)
else:
    # Q1 (c) (ii) If True: print <bol>Final Grade: E<eol>
    print("Final Grade: E")  # Final grade is an E

# Alternative Method - Uncomment if you would like to test this code block.
# if final_pct >= 90:
#     print(f"Final Grade: A")
# elif 80 <= final_pct < 90:
#     print(f"Final Grade: B")
# elif 70 <= final_pct < 80:
#     print(f"Final Grade: C")
# elif 60 <= final_pct < 70:
#     print(f"Final Grade: D")
# else:
#     print(f"Final Grade: E")

# Q1 (d) Change the value of variable in Q1 (a) above and re-run the code to test your code.
# Using a for loop to test various test cases. You will learn about loops in Module 3.
test_scores = [64, 151, 189, 200, 249]
index = 1
for score in test_scores:
    print(f"\n ### Q1 (d) ### Test Case # {index} | Expected Score = {score}\n")  # Ignore this line

    print("\n ### Q1 (a) ### \n")  # Ignore this line
    final_score = score
    print(f"My expected final score: {final_score}/250")

    print("\n ### Q1 (b) ### \n")  # Ignore this line
    final_pct = (final_score / 250) * 100
    print(f"My expected final percentage: {final_pct}%")

    print("\n ### Q1 (c) ### \n")  # Ignore this line
    if final_pct >= 90:
        print("Final Grade: A")
    elif final_pct >= 80 and final_pct < 90:
        print("Final Grade: B")
    elif final_pct >= 70 and final_pct < 80:
        print("Final Grade: C")
    elif final_pct >= 60 and final_pct < 70:
        print("Final Grade: D")
    else:
        print("Final Grade: E")

    index += 1

# End Q1
#######################################################################################################################
# TODO Q2: Comparing Numbers
#   In this question, you will check if a number, that represents an area, is within a range and convert the units of
#   this number accordingly.
#   (a) Create a variable that stores a float to represent an area of a polygon in hectares and print its contents.
#   (b) Write if, elif and/or else statements to check for all of the following conditions and perform the necessary
#   actions as stated below.
#       (i) If the area is greater than 50 and less than 100 hectares, convert the area to square feet and print:
#           <bol>Original Area: <variable from (a)> Hectares --> Converted to <new_area> Square Feet.<eol>
#       (ii) If the area is greater than 100 and less than 1000 hectares, convert the area to square meters and print:
#           <bol>Original Area: <variable from (a)> Hectares --> Converted to <new_area> Square Meters.<eol>
#       (iii) If the area is greater than 1000 and less than 10000 hectares, convert the number to acres and print:
#           <bol>Original Number: <variable from (a)> Hectares --> Converted to <new_area> Acres.<eol>
#       (iv) For all other areas, convert the area to square kilometers and print:
#           <bol>Original Number: <variable from (a)> Hectares --> Converted to <new_area> Square Kilometers.<eol>
#   (c) Test your code by running your code block for each of the following areas:
#       42.424242, 87.98, 439.4787, 1000, 7498.4, 51829.02
#       You can do this by changing the value of the variable from (a) and running the code block multiple times.
#       Ensure that your code handles all test cases correctly.
#   Note: Conversion Units:
#       1 Hectare = 107639.10417 Square Feet
#       1 Hectare = 10000 Square Meters
#       1 Hectare = 2.47 Acres
#       1 Hectare = 0.01 Square Kilometers
print("\n ##### Question 2 ################################################################### \n")  # Ignore this line
# Write your code below

print("\n ### Q2 (a) ### \n")  # Ignore this line
# Q2 (a) New variable that stores a float to represent an area of a polygon in hectares.
area_ha = 45.67  # Area of polygon in hectares as float. Change this float for test cases in (d) and re-run the code
# Q2 (a) Print the contents of the new variable
print(f"Area of Polygon: {area_ha} Hectares")

print("\n ### Q2 (b) ### \n")  # Ignore this line
# Q2 (b) (i) Check if the area is greater than 50 and less than 100 hectares
if 50 < area_ha < 100:
    # Q2 (b) (i) If True: Convert the area to square feet and assign to a new variable.
    new_area = area_ha * 107639.10417
    # Q2 (b) (i) If True: Print the following:
    # <bol>Original Area: <variable from (a)> Hectares --> Converted to <new_area> Square Feet.<eol>
    print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Square Feet.")
# Q2 (b) (ii) Use elif to check if the area is greater than 100 and less than 1000 hectares
elif 100 < area_ha < 1000:
    # Q2 (b) (ii) If True: Convert the area to square meters and assign to a new variable.
    new_area = area_ha * 10000
    # Q2 (b) (ii) If True: Print the following:
    # <bol>Original Area: <variable from (a)> Hectares --> Converted to <new_area> Square Meters.<eol>
    print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Square Meters.")
# Q2 (b) (iii) Use elif to check if the area is greater than 1000 and less than 10000 hectares
elif 1000 < area_ha < 10000:
    # Q2 (b) (iii) If True: Convert the area to acres and assign to a new variable.
    new_area = area_ha * 2.47
    # Q2 (b) (iii) If True: Print the following:
    # <bol>Original Area: <variable from (a)> Hectares --> Converted to <new_area> Acres.<eol>
    print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Acres.")
# Q2 (b) (iii) Use else to check for all other areas
else:
    # Q2 (b) (iv) If True: Convert the area to square kilometers and assign to a new variable.
    new_area = area_ha * 0.01
    # Q2 (b) (iv) If True: Print the following:
    # <bol>Original Area: <variable from (a)> Hectares --> Converted to <new_area> Square Kilometers.<eol>
    print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Square Kilometers.")

# Q2 (c) Change the value of variable in Q2 (a) above and re-run the code to test your code.
# Using a for loop to test various test cases. You will learn about loops in Module 3.
test_areas = [42.424242, 87.98, 439.4787, 1000, 7498.4, 51829.02]
index = 1
for area in test_areas:
    print(f"\n ### Q2 (c) ### Test Case # {index} | Area = {area} Hectares\n")  # Ignore this line

    print("\n ### Q2 (a) ### \n")  # Ignore this line
    area_ha = area
    print(f"Area of Polygon: {area_ha} Hectares")

    print("\n ### Q2 (b) ### \n")  # Ignore this line
    if 50 < area_ha < 100:
        new_area = area_ha * 107639.10417
        print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Square Feet.")
    elif 100 < area_ha < 1000:
        new_area = area_ha * 10000
        print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Square Meters.")
    elif 1000 < area_ha < 10000:
        new_area = area_ha * 2.47
        print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Acres.")
    else:
        new_area = area_ha * 0.01
        print(f"Original Area: {area_ha} Hectares --> Converted to {new_area:.2f} Square Kilometers.")
    index += 1

# End Q2
#######################################################################################################################
# TODO Q3: Conditional Statements and Lists
#   In this question, you will manipulate a given list of feature class names, create paths and check if these feature
#   classes exist on your computer.
#   (a) Set the arcpy environment property for workspace to the "data" folder for this class and print its contents:
#   (b) Write if, elif and/or else statements to check if the string "bike_routes.shp" is in the list.
#       - If True,
#           (i) Create a variable to store the path created by concatenating the workspace string and this name from
#           the list. Print the contents of this variable.
#           (ii) Using arcpy.Exists() and the above variable, check if it exists on your computer:
#           - If True, print: <bol><Variable from (b) (i)> exists!<eol>
#           - If False, remove the item from the list.
#       - If False, print: <bol>bike_routes.shp not found in list!<eol>
#   (c) Print the contents of the list.
#   (d) Write if, elif and/or else statements to check if the string "hospitals.shp" is in the list.
#       - If True, print: <bol>hospitals.shp found in list!<eol>
#       - If False,
#           (i) Create a variable to store the path created by concatenating the workspace string and this name.
#           Print the contents of this variable.
#           (ii) Using arcpy.Exists() and the above variable, check if it exists on your computer:
#           - If True,
#               (1) print: <bol><Variable from (d) (i)> exists!<eol>
#               (2) Add "hospitals.shp" as the second item in the list.
#           - If False, do nothing.
#   (e) Print the contents of the list.
#   IMPORTANT: Remember to import arcpy before using any of the arcpy functionality.
print("\n ##### Question 3 ################################################################### \n")  # Ignore this line
# Write your code below

# Given list stored in a variable. Do not modify this. Use this variable in order to complete all tasks.
list_of_shapefiles = ["bike_routes.shp", "parcels.shp"]

# Import the arcpy module
import arcpy

print("\n ### Q3 (a) ### \n")  # Ignore this line
# Q3 (a) Set the arcpy environment property for workspace to the "data" folder on your computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data"
# Q3 (a) Print the contents of the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")

print("\n ### Q3 (b) ### \n")  # Ignore this line
# Q3 (b) Check if the string "bike_routes.shp" is in the list
if "bike_routes.shp" in list_of_shapefiles:
    # Q3 (b) (i) If it is in the list: New variable stores the path created by concatenating the workspace and the
    # name of the shapefile from the list
    bike_routes_path = f"{arcpy.env.workspace}\\{list_of_shapefiles[list_of_shapefiles.index('bike_routes.shp')]}"
    # Q3 (b) (i) Print the contents of this variable
    print(f"Bike Routes Path: {bike_routes_path}")
    # Q3 (b) (ii) Check if the path exists using the arcpy.Exists() function and the variable from (b) (i)
    if arcpy.Exists(bike_routes_path):
        # Q3 (b) (ii) If the path exists, print: <bol><Variable from (b) (i)> exists!<eol>
        print(f"{bike_routes_path} exists!")
    # Q3 (b) (ii) Use elif or else to set up what happens if the path does not exist.
    else:
        # Q3 (b) (ii) If the path does not exist, remove the item from the list
        list_of_shapefiles.remove("bike_routes.shp")
# Q3 (b) Use elif or else to set up what happens if the string "bike_routes.shp" is not in the list
else:
    # Q3 (b) If it is not in the list: print <bol>bike_routes.shp not found in list!<eol>
    print("bike_routes.shp not found in list!")

print("\n ### Q3 (c) ### \n")  # Ignore this line
# Q3 (c) Print the contents of the list
print("Updated List of Shapefile Names :", list_of_shapefiles)

print("\n ### Q3 (d) ### \n")  # Ignore this line
# Q3 (d) Check if the string "hospitals.shp" is in the list
if "hospitals.shp" in list_of_shapefiles:
    # Q3 (d) If it is in the list: print: <bol>hospitals.shp found in list!<eol>
    print("hospitals.shp found in list!")
# Q3 (d) Use elif or else to set up what happens if the string "hospitals.shp" is not in the list
else:
    # Q3 (d) (i) If it is not in the list: New variable stores the path created by concatenating the workspace and the
    # name of the shapefile
    hospitals_path = f"{arcpy.env.workspace}\\hospitals.shp"
    # Q3 (d) (i) Print the contents of this variable
    print(f"Hospitals Path: {hospitals_path}")
    # Q3 (d) (ii) Check if the path exists using the arcpy.Exists() function and the variable from (d) (i)
    if arcpy.Exists(hospitals_path):
        # Q3 (d) (ii) (1) If the path exists, print: <bol><Variable from (d) (ii)> exists!<eol>
        print(f"{hospitals_path} exists!")
        # Q3 (d) (ii) (2) If the path exists, add the string "hospitals.shp" as the second item in the list
        list_of_shapefiles.insert(1, "hospitals.shp")
    # Q3 (d) (ii) If the path does not exist: No code necessary.

print("\n ### Q3 (e) ### \n")  # Ignore this line
# Q3 (e) Print the contents of the list
print("Updated List of Shapefile Names:", list_of_shapefiles)

# End Q3
#######################################################################################################################
# TODO Q4: Spatial Reference
#   In this question, you will create spatial reference objects for two coordinate systems and print their properties.
#   (a) Create a spatial reference object for the Geographic Coordinate System for St Paul Island in Alaska using its
#   WKID/Factory Code.
#   (b) Print the following properties for this spatial reference object in the following output format:
#   <bol><Property Name>: <Property Value><eol>
#       (i) GCS Name
#       (ii) GCS Code
#       (iii) Spheroid Name
#       (iv) Type
#       (v) Angular Unit Name
#   (c) Create a spatial reference object for the Projected Coordinate System for NAD 1983 HARN Arizona State Plane
#   Central FIPS 0202 International Feet using its WKID/Factory Code.
#   (d) Print the following properties for this spatial reference object in the following output format:
#   <bol><Property Name>: <Property Value><eol>
#       (i) PCS Name
#       (ii) PCS Code
#       (iii) Projection Name
#       (iv) Type
#       (v) Linear Unit Name
print("\n ##### Question 4 ################################################################### \n")  # Ignore this line
# Write your code below

# Import arcpy module
import arcpy

print("\n ### Q4 (a) ### - No Output \n")  # Ignore this line
# Q4 (a) Look up the WKID for the Geographic Coordinate System (GCS) for St Paul Island in Alaska on the Esri Help
# documentation website. Use the SpatialReference class to create the object and assign to a new variable.
gcs_st_paul = arcpy.SpatialReference(4137)

print("\n ### Q4 (b) ### \n")  # Ignore this line
# Q4 (b) (i) Print the GCS Name property in the format <bol><Property Name>: <Property Value><eol>
print(f"GCS Name: {gcs_st_paul.GCSName}")
# Q4 (b) (ii) Print the GCS Code property in the format <bol><Property Name>: <Property Value><eol>
print(f"GCS Code: {gcs_st_paul.GCSCode}")
# Q4 (b) (iii) Print the Spheroid Name property in the format <bol><Property Name>: <Property Value><eol>
print(f"Spheroid Name: {gcs_st_paul.spheroidName}")
# Q4 (b) (iv) Print the Type property in the format <bol><Property Name>: <Property Value><eol>
print(f"Type: {gcs_st_paul.type}")
# Q4 (b) (v) Print the Angular Unit Name property in the format <bol><Property Name>: <Property Value><eol>
print(f"Angular Unit Name: {gcs_st_paul.angularUnitName}")

print("\n ### Q4 (c) ### - No Output\n")  # Ignore this line
# Q4 (c) Look up the WKID for theProjected Coordinate System (PCS) for NAD 1983 HARN Arizona State Plane Central
# FIPS 0202 International Feet on the Esri Help documentation website. Use the SpatialReference class to create the
# object and assign to a new variable.
pcs_az_state_plane = arcpy.SpatialReference(2868)

print("\n ### Q4 (d) ### \n")  # Ignore this line
# Q4 (d) (i) Print the PCS Name property in the format <bol><Property Name>: <Property Value><eol>
print(f"PCS Name: {pcs_az_state_plane.PCSName}")
# Q4 (d) (i) Print the PCS Name property in the format <bol><Property Name>: <Property Value><eol>
print(f"PCS Code: {pcs_az_state_plane.PCSCode}")
# Q4 (d) (i) Print the Projection Name property in the format <bol><Property Name>: <Property Value><eol>
print(f"Projection Name: {pcs_az_state_plane.projectionName}")
# Q4 (d) (i) Print the Type property in the format <bol><Property Name>: <Property Value><eol>
print(f"Type: {pcs_az_state_plane.type}")
# Q4 (d) (i) Print the Linear Unit Name property in the format <bol><Property Name>: <Property Value><eol>
print(f"Linear Unit Name: {pcs_az_state_plane.linearUnitName}")

# End Q4
#######################################################################################################################
# TODO Q5: Union Tool
#   In this question, you will execute the Union tool on two shapefiles.
#   (a) Set the following arcpy environment properties and print their contents:
#       (i) workspace - Set to the "data" folder for this class.
#       (ii) overwriting output - Ensure that outputs are overwritten.
#   (b) Create two variables to store the following names of shapefiles and print their contents:
#       (i) Input Feature # 1: parks.shp
#       (ii) Input Feature # 2: geology.shp
#   (c) Write if, elif and/or else statements to check if BOTH shapefiles exist on your computer.
#       - If True:
#           (i) Create a variable to store a list with both of these variables as two items and print its contents.
#           (ii) Execute the Union tool using the following parameters and assign the result to a variable called
#           union_result:
#              - in_features: Variable that stores the list from (c)
#              - out_feature_class: parks_geology_union.shp
#              - join_attributes: use the default option
#              - cluster_tolerance: use the default option
#              - gaps: Ensure that features ARE created for areas that are completely enclosed by polygons.
#            (iii) Print ALL geoprocessing messages from the union tool execution using the result object stored in
#            variable union_result.
#       - If False, print: <bol><Variable from (b) (i)> and/or <Variable from (b) (ii)> do not exist. Cannot execute
#                               union tool!<eol>
#   IMPORTANT: Remember to import arcpy before using any of the arcpy functionality.
print("\n ##### Question 5 ################################################################### \n")  # Ignore this line
# Write your code below

# Import arcpy module
import arcpy

print("\n ### Q5 (a) ### \n")  # Ignore this line
# Q5 (a) (i) Set the arcpy environment property for workspace to the "data" folder on your computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data"
# Q5 (a) (i) Print the contents of the arcpy environment property for workspace
print(f"arcpy workspace property: {arcpy.env.workspace}")

# Q5 (a) (ii) Set the arcpy environment property to overwrite outputs
arcpy.env.overwriteOutput = True
# Q5 (a) (ii) Print the contents of the arcpy environment property that overwrites outputs
print(f"arcpy Overwrite Output property: {arcpy.env.overwriteOutput}")

print("\n ### Q5 (b) ### \n")  # Ignore this line
# Q5 (b) (i) New variable stores the string "parks.shp"
input_feature_1 = "parks.shp"
# Q5 (b) (i) Print the contents of the new variable
print(f"Input Feature # 1: {input_feature_1}")

# Q5 (b) (ii) New variable stores the string "geology.shp"
input_feature_2 = "geology.shp"
# Q5 (b) (ii) Print the contents of the new variable
print(f"Input Feature # 2: {input_feature_2}")

print("\n ### Q5 (c) ### - No Output \n")  # Ignore this line
# Q5 (c) Check if BOTH shapefiles exist on your computer using the arcpy.Exists() function and the
# variables from (b) (i) & (ii). You will have to use a logical operator to check for both files.
if arcpy.Exists(input_feature_1) and arcpy.Exists(input_feature_2):
    print("\n ### Q5 (c) (i) ### \n")  # Ignore this line
    # Q5 (c) (i) If both shapefiles exist, new variable will store a list with the names of these shapefiles using the
    # two variables
    list_of_shp = [input_feature_1, input_feature_2]
    # Q5 (c) (i) Print the contents of this variable
    print(f"In Features for the Union Tool: {list_of_shp}")
    print("\n ### Q5 (c) (ii) ### \n")  # Ignore this line
    # Q5 (c) (ii) If both shapefiles exist, execute the union tool using the given parameters and assign the result
    # object to a variable called union_result
    union_result = arcpy.analysis.Union(in_features=list_of_shp,
                                        out_feature_class="parks_geology_union.shp",
                                        join_attributes="",
                                        cluster_tolerance="",
                                        gaps="NO_GAPS")
    print("\n ### Q5 (c) (iii) ### \n")  # Ignore this line
    # Q5 (c) (iii) Print ALL geoprocessing messages using the result object stored in variable union_result.
    print(union_result.getMessages())
# Q5 (c) Use elif or else to set up what happens if both shapefiles do not exist.
else:
    # Q5 (c) If both shapefile do not exist, print the following line
    # <bol><Variable from (b) (i)> and/or <Variable from (b) (ii)> do not exist. Cannot execute union tool!<eol>
    print(f"{input_feature_1} and/or {input_feature_2} do not exist. Cannot execute union tool!")

# End Q5
#######################################################################################################################
# TODO Q6: Average Nearest Neighbor Tool
#   In this question, you will execute the Average Nearest Neighbor tool to determine if the points in a shapefile are
#   clustered, dispersed or random.
#   (a) Set the following arcpy environment variables and print their contents:
#       (i) workspace - Set to the "data" folder for this class.
#       (ii) overwriting output - Ensure that outputs are overwritten.
#   (b) Create a variable to store the "facilities.shp" shapefile name and print its contents.
#   (c) Write if, elif and/or else statements to check if the shapefile from (b) exists on your computer.
#       - If True:
#           (i) Execute the Average Nearest Neighbor tool using the following parameters and assign the result object
#           to a variable called ann_result:
#              - Input_Feature_Class: Variable that stores the name from (b)
#              - Distance_Method: Use the Manhattan distance method
#              - Generate_Report: Ensure that a graphical summary is created as an HTML file
#              - Area: use the default option
#           (ii) Print the following using the result object stored in variable ann_result:
#               <bol>Nearest Neighbor Results for facilities.shp:<eol>
#               <bol>Z-Score = <the Z-Score><eol>
#               <bol>p-value = <the p-value><eol>
#               <bol>HTML Report Location =  <the path to the HTML summary><eol>
#           (iii) Create a new variable to store the nearest neighbor index value as a float from the result object
#           stored in variable ann_result and print its content.
#           (iv) Write if, elif and/or else statements to check for all of the following conditions and perform the
#           necessary actions as stated below.
#              (1) If the nearest neighbor index is less than 1, print the following:
#                  <bol>Nearest Neighbor Index = <Value from (iii)>, point pattern exhibits clustering.<eol>
#              (2) If the nearest neighbor index is greater than 1, print the following:
#                  <bol>Nearest Neighbor Index = <Value from (iii)>, point pattern exhibits dispersion.<eol>
#              (3) For all other values of the nearest neighbor index, print the following:
#                  <bol>Nearest Neighbor Index = <Value from (iii)>, point pattern exhibits randomness.<eol>
#   IMPORTANT: Remember to import arcpy before using any of the arcpy functionality.
print("\n ##### Question 6 ################################################################### \n")  # Ignore this line
# Write your code below

# Import arcpy module
import arcpy

print("\n ### Q6 (a) ### \n")  # Ignore this line
# Q6 (a) (i) Set the arcpy environment variable for workspace to the "data" folder on your computer
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data"
# Q6 (a) (i) Print the contents of the arcpy environment variable for workspace
print(f"arcpy workspace variable: {arcpy.env.workspace}")

# Q6 (a) (ii) Set the arcpy environment variable to overwrite outputs
arcpy.env.overwriteOutput = True
# Q6 (a) (ii) Print the contents of the arcpy environment variable that overwrites outputs
print(f"arcpy Overwrite Output variable: {arcpy.env.overwriteOutput}")

print("\n ### Q6 (b) ### \n")  # Ignore this line
# Q6 (b)New variable stores the string "facilities.shp"
input_feature = "facilities.shp"
# Q6 (b) Print the contents of the new variable
print(f"Input Feature: {input_feature}")

print("\n ### Q6 (c) ### - No Output \n")  # Ignore this line
# Q6 (c) Check if the "facilities.shp" shapefile exists on your computer using the arcpy.Exists() function and the
# variable from (b)
if arcpy.Exists(input_feature):
    print("\n ### Q6 (c) (i) ### \n")  # Ignore this line
    # Q6 (c) (i) If it exists, execute the Average Nearest Neighbor tool using the given parameters and assign the
    # result object to a variable called ann_result
    ann_result = arcpy.stats.AverageNearestNeighbor(Input_Feature_Class=input_feature,
                                                      Distance_Method="MANHATTAN_DISTANCE",
                                                      Generate_Report="GENERATE_REPORT",
                                                      Area="")
    print("\n ### Q6 (c) (ii) ### \n")  # Ignore this line
    # Q6 (c) (ii) Print: <bol>Nearest Neighbor Results for facilities.shp:<eol>
    print("Nearest Neighbor Results for facilities.shp:")
    # Q6 (c) (ii) Print using the result object stored in ann_result: <bol>Z-Score = <the Z-Score><eol>
    print(f"Z-Score = {ann_result[1]}")
    # Q6 (c) (ii) Print using the result object stored in ann_result: <bol>p-value = <the p-value><eol>
    print(f"p-value = {ann_result[2]}")
    # Q6 (c) (ii) Print using the result object stored in ann_result:
    # <bol>HTML Report Location =  <the path to the HTML summary><eol>
    print(f"HTML Report Location = {ann_result[5]}")
    print("\n ### Q6 (c) (iii) ### \n")  # Ignore this line
    # Q6 (c) (iii) New variable stores the nearest neighbor index value as a float from the result object stored
    # in ann_result
    nn_index = float(ann_result[0])
    # Q6 (c) (iii) Print the contents of the new variable
    print(f"Nearest Neighbor Index: {nn_index}")
    print("\n ### Q6 (c) (iv) ### - No Output \n")  # Ignore this line
    # Q6 (c) (iv) (1) Check if the nearest neighbor index is less than 1
    if nn_index < 1:
        print("\n ### Q6 (c) (iv) (1) ### \n")  # Ignore this line
        # Q6 (c) (iv) (1) If True, print:
        # <bol>Nearest Neighbor Index = <Value from (iii)>, point pattern exhibits clustering.<eol>
        print(f"Nearest Neighbor Index = {nn_index}, point pattern exhibits clustering.")
    # Q6 (c) (iv) (2) Use elif to check if the nearest neighbor index is greater than 1
    elif nn_index > 1:
        print("\n ### Q6 (c) (iv) (2) ### \n")  # Ignore this line
        # Q6 (c) (iv) (2) If True, print:
        # <bol>Nearest Neighbor Index = <Value from (iii)>, point pattern exhibits dispersion.<eol>
        print(f"Nearest Neighbor Index = {nn_index}, point pattern exhibits dispersion.")
    # Q6 (c) (iv) (3) Use else to check for all other values
    else:
        print("\n ### Q6 (c) (iv) (3) ### \n")  # Ignore this line
        # Q6 (c) (iv) (3) If True, print:
        # <bol>Nearest Neighbor Index = <Value from (iii)>, point pattern exhibits randomness.<eol>
        print(f"Nearest Neighbor Index = {nn_index}, point pattern exhibits randomness.")
# Q6 (c) Use elif or else to set up what happens if the shapefile does not exist.
else:
    # Q6 (c) If the shapefile does not exist, print the following line
    # <bol><Variable from (b)> does not exist. Cannot execute Average Nearest Neighbor tool!<eol>
    print(f"{input_feature} does not exist. Cannot execute Average Nearest Neighbor tool!")

# End Q6
#######################################################################################################################
# END OF ASSIGNMENT 2
#######################################################################################################################
