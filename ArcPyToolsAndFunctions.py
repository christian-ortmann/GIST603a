# -------------------------------------------------------------------------------
# Name:        ArcPyToolsAndFunctions
# Purpose:     Script for code used as part of the ArcPy Tools & Functions
#               Lecture Video
# Author:      Dr. Yoganand Korgaonkar
# Created:     10/22/2020
# -------------------------------------------------------------------------------

# Importing the ArcPy site package
import arcpy

##########################################################################
# ArcPy Tools
# Example of Buffer Tool

# # Input Feature Class
in_fc = "C:/workspace/gist/data/hospitals.shp"

# # Output Feature Class
out_fc = "C:/workspace/gist/results/hosp_buffer.shp"

# # Execute the tool with a Buffer Radius of 5000 Meters
arcpy.Buffer_analysis(in_fc,out_fc,"5000 Meters")


# ##########################################################################
# # ArcPy Functions

arcpy.GetInstallInfo()

# # Extensions
help(arcpy.CheckExtension)

# # Check if license is available
# # Can return 4 possible values:
# #   1) Available - is available to set
# #   2) Unavailable - is unavailable to set
# #   3) NotLicensed - license is not valid
# #   4) Failed - system failure during request
arcpy.CheckExtension("Spatial")
arcpy.CheckExtension("StreetMap")

# # Exists Function

# # Returns True if file is found at location
arcpy.Exists("C:/workspace/gist/data/zip.shp")

# # Returns False if file is not found at location
arcpy.Exists("C:/workspace/gist/zip.shp")

