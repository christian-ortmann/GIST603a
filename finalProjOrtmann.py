
#--------------------------------------------------
#imports
#--------------------------------------------------

import arcpy
import pandas as pd
import numpy as np
import os



#--------------------------------------------------
#inputs
#--------------------------------------------------

#csv of coordinates for point locations
point_loc = r'C:\Users\cortmann\Desktop\GIST603a\GIST603a\finalProjChiSq\nests_random.csv'
#raster layer that must have discrete classes
veg = r'C:\Users\cortmann\Desktop\GIST603a\GIST603a\finalProjChiSq\ChiSquareData.gdb'
#csv of ChiSq table
chi2 = r'C:\Users\cortmann\Desktop\GIST603a\GIST603a\finalProjChiSq\chi_square_table.csv'
#location to store outputs
storeOut = r'C:\Users\cortmann\Desktop\GIST603a\GIST603a\finalProjChiSq\finalProjOut' # raw text for output loc
#.txt for analysis results
chi2Results = r'C:\Users\cortmann\Desktop\GIST603a\GIST603a\finalProjChiSq\finalProjOut\chi2Results.txt'




#--------------------------------------------------
#outputs
#--------------------------------------------------

chi2Results




#--------------------------------------------------
#set up 
#--------------------------------------------------
arcpy.env.workspace = veg

#set spatial ref to NAD 1983 UTM Zone 13M
sr = arcpy.SpatialReference(26913)

#List all rasters in the geodatabase
raster = arcpy.ListRasters()

#add raster as vegLayer
arcpy.management.MakeRasterLayer(raster[0],'vegLayer')

#add nests.csv
arcpy.management.MakeXYEventLayer(point_loc,'X','Y','nestLayer', spatial_reference=sr)

#convert to .shp
arcpy.FeatureClassToShapefile_conversion('nestLayer', storeOut)




#---------------------------------------------------------------------
#Relate distribution of nests to the vegetation types 
#---------------------------------------------------------------------

#read out the vegetation types as a .dbf
arcpy.sa.Sample('vegLayer', storeOut+'/nestLayer.shp',  storeOut + '/sampleVeg.dbf', 'NEAREST')
#look at field (column) names (more for development, but can be helpful none the less)
arcpy.ListFields( storeOut + '/sampleVeg.dbf')

#look at field (column) names to find the count by veg type
arcpy.ListFields( storeOut +'/sampleVeg.dbf')
#use summary statistics to determine how many nests are in each veg type
arcpy.analysis.Statistics( storeOut+'/sampleVeg.dbf',  storeOut+'/sumVegTypes.dbf', [['veg_Band_1', "COUNT"]], 'veg_Band_1')

#convert to pandas data frame to make things easier
sv_array = arcpy.da.TableToNumPyArray( storeOut+'/sumVegTypes.dbf', '*')
sumVegDf= pd.DataFrame(sv_array)




#---------------------------------------------------------------------
#Proportional area from each vegetation type 
#---------------------------------------------------------------------

#get raster layer attributes by converting to a pandas dataframe
raster_array = arcpy.da.TableToNumPyArray('vegLayer', '*')
attrDf = pd.DataFrame(raster_array) #convert to df for easier processing

#calculate proportion of total area
attrDf['proportion'] = attrDf['Count']/sum(attrDf['Count'])




#---------------------------------------------------------------------
#Calculate statistics
#---------------------------------------------------------------------

#initalize observed value
attrDf['obs'] = 0

#loop through and grab expected nest per area from sumVegDf
for index, veg in attrDf.iterrows():
    # Check if the current value exists in sumVegDf['veg_BAND_1']
    if veg['Value'] in sumVegDf['veg_Band_1'].values:
        # Get the corresponding expected observed
        expected_value = sumVegDf.loc[sumVegDf['veg_Band_1'] == veg['Value'], 'COUNT_veg_'].values[0]
        attrDf.at[index, 'obs'] = expected_value  # Assign expected value
    else:
        attrDf.at[index, 'obs'] = 0  # Assign 0 if no match is found

#calculate chi2
attrDf['chi2'] = ((attrDf['obs'] - (sum(attrDf['obs'])*attrDf['proportion']))**2)/(sum(attrDf['obs'])*attrDf['proportion'])
chi2Sum = sum(attrDf['chi2'])

#degrees of freedom
dof = (len(attrDf['Type'])-1) * (2-1) #where two is the number of columns we are analyzing (expected and observed)

#calculate Cramer's V
q = min(len(attrDf['Type']),2)
cramVSum= (chi2Sum / (sum(attrDf['obs']) * q-1))**(1/2)


#open reference table
chi2Ref = pd.read_csv(chi2)


#grab chi2 for P = 0.05
theorChi2 = chi2Ref.loc[dof-1,'0.05'] #dof - 1 is to get the right index

#results
featureClassFileName = os.path.splitext(os.path.basename(point_loc))[0]
eq = ''
result = ''
inf = ''

if chi2Sum >= theorChi2:
    eq = 'Observed Chi-Square > Theoretical Chi-Square'
    result = f'We reject the null hypothesis\nPoints in the {featureClassFileName} feature class are NOT randomly distributed in the {arcpy.ListRasters()[0]} raster'
    infl = f'The classes in the {arcpy.ListRasters()[0]} raster strongly influence the distribution of points in the {featureClassFileName} feature class.'
else:
    eq = 'Observed Chi-Square <= Theoretical Chi-Square'
    result = f'We fail to reject the null hypothesis\nPoints in the {featureClassFileName} feature class are randomly distributed in the {arcpy.ListRasters()[0]} raster'
    infl = f"The classes in the {arcpy.ListRasters()[0]} raster weakly influence the distribution of points in the {featureClassFileName} feature class."





#---------------------------------------------------------------------
#write results to text file
#---------------------------------------------------------------------

final = open(chi2Results,'w')
final.writelines(
    "Chi Square Analysis Results\n\n"
    "Null Hypothesis: The points in nests are randomly distributed in the veg raster\n\n"
    "Point Features\n"
    f"  Feature Class Name: {featureClassFileName}\n"
    f"  Total Number of Points = {sum(attrDf['obs'])}\n\n"
    "Raster\n"
    f"  Raster Name:{arcpy.ListRasters()[0]}\n"
    f"  Total Number of Classes = {len(attrDf)}\n\n"
    "## Chi-Square Statistic\n\n"
    f"Observed Chi-Square = {chi2Sum}\n\n"
    f"Degrees of Freedom = ({len(attrDf['Type'])} - 1) X (2 - 1) = {dof}\n\n"
    f"Theoretical Chi-Square for P = 0.05 with {dof} Degrees of Freedom = {theorChi2}\n\n"
    f"{eq}\n\n"
    f"{result}\n\n"
    "## Cramer V Statistic\n\n"
    f"V = {cramVSum}\n\n"
    f"{infl}"
    )

final.close()



