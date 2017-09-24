import arcpy, os

aprx = arcpy.mp.ArcGISProject("CURRENT")
path = r'C:\Users\James Jones\Documents\ArcGIS\Projects'
lyt = aprx.listLayouts("Title Page")[0]
lyt.exportToPDF(os.path.join(path, "TitlePage.pdf"))
lyt = aprx.listLayouts("Great Lakes Maps")[0]

scaleBar = lyt.listElements("MAPSURROUND_ELEMENT", "Scale Bar")[0]
mf = scaleBar.mapFrame
scaleBar.elementPositionX = mf.elementPositionX + 1.25
scaleBar.elementPositionY = mf.elementPositionY - 3

northArrow = lyt.listElements("MAPSURROUND_ELEMENT", "North Arrow")[0]
mf = northArrow.mapFrame
northArrow.elementPositionX = mf.elementPositionX + 6
northArrow.elementPositionY = mf.elementPositionY - 0.9

srText = lyt.listElements('TEXT_ELEMENT', 'Spatial Reference Text')[0]
srText.elementPositionX = northArrow.elementPositionX - 6
srText.elementPositionY = northArrow.elementPositionY - 1.5

title = lyt.listElements('TEXT_ELEMENT', 'Title')[0]
mf = lyt.listElements('MAPFRAME_ELEMENT', "Great Lakes")[0]
title.elementPositionX = mf.elementPositionX + (mf.elementWidth/2)

aprx.save()

title = lyt.listElements('TEXT_ELEMENT', 'Title')[0]

bkmks = mf.map.listBookmarks()
for bkmk in bkmks:
    mf.zoomToBookmark(bkmk)
    title.text = bkmk.name
    lyt.exportToPDF(os.path.join(path, bkmk.name+'.pdf'))

aprx.save()

pdfPath = os.path.join(path, 'GreatLakesMapbook.pdf')
pdfDoc = arcpy.mp.PDFDocumentCreate(pdfPath)

pdfDoc.appendPages(os.path.join(path, 'TitlePage.pdf'))
pdfDoc.appendPages(os.path.join(path, 'Lake Erie.pdf'))
pdfDoc.appendPages(os.path.join(path, 'Lake Huron.pdf'))
pdfDoc.appendPages(os.path.join(path, 'Lake Michigan.pdf'))
pdfDoc.appendPages(os.path.join(path, 'Lake Ontario.pdf'))
pdfDoc.appendPages(os.path.join(path, 'Lake Superior.pdf'))
pdfDoc.updateDocProperties(pdf_title='Great Lakes of North America', pdf_author='James Jones', pdf_subject='An overview of the Great Lakes.', pdf_keywords="Great Lakes; Erie; Michigan; Huron; Ontario; Superior",pdf_open_view="USE_THUMBS", pdf_layout='SINGLE_PAGE')
pdfDoc.saveAndClose()