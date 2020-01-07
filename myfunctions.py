# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import tempfile
from PyQt4.QtGui import *

import numpy as np
from qgis.core import *


def getlayerbyName(self, layers, name):
    """Pass a list with all mapcanvas layers, returns a layer or None if not found """
    for layer in layers:
        if layer.name() == name:
            return layer
        

def getlayerbyHostTableName(layers, host, tablename):
    """Pass a list with all mapcanvas layers, returns a layer or None if not found """
    for layer in layers:
        uri = QgsDataSourceURI(layer.dataProvider().dataSourceUri())
        if uri.host () == host and uri.table() == tablename:
            return layer

def addPostGISLayer(host, port, dbname, username, password, schema, table, layername, geom_col, key_col):
    '''Adds a PostGIS table to the map'''
    uri = QgsDataSourceURI()
    uri.setConnection(str(host), str(port), str(dbname), str(username), str(password))
    uri.setDataSource(schema, table, geom_col, '', key_col)
    vlayer = QgsVectorLayer(uri.uri(), layername, "postgres")

    if not vlayer.isValid():
        print "Layer failed to load!Invalid layer!"
        return None
        
    # QgsMapLayerRegistry.instance().addMapLayer(vlayer)
    if not vlayer:
        return None
    else:
        return vlayer
  
  
#==============================================================================================================================                     
def startfile(path):
    
    if not os.path.isfile(path):
        print "File %s doesn't exist in disk" % str(path)
        QMessageBox.information(None, "File %s does not exist." % str(path))

    if os.path.isfile(path):        
        if sys.platform == 'linux2':
            subprocess.call(["xdg-open", path])
        else:
            os.startfile(path)
  #==============================================================================================================================     
   

def writeBinary(data,suffix):
    
    try:
          
        temp = tempfile.NamedTemporaryFile( suffix=suffix, dir=tempfile.gettempdir(), delete=False)
        
        temp.write(data)
        temp.seek(0)
        temp.close()
        
        path = temp.name
        return path
        
    except IOError, e:    
        print "Error %d: %s" % (e.args[0], e.args[1])
        QMessageBox.information(None, "Error %d: %s" % (e.args[0], e.args[1]))
        return None
        
def readBinary(file):

    try:
        fin = open(file, "rb")
        img = fin.read()
        
        
    except IOError, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        
        if fin:
            fin.close()
            return img

def validatedDefaultSymbol(geometryType):
    symbol = QgsSymbolV2.defaultSymbol(geometryType)
    if symbol is None:
        if geometryType == QGis.Point:
              symbol = QgsMarkerSymbolV2()
        elif geometryType == QGis.Line:
            symbol = QgsLineSymbolV2 ()
        elif geometryType == QGis.Polygon:
            symbol = QgsFillSymbolV2 ()
    return symbol

def applyGraduatedSymbologyStandardMode(layer, field, classes, mode):
    symbol = validatedDefaultSymbol(layer.geometryType())
    colorRamp = QgsVectorGradientColorRampV2.create({'color1':'254,240,217,255', 'color2':'179,0,0,255', 'stops':'0.25;253,204,138,255:0.50;252,141,89,255:0.75;227,74,51,255'})
    renderer = QgsGraduatedSymbolRendererV2.createRenderer(layer, field, classes, mode, symbol, colorRamp)
    # renderer.setSizeScaleField("deiktis")
    layer.setRendererV2 (renderer)
    return layer
    

def geomSql(sql):
        geomsql = sql.replace("select", "select the_geom,");
        return geomsql.lower() 



def updatecolors(layer, field):
    '''Updates colors for graduated classification and standard deviation mode: blue for values<mean and red for values>mean'''
    
    renderer = layer.rendererV2()
    values = getFloatsFromAttributeTable(layer, field)

    # blue=[(255,247,251),(236,231,242),(208,209,230),(166,189,219),(116,169,207),(54,144,192),(5,112,176),(4,90,141),(2,56,88)]
    blue = ['#C4DBFD', '#9CC2FC', '#74AAFB', '#4D92F9', '#257AF8', '#0763ED', '#064BB2', '#043A8B', '#032963', '#02193B', '#010814'] 
    red = [(255, 247, 236), (254, 232, 200), (253, 212, 158), (253, 187, 132), (252, 141, 89), (239, 101, 72), (215, 48, 31), (179, 0, 0), (127, 0, 0), (20, 0, 0)]

    ranges = renderer.ranges()
    myindex = 0
    bluecolorindex = 0
    redcolorindex = 0
    R = 8
    B = 81
    G = 156
    belowAVGvalues = []
    for range in ranges:
        print range.label ()
        print range.lowerValue(), '-', range.upperValue()
        if range.upperValue() < np.mean(values) or range.lowerValue() < np.mean(values):
            belowAVGvalues.append(myindex)
            bluecolorindex += 1
            myindex = myindex + 1
        elif range.upperValue() > np.mean(values) or range.lowerValue() > np.mean(values):
            symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
            color = QColor()
            color.setRed(red[redcolorindex][0])
            color.setGreen(red[redcolorindex][1])
            color.setBlue(red[redcolorindex][2])
            symbol.setColor(color)
            renderer.updateRangeSymbol (myindex, symbol)
            redcolorindex += 1
            myindex = myindex + 1
        
        bluecolorindex = 0
        rbelowAVGvalues = belowAVGvalues[::-1]  # invert list 
        for rangeindex in rbelowAVGvalues :
            print rangeindex
            symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
            symbol.setColor(QColor(blue[bluecolorindex]))
            renderer.updateRangeSymbol (rangeindex, symbol)
            bluecolorindex += 1
    return layer

def getFloatsFromAttributeTable(layer, fieldName):
    iter = layer.getFeatures()
    values = []
    for feature in iter:
        idx = layer.fieldNameIndex(fieldName)
        print type(feature.attributes()[idx])
        if feature.attributes()[idx]==NULL:
             continue
        values.append(feature.attributes()[idx])
    return values

def fix_file_extension(filename, extension):
    """Fix filename extension. Checks if extension is present to filename else appends extension to filename"""
    if not filename.endswith(extension):
        filename = filename + extension
    return filename
