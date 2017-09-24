mxd = arcpy.mapping.MapDocument("CURRENT")
mxd.author = "James Jones"
mxd.save()
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyrFile = arcpy.mapping.Layer(r"C:\Users\James Jones\Documents\ArcGIS\NHL_Teams.lyr")
arcpy.mapping.AddLayer(df, lyrFile)
arcpy.mapping.ExportToPDF(mxd, r'C:\Users\James Jones\Documents\ArcGIS\NHL_Teams.pdf')
lyr = arcpy.mapping.ListLayers(mxd)[0]
lyr.name = "NHL Teams"
lyr.visible = False
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
lyr.visible = True
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
lyrExtent = lyr.getSelectedExtent()
df.extent = lyrExtent
arcpy.mapping.ExportToPDF(mxd, r'C:\Users\James Jones\Documents\ArcGIS\Hockey_Teams.pdf')
PDFdoc = arcpy.mapping.PDFDocumentCreate(r'C:\Users\James Jones\Documents\ArcGIS\'Hockey_Overview.pdf')
PDFdoc.appendPages(r'C:\Users\James Jones\Documents\ArcGIS\'NHL_Teams.pdf')
PDFdoc.appendPages(r'C:\Users\James Jones\Documents\ArcGIS\NHL_Teams.pdf')
PDFdoc.appendPages(r'C:\Users\James Jones\Documents\ArcGIS\Hockey_Teams.pdf')
PDFdoc.saveAndClose()

