# ---------------------------------------------------------------------------------------------------------------------
# Name:        Assignment5_Solution.py
# Purpose:     Solution Script for Assignment 5
# Author:      Dr. Yoganand Korgaonkar
# ---------------------------------------------------------------------------------------------------------------------
print("\n ##### ASSIGNMENT 5 ##### \n")  # Ignore this line
#######################################################################################################################
# TODO Q1: Copy Data
#   In this question, you will create a new geodatabase and copy rasters that will be used later in this assignment.
#   (a) Create a folder called "A5_Results" on your computer. You can do this manually or use os.mkdir() in Python.
#   (b) Create a geodatabase called Assignment5.gdb in A5_Results using an appropriate ArcGIS geoprocessing tool.
#   (c) Copy the following rasters from ExploringSpatialData\Sturgis.gdb to Assignment5.gdb:
#       (i) canopy
#       (ii) landcover
#       (iii) topo30m
print("\n ##### Question 1 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module
import arcpy
# Import the os module
import os

print("\n ### Q1 (a) ### - os.mkdir() \n")  # Ignore this line
# Q1 (a) New variable stores the path to new folder called "A5_Results" on your computer
folder_path = r"E:\workspace\PythonProgramming\Results\A5_Results"
# Q1 (a) Create the folder using os.mkdir()
os.mkdir(folder_path)
# Q1 (a) Print a message that it is created
print(f"Folder 'A5_Results' was created at {folder_path}")

print("\n ### Q1 (b) ### - CreateFileGDB \n")  # Ignore this line
# Q1 (b) Create a geodatabase called Assignment5.gdb in A5_Results using the CreateFileGDB tool and assign the result
# object to a new variable called gdb_result
gdb_result = arcpy.management.CreateFileGDB(out_folder_path=folder_path,
                                            out_name="Assignment5.gdb")
# Q1 (b) Print ALL geoprocessing messages using the result object stored in the variable gdb_result
print(gdb_result.getMessages())

print("\n ### Q1 (c) ### - CopyRaster \n")  # Ignore this line
# Q1 (c) New variable stores a list of all the given raster names - canopy, landcover, topo30m
given_rasters = ["canopy", "landcover", "topo30m"]
# Q1 (c) Set the arcpy environment property for workspace to ExploringSpatialData\Sturgis.gdb
arcpy.env.workspace = r"E:\workspace\PythonProgramming\data\ExploringSpatialData\Sturgis.gdb"
# Q1 (c) New variable stores a list of raster names returned by an appropriate arcpy list function
ras_list = arcpy.ListRasters()
# Q1 (c) Use a for loop on the list of raster names
for r_name in ras_list:
    # Check if the raster name from the iteration is in the list of raster names to be copied.
    if r_name in given_rasters:
        # Print the name of the raster
        print(f"Raster Name: {r_name}")
        # Copy the raster to "A5_Results\Assignment5.gdb" using the CopyRaster tool. The
        # output should have the same name and assign the result object to a variable called cr_result.
        cr_result = arcpy.management.CopyRaster(in_raster=r_name,
                                                out_rasterdataset=f"{gdb_result}\\{r_name}")
        # Print ALL geoprocessing messages using the result object stored in the variable cr_result
        print(cr_result.getMessages())

# End Q1
#######################################################################################################################
# TODO Q2: Creating Point Geometries
#   In this question you will add and edit points to the sturgis_pts.shp feature class using a CSV file.
#   (a) Create an empty point feature class called sturgis_pts in A5_Results\Assignment5.gdb with a
#   NAD 1983 UTM Zone 13N spatial reference.
#   (b) Add the following fields to the sturgis_pts feature class:
#       (i) Name: W_ID, Type: Integer, Alias: Watershed ID
#       (ii) Name: WSHED, Type: Text, Alias: Watershed Name, Length: 50
#   (c) Create and add point geometries and the ID and watershed name using the pourpoints.csv file to the empty
#   sturgis_pts feature class using an Insert Cursor.
#   (d) Move the points for the Whitewood watersheds 50 meters to the South and 23 meters to the West.
#   (e) Print the X & Y coordinates, watershed ID and name for all features in sturgis_pts using a Search Cursor.
print("\n ##### Question 2 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module
import arcpy
# Import the csv module
import csv

# Set the arcpy environment property for workspace to A5_Results\Assignment5.gdb
arcpy.env.workspace = r"E:\workspace\PythonProgramming\Results\A5_Results\Assignment5.gdb"

print("\n ### Q2 (a) ### - CreateFeatureclass\n")  # Ignore this line
# Q2 (a) New variable stores the spatial reference object for NAD 1983 UTM Zone 13N
spatial_ref = arcpy.SpatialReference(26913)
# Q2 (a) Execute the CreateFeatureclass tool to create a point feature class called sturgis_pts in
# A5_Results\Assignment5.gdb and assign the result object to a variable called cf_result
cf_result = arcpy.management.CreateFeatureclass(out_path=arcpy.env.workspace,
                                                out_name="sturgis_pts",
                                                geometry_type="POINT",
                                                spatial_reference=spatial_ref)
# Q2 (a) Print ALL geoprocessing messages using the result object stored in the variable cf_result
print(cf_result.getMessages())

print("\n ### Q2 (b) ### - AddFields\n")  # Ignore this line
# Q2 (b) New variable stores a list for the new field W_ID in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
wid_field = ["W_ID", "SHORT", "Watershed ID"]
# Q2 (b) New variable stores a list for the new field WSHED in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
wshed_field = ["WSHED", "TEXT", "Watershed Name", 50]
# Q2 (b) Execute the AddFields tool to add two new fields to the empty feature class using the two lists created above
# and assign the result object to a variable called af_result
af_result = arcpy.management.AddFields(in_table=cf_result,
                                       field_description=[wid_field, wshed_field])
# Q2 (b) Print ALL geoprocessing messages using the result object stored in the variable af_result
print(af_result.getMessages())

print("\n ### Q2 (c) ### - CSV file and Insert Cursor - No Output\n")  # Ignore this line
# Q2 (c) New variable stores the path and name to the pourpoints CSV file
csv_location = r"E:\workspace\PythonProgramming\Assignments\pourpoints.csv"
# Q2 (c) Use the with statement to open the pourpoints CSV file in read mode
with open(csv_location, "r") as csv_file:
    # New variable stores a DictReader object for the CSV file
    d_reader = csv.DictReader(csv_file)
    # Use a for loop to iterate over each row in the DictReader object
    for row in d_reader:
        # New variable stores the x coordinate from the row
        x_coord = row["X_COORD"]
        # New variable stores the y coordinate from the row
        y_coord = row["Y_COORD"]
        # New variable stores the ID of the watershed from the row
        wshed_id = row["W_ID"]
        # New variable stores the name of the watershedfrom the row
        wshed_name = row["NAME"]
        # New variable stores a Point object created using the X & Y coordinates
        pt_obj = arcpy.Point(x_coord, y_coord)
        # New variable stores a PointGeometry object created using the above Point object and spatial reference
        pt_geom = arcpy.PointGeometry(pt_obj, spatial_ref)
        # Use the with statement to set up an insert cursor on the sturgis_pts feature class with fields SHAPE@, W_ID
        # and WSHED
        with arcpy.da.InsertCursor(af_result, ["SHAPE@", "W_ID", "WSHED"]) as in_cursor:
            # Use the .insertRow() method to insert the PointGeometry, ID and name of the watershed
            in_cursor.insertRow([pt_geom, wshed_id, wshed_name])

print("\n ### Q2 (d) ### - Update Whitewood Points - No Output\n")  # Ignore this line
# Q2 (d) New variable stores the where clause to search for watershed names that begin with the string "Whitewood"
where_clause = f"\"WSHED\" LIKE 'Whitewood%'"
# Q2 (d) Use the with statement to set up an update cursor on the sturgis_pts feature class. Provide the "SHAPE@X" and
# "SHAPE@Y" fields and the where clause to the cursor to retrieve the records for the Whitewood watershed
with arcpy.da.UpdateCursor(af_result, ["SHAPE@X", "SHAPE@Y"], where_clause) as u_cursor:
    # Use a for loop on the iterator of the records in the cursor
    for row in u_cursor:
        # Update the X coordinate by subtracting 23
        row[0] = row[0] - 23
        # Update the Y coordinate by subtracting 50
        row[1] = row[1] - 50
        # Update the row with the new X & Y coordinates using the .updateRow() method to save changes
        u_cursor.updateRow(row)

print("\n ### Q2 (e) ### - Search Cursor to Print Attributes\n")  # Ignore this line
# Q2 (e) New variable stores a list of field names to provide to the search cursor - SHAPE@X, SHAPE@Y, W_ID and WSHED
field_names = ["SHAPE@X", "SHAPE@Y", "W_ID", "WSHED"]
# Q2 (e) Use the with statement to set up a search cursor on the sturgis_pts feature class
with arcpy.da.SearchCursor(af_result, field_names) as s_cursor:
    # Use a for loop on the iterator of the records in the cursor
    for row in s_cursor:
        # Print the attributes for each record
        print(f"ID: {row[2]} - NAME: {row[3]} at X: {row[0]:.4f} and Y: {row[1]:.4f}")

# End Q2
#######################################################################################################################
# TODO Q3: Creating Watersheds
#   In this question, you will create watersheds from the sturgis_pts feature class.
#   (a) Use the topo30m raster and sturgis_pts.shp to create watersheds by using the following process:
#       (i) Execute the arcpy.sa.Fill tool
#       (ii) Execute the arcpy.sa.FlowDirection tool
#       (iii) Execute the arcpy.sa.FlowAccumulation tool
#       (iv) Execute the arcpy.sa.SnapPourPoint tool
#       (v) Execute the arcpy.sa.Watershed tool
#   Note: Save all output rasters in A5_Results\Assignment5.gdb
#   (b) Print the names of all the rasters in A5_Results\Assignment5.gdb
print("\n ##### Question 3 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module
import arcpy

# Set the arcpy environment property for workspace to A5_Results\Assignment5.gdb
arcpy.env.workspace = r"E:\workspace\PythonProgramming\Results\A5_Results\Assignment5.gdb"

print("\n ### Q3 (a) (i) ### - Fill\n")  # Ignore this line
# Q3 (a) (i) Execute the Fill tool using the topo30m digital elevation model raster and assign the raster output to a
# new variable called filled_dem
filled_dem = arcpy.sa.Fill(in_surface_raster="topo30m")
# Q3 (a) (i) Save the raster output to disk with the name topo30m_fill
filled_dem.save("topo30m_fill")
# Q3 (a) (i) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q3 (a) (ii) ### - FlowDirection\n")  # Ignore this line
# Q3 (a) (ii) Execute the FlowDirection tool using the filled DEM and assign the raster output to a new variable
# called fd
fd = arcpy.sa.FlowDirection(in_surface_raster=filled_dem)
# Q3 (a) (ii) Save the raster output to disk with the name topo30m_fd
fd.save('topo30m_fd')
# Q3 (a) (ii) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q3 (a) (iii) ### - FlowAccumulation\n")  # Ignore this line
# Q3 (a) (iii) Execute the FlowAccumulation tool using the flow direction and assign the raster output to a new variable
# called fa
fa = arcpy.sa.FlowAccumulation(in_flow_direction_raster=fd)
# Q3 (a) (iii) Save the raster output to disk with the name topo30m_fa
fa.save('topo30m_fa')
# Q3 (a) (iii) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q3 (a) (iv) ### - SnapPourPoint\n")  # Ignore this line
# Q3 (a) (iv) Execute the SnapPourPoint tool using sturgis_pts and flow accumulation and a snap distance of 50m and
# assign the raster output to a new variable called pp
pp = arcpy.sa.SnapPourPoint(in_pour_point_data=af_result,
                            in_accumulation_raster=fa,
                            snap_distance=50)
# Q3 (a) (iv) Save the raster output to disk with the name topo30m_pp
pp.save('topo30m_pp')
# Q3 (a) (iv) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q3 (a) (v) ### - Watershed\n")  # Ignore this line
# Q3 (a) (v) Execute the Watershed tool using the flow direction and the snapped pour points and assign the raster
# output to a new variable called sheds
sheds = arcpy.sa.Watershed(in_flow_direction_raster=fd,
                           in_pour_point_data=pp)
# Q3 (a) (v) Save the raster output to disk with the name topo30m_sheds
sheds.save('topo30m_sheds')
# Q3 (a) (v) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q3 (b) ### - Raster Names\n")  # Ignore this line
# Q3 (b) New variable stores a list of raster names returned by an appropriate arcpy list function
list_of_rasters = arcpy.ListRasters()
print(f"Rasters in {arcpy.env.workspace}:")
# Q3 (b) Use a for loop on the above list
for ras in list_of_rasters:
    # Q3 (b) Print the name of the raster in the iteration
    print(ras)

# End Q3
#######################################################################################################################
# TODO Q4: Updating Raster attribute table
#   In this question, you will add empty fields to the watershed raster attribute table and populate them with
#   information from the CSV file.
#   (a) Add the following fields to the attribute table of the watershed raster:
#       (i) Name: W_ID, Type: Integer, Alias: Watershed ID
#       (ii) Name: WSHED, Type: Text, Alias: Watershed Name, Length: 50
#       (iii) Name: AREA_HA, Type: Double, Alias: Watershed Area
#       (iv) Name: QUAL, Type: Text, Alias: Watershed Quality, Length: 20
#       (v) Name: CHK_BY, Type: Text, Alias: Checked By, Length: 50
#       (vi) Name: CHK_DATE, Type: Date, Alias: Checked on Date
#   (b) Fill in the above attributes as follows:
#       (i) W_ID --> From the column VALUE in the attribute table
#       (ii) WSHED --> From the CSV file
#       (iii) AREA_HA --> Calculate using the COUNT column in the attribute table
#       (iv) QUAL --> From the CSV file
#       (v) CHK_BY --> From the CSV file
#       (iv) CHK_DATE --> From the CSV file
#   (c) Print the ID, name, area in hectares, quality, checked by name and checked by date for all the watersheds
#   using a Search Cursor.
print("\n ##### Question 4 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module
import arcpy

# Set the arcpy environment property for workspace to A5_Results\Assignment5.gdb
arcpy.env.workspace = r"E:\workspace\PythonProgramming\Results\A5_Results\Assignment5.gdb"

print("\n ### Q4 (a) ### - AddFields\n")  # Ignore this line
# Q4 (a) (i) New variable stores a list for the new field W_ID in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
wid_field = ["W_ID", "SHORT", "Watershed ID"]
# Q4 (a) (ii) New variable stores a list for the new field WSHED in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
wshed_field = ["WSHED", "TEXT", "Watershed Name", 50]
# Q4 (a) (iii) New variable stores a list for the new field AREA_HA in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
area_ha_field = ["AREA_HA", "DOUBLE", "Watershed Area"]
# Q4 (a) (iv) New variable stores a list for the new field QUAL in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
qual_field = ["QUAL", "TEXT", "Watershed Quality", 20]
# Q4 (a) (v) New variable stores a list for the new field CHK_BY in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
chk_by_field = ["CHK_BY", "TEXT", "Checked By", 50]
# Q4 (a) (v) New variable stores a list for the new field CHK_DATE in the format:
# [Field Name, Field Type, {Field Alias}, {Field Length}, {Default Value}, {Field Domain}]
chk_date_field = ["CHK_DATE", "Date", "Checked on Date", 50]
# Q4 (a) New variable stores a list of all the above variables
fields_list = [wid_field, wshed_field, area_ha_field, qual_field, chk_by_field, chk_date_field]
# Q4 (a) Execute the AddFields tool to add the fields to the watersheds raster using the list of lists created above
# and assign the result object to a variable called af_result
af_result = arcpy.management.AddFields(in_table=sheds,
                                       field_description=fields_list)
# Q4 (a) Print ALL geoprocessing messages using the result object stored in the variable af_result
print(af_result.getMessages())

print("\n ### Q4 (b) ### - CSV file and Update Cursor - No Output\n")  # Ignore this line
# Q4 (b) Two new variables stores the mean cell width and mean cell height of the watersheds raster
mean_width = sheds.meanCellWidth
mean_height = sheds.meanCellHeight
# Q4 (b) New variable stores the cell area calculated by multiplying the width and height of the cell
cell_area = mean_width * mean_height
# Q4 (b) New variable stores the path and name to the pourpoints CSV file
csv_location = r"E:\workspace\PythonProgramming\Assignments\pourpoints.csv"
# Q4 (b) Use the with statement to open the pourpoints CSV file in read mode
with open(csv_location, "r") as csv_file:
    # New variable stores a DictReader object for the CSV file
    d_reader = csv.DictReader(csv_file)
    # Use a for loop to iterate over each row in the DictReader object
    for row in d_reader:
        # New variable stores the id of the watershed from the row
        wshed_id = row["W_ID"]
        # New variable stores the name of the watershed from the row
        wshed_name = row["NAME"]
        # New variable stores the quality of the watershed from the row
        qual = row["QUAL"]
        # New variable stores the checked by name from the row
        chk_by = row["CHK_BY"]
        # New variable stores the checked by date from the row
        chk_date = row["CHK_DATE"]
        # Q4 (b) New variable stores a list of field names to retrieve using the Update Cursor - COUNT, W_ID, WSHED,
        # AREA_HA, QUAL, CHK_BY and CHK_DATE
        fields_list = ["COUNT", "W_ID", "WSHED", "AREA_HA", "QUAL", "CHK_BY", "CHK_DATE"]
        # Q2 (d) New variable stores the where clause to search for watershed names that begin with the string
        # "Whitewood"
        where_clause = f"\"VALUE\" = {wshed_id}"
        # Use the with statement to set up an update cursor on the watersheds raster with the list of field names and
        # the where clause
        with arcpy.da.UpdateCursor(sheds.catalogPath, fields_list, where_clause) as u_cursor:
            # Use a for loop on the iterator of the records in the cursor
            for urow in u_cursor:
                # Update the watershed id in the record
                urow[1] = wshed_id
                # Update the watershed name in the record
                urow[2] = wshed_name
                # Update the watershed quality in the record
                urow[4] = qual
                # Calculate the area in square meters using the count field and the cell area
                area_sqm = cell_area * urow[0]
                # Convert the area to hectare - 1 ha = 10,000 square meters
                area_ha = area_sqm / 10000
                # Update the area in hectares in the record
                urow[3] = area_ha
                # Update the checked by name in the record
                urow[5] = chk_by
                # Update the checked by date in the record
                urow[6] = chk_date
                # Update the row with the new information using the .updateRow() method to save changes
                u_cursor.updateRow(urow)

print("\n ### Q4 (c) ### - Search Cursor to Print Attributes\n")  # Ignore this line
# Q4 (c) New variable stores a list of field names to provide to the search cursor - W_ID, WSHED, QUAL, AREA_HA, CHK_BY
# and CHK_DATE
field_names = ["W_ID", "WSHED", "AREA_HA", "QUAL", "CHK_BY", "CHK_DATE"]
# Q4 (c) Use the with statement to set up a search cursor on the watersheds raster
with arcpy.da.SearchCursor(sheds.catalogPath, field_names) as s_cursor:
    # Use a for loop on the iterator of the records in the cursor
    for row in s_cursor:
        # Print the attributes for each record
        print(f"ID: {row[0]} - NAME: {row[1]}\n\t"
              f"Area {row[2]} ha\n\t"
              f"Quality: {row[3]}\n\t"
              f"Checked By: {row[4]} on {row[5]}")

# End Q4
#######################################################################################################################
# TODO Q5: Suitability Analysis
#   In this question, you will find areas in the watersheds that have high canopy cover and land cover types of
#   grassland/herbaceous or shrub/scrub.
#   (a) Reclassify the canopy cover raster as follows:
#       (i) Pixel Values of 0 - 59 --> 0, representing Low canopy cover
#       (ii) Pixel Values of 60 - 100 --> 1, representing High canopy cover
#   (b) Reclassify the landcover raster as follows:
#       (i) Land cover types of Grassland/Herbaceous (VALUE = 71) or Shrub/Scrub (VALUE = 52) --> 1, representing
#       favorable land cover types
#       (ii) All other land cover types --> 0, representing unfavorable land cover types
#   (c) Reclassify the watersheds raster as follows:
#       (i) Pixel Value of 1 --> 10
#       (ii) Pixel Value of 2 --> 20
#       (iii) Pixel Value of 3 --> 30
#       (iv) Pixel Value of 4 --> 40
#       (v) Pixel Value of 5 --> 50
#       (vi) Pixel Value of 6 --> 60
#       (vii) Pixel Value of 7 --> 70
#       (viii) Pixel Value of 8 --> 80
#       (ix) Pixel Value of 9 --> 90
#   (d) Perform an addition of the reclassified canopy cover raster, the reclassified landcover raster and the
#   reclassified watershed raster.
#   (e) Calculate and print the area in hectare in the watersheds that meets both criteria using a search cursor.
#   (f) Print the names of all the rasters in A5_Results\Assignment5.gdb
print("\n ##### Question 5 ################################################################### \n")  # Ignore this line
# Write your code below

# Import the arcpy module
import arcpy

# Set the arcpy environment property for workspace to A5_Results\Assignment5.gdb
arcpy.env.workspace = r"E:\workspace\PythonProgramming\Results\A5_Results\Assignment5.gdb"

print("\n ### Q5 (a) ### - Reclassify the canopy cover\n")  # Ignore this line
# Q5 (a) New variable stores a RemapRange object to reclassify range 0 - 59 to 0 and range 60 - 100 to 1
remap_range = arcpy.sa.RemapRange([[0, 59, 0], [60, 100, 1]])
# Q5 (a) Execute the Reclassify tool on the VALUE field in the canopy raster using the remap range and assign the raster
# output to a new variable called r_canopy
r_canopy = arcpy.sa.Reclassify(in_raster="canopy",
                               reclass_field="VALUE",
                               remap=remap_range)
# Q5 (a) Save the raster output to disk with the name canopy_re
r_canopy.save('canopy_re')
# Q5 (a) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q5 (b) ### - Reclassify the land cover\n")  # Ignore this line
# Q5 (b) Execute the Con tool on the VALUE field in the canopy raster using the remap range and assign the raster
# output to a new variable called con_lc
con_lc = arcpy.sa.Con(in_conditional_raster="landcover",
                      in_true_raster_or_constant=1,
                      in_false_raster_or_constant=0,
                      where_clause="VALUE = 71 Or Value = 52")
# Q5 (b) Save the raster output to disk with the name landcover_re
con_lc.save('landcover_re')
# Q5 (b) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q5 (c) ### - Reclassify the watersheds raster\n")  # Ignore this line
# Q5 (c) New variable stores a RemapValue object to reclassify watershed values as given above
remap_value = arcpy.sa.RemapValue([[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90]])
# Q5 (c) Execute the Reclassify tool on the VALUE field in the watershed raster using the remap value and assign the
# raster output to a new variable called r_sheds
r_sheds = arcpy.sa.Reclassify(in_raster=sheds,
                               reclass_field="VALUE",
                               remap=remap_value)
# Q5 (c) Save the raster output to disk with the name sheds_re
r_sheds.save('sheds_re')
# Q5 (c) Print geoprocessing messages using the arcpy.GetMessages() function
print(arcpy.GetMessages())

print("\n ### Q5 (d) ### - Raster Addition - No Output\n")  # Ignore this line
# Q5 (d) Add the reclassified canopy cover, reclassified landcover and reclassified watersheds rasters and assign the
# raster output to a new variable called suit
suit = r_canopy + con_lc + r_sheds
# Q5 (d) Save the raster output to disk with the name suitability
suit.save('suitability')

print("\n ### Q5 (e) ### - Suitable Area\n")  # Ignore this line
# Q5 (e) Use the with statement to set up a search cursor on the suitability raster using the where clause and
# retrieve the Value and Count fields
with arcpy.da.SearchCursor("suitability", ["Value", "Count"]) as s_cursor:
    # Use a for loop on the iterator of the records in the cursor
    for row in s_cursor:
        # Check if the value ends with 2 so that it meets both the canopy and landcover criteria
        if row[0] % 10 == 2:
            # New variable stores the watershed id from the value field using integer division by 10
            w_id = row[0] // 10
            # New variable stores the calculated area in square meters using cell size and the count field
            area_sqm = cell_area * row[1]
            # New variable stores the calculated area in hectares. 1 ha = 10,000 square meters
            area_ha = area_sqm / 10000
            # Print the area and the watershed id
            print(f"Suitable Area in Watershed {w_id}: {area_ha:.2f} ha")

print("\n ### Q5 (f) ### - Raster Names\n")  # Ignore this line
# Q3 (c) New variable stores a list of raster names returned by an appropriate arcpy list function
list_of_rasters = arcpy.ListRasters()
print(f"Rasters in {arcpy.env.workspace}:")
# Q3 (c) Use a for loop on the above list
for ras in list_of_rasters:
    # Q3 (c) Print the name of the raster in the iteration
    print(ras)

# End Q5
#######################################################################################################################
# END OF ASSIGNMENT 5
#######################################################################################################################
