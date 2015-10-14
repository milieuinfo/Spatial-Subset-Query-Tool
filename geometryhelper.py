# -*- coding: utf-8 -*-
import os

from qgis.core import *
from PyQt4.QtGui import QFileDialog, QColor
from qgis.gui import QgsVertexMarker


class geometryHelper:
    def __init__(self , iface ):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.adreslayerid = ''
    
    @staticmethod
    def getGetMapCrs(iface):
        new24 = QGis.QGIS_VERSION_INT >= 20400
        return ( iface.mapCanvas().mapSettings().destinationCrs() if new24
                 else  iface.mapCanvas().mapRenderer().destinationCrs() )
        
    def prjPtToMapCrs( self, xy , fromCRS=4326 ):
        point = QgsPoint( xy[0], xy[1] )
        fromCrs = QgsCoordinateReferenceSystem(fromCRS)
        toCrs = self.getGetMapCrs(self.iface)
        xform = QgsCoordinateTransform( fromCrs, toCrs )
        return   xform.transform( point )
    
    def prjPtFromMapCrs( self, xy , toCRS=31370 ):
        point = QgsPoint( xy[0], xy[1] )
        toCrs = QgsCoordinateReferenceSystem(toCRS)
        fromCrs = self.getGetMapCrs(self.iface)
        xform = QgsCoordinateTransform( fromCrs, toCrs )
        return   xform.transform( point )

    def prjLineFromMapCrs(self, lineString, toCRS=4326 ):
        fromCrs = self.getGetMapCrs(self.iface)
        toCrs = QgsCoordinateReferenceSystem(toCRS)
        xform = QgsCoordinateTransform(fromCrs, toCrs)
        wgsLine = [ xform.transform( xy ) for xy in  lineString.asPolyline()]
        return QgsGeometry.fromPolyline( wgsLine )

    def prjLineToMapCrs(self, lineString, fromCRS=4326 ):
        fromCrs = QgsCoordinateReferenceSystem(fromCRS)
        toCrs = self.getGetMapCrs(self.iface)
        xform = QgsCoordinateTransform(fromCrs, toCrs)
        if isinstance(lineString, QgsGeometry):
            wgsLine = [ xform.transform( xy ) for xy in  lineString.asPolyline()]
        if hasattr(lineString, '__iter__'):
            wgsLine = [ xform.transform( QgsPoint(xy[0], xy[1]) ) for xy in  lineString]
        return QgsGeometry.fromPolyline( wgsLine )

    def zoomtoRec(self, xyMin, xyMax , crs=None):
        """zoom to rectangle from 2 points with given crs, default= mapCRS"""
        if crs is None:
            crs = self.getGetMapCrs(self.iface)
            
        maxpoint = QgsPoint(xyMax[0], xyMax[1])
        minpoint = QgsPoint(xyMin[0], xyMin[1])
        
        pmaxpoint = self.prjPtToMapCrs(maxpoint, crs)
        pminpoint = self.prjPtToMapCrs(minpoint, crs)
        
        # Create a rectangle to cover the new extent
        rect = QgsRectangle( pmaxpoint, pminpoint )
    
        # Set the extent to our new rectangle
        self.iface.mapCanvas().setExtent(rect)
        # Refresh the map
        self.iface.mapCanvas().refresh()
    
    def zoomtoRec2(self, bounds, crs=None):
        "zoom to rectangle from a list containing: [xmin,ymin,xmax,ymax] with given crs, default= mapCRS"
        if not bounds or len(bounds) != 4:
            return
        if crs is None:
            crs = self.getGetMapCrs(self.iface)
            
        maxpoint = QgsPoint( bounds[0], bounds[1])
        minpoint = QgsPoint( bounds[2], bounds[3])
        
        pmaxpoint = self.prjPtToMapCrs(maxpoint, crs)
        pminpoint = self.prjPtToMapCrs(minpoint, crs)
      
        # Create a rectangle to cover the new extent
        rect = QgsRectangle( pmaxpoint, pminpoint )
    
        # Set the extent to our new rectangle
        self.iface.mapCanvas().setExtent(rect)
        # Refresh the map
        self.iface.mapCanvas().refresh()
      
    def _saveToFile( self, sender, startFolder=None ):
        'save to file'
        #"Shape Files (*.shp);;Geojson File (*.geojson);;GML ( *.gml);;Comma separated value File (excel) (*.csv);;MapInfo TAB (*.TAB);;Any File (*.*)"
        filter = "ESRI Shape Files (*.shp);;SpatiaLite (*.sqlite);;Any File (*.*)" #show only formats with update capabilty
        Fdlg = QFileDialog()
        Fdlg.setFileMode(QFileDialog.AnyFile)
        fName = QFileDialog.getSaveFileName(sender, "open file", filter=filter, directory=startFolder)
        if fName:
          ext = os.path.splitext( fName )[1]
          if "SHP" in ext.upper():
            flType = "ESRI Shapefile"
          elif "SQLITE" in ext.upper():
            flType = "SQLite" 
          elif "GEOJSON" in ext.upper():  #no update possible -> hidden
            flType = "GeoJSON"
          elif "GML" in ext.upper():
            flType = "GML"
          elif 'TAB' in ext.upper():
            flType = 'MapInfo File'
          elif 'KML' in ext.upper():
            flType = 'KML'
          else:
            fName = fName + ".shp"
            flType = "ESRI Shapefile"
          return (fName , flType )
        else:
            return None
      
    def addPointGraphic(self, xy, color="#FFFF00", size=1, pen=10, markerType=QgsVertexMarker.ICON_BOX ):
        "create a point Graphic at location xy and return it"
        x, y = list( xy )[:2]
        m = QgsVertexMarker(self.canvas)
        m.setCenter(QgsPoint(x,y))
        m.setColor(QColor(color))
        m.setIconSize(size)
        m.setIconType(markerType) 
        m.setPenWidth(pen)
        return m

    @staticmethod
    def getBoundsOfPointArray( pointArray, delta=100):
        minX = 1.7976931348623157e+308
        maxX = -1.7976931348623157e+308
        minY = 1.7976931348623157e+308
        maxY = -1.7976931348623157e+308
    
        for xy in pointArray:
            x, y = list(xy)[:2]
            if x > maxX: maxX = x
            if x < minX: minX = x
            if y > maxY: maxY = y
            if y < minY: minY = y
          
        Xdelta = (maxX - minX) /delta
        Ydelta = (maxY - minY) /delta
        
        return [ minX - Xdelta, minY - Ydelta, maxX + Xdelta, maxY + Ydelta]
    
    @staticmethod
    def getBoundsOfPoint( x, y, delta=None):
      if delta is None:
        if x >= 360:
            delta = 300 #x bigger then 360 -> meters
        else:
            delta = 0.0025 #x smaller then 360 -> degrees
      
        xmax = x + delta
        xmin = x - delta
        ymax = y + delta
        ymin = y - delta
        
        return [xmin, ymin, xmax,ymax]