import arcpy, os
from arcpy import env

env.overwriteOutput = True
gdb = r'C:\Users\James Jones\Documents\ArcGIS\WV.gdb'

geocodeResult = r'C:\Users\James Jones\Documents\ArcGIS\NHL Teams\ECHL_Teams.shp'
wvFC = os.path.join(gdb, "Counties")
wvECHL = os.path.join(gdb, "WV_echlTeams")
echlLyr = r'C:\Users\James Jones\Documents\ArcGIS\ECHL.lyr'
wvLyr = r'C:\Users\James Jones\Documents\ArcGIS\WV.lyr'
gc = 'ECHL'
wvL = 'West Virginia'

arcpy.MakeFeatureLayer_management(geocodeResult, gc)
arcpy.MakeFeatureLayer_management(wvFC, wvL)
arcpy.SaveToLayerFile_management(gc, echlLyr)
arcpy.SaveToLayerFile_management(wvL, wvLyr)

##Establish the Initial MXD and data frame
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

##Adds the layers to the current data frame
echl = arcpy.mapping.ListLayers(mxd)[0]
wv = arcpy.mapping.ListLayers(mxd)[1]

##Renames the layers and turns them off
echl.name = "East Coast Hockey League"
wv.name = "West Virginia"
echl.visible = True
wv.visible = True
arcpy.RefreshTOC()
arcpy.RefreshActiveView()

arcpy.SelectLayerByLocation_management(gc, 'INTERSECT', wvL)
arcpy.CopyFeatures_management(gc, wvECHL)
arcpy.MakeFeatureLayer_management(wvECHL, "Wheeling Nailers")

wv.visible = False
echl.visible = False
arcpy.RefreshTOC()
arcpy.RefreshActiveView()

arcpy.mapping.ExportToPDF(mxd, r'C:\Users\James Jones\Documents\ArcGIS\WheelingNailers.pdf')