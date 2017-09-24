import arcpy, os, time, traceback
from arcpy import env

env.overwriteOutput = True

inFC = arcpy.GetParameterAsText(0)
buffDist = arcpy.GetParameterAsText(1)
buffUnits = arcpy.GetParameterAsText(2)

env.workspace = r'C:\Users\James Jones\Documents\ArcGIS\NHL Teams\NHL_Teams.gdb'
nhl = "NHL_Teams"
ahl = "AHL_Teams"
echl = "ECHL_Teams"
chl = "CHL_Teams"
sphl = "SPHL_Teams"

leagues = [nhl, ahl, echl, chl, sphl]

try:
    arcpy.MakeFeatureLayer_management(inFC, "buffLyr")

    count = 0
    for l in leagues:
        lLyr = l + "Lyr"
        arcpy.MakeFeatureLayer_management(l, lLyr)
        arcpy.SelectLayerByLocation_management("buffLyr", "WITHIN_A_DISTANCE", lLyr, str(buffDist) + " " + str(buffUnits))
        matchcount = int(arcpy.GetCount_management(lLyr)[0])
        count += matchcount

    print("There are " + str(count) + " teams within " + str(buffDist) + " of your selected layer.")
    arcpy.AddMessage("There are " + str(count) + " teams within " + str(buffDist) + " of your selected layer.")
except:
    print("Uh oh!")
    print("Error at " + time.strftime("%c"))

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg  = "PYTHON ERRORS:\n Traceback info:\n" + tbinfo + "Error info:\n" + str(sys.exc_info()[1])
    msg = "\nArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(pymsg)
    arcpy.AddError(msg)
    exit