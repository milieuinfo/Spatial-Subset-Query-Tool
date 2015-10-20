# -*- coding: utf-8 -*-
import os, webbrowser
from PyQt4 import QtGui, QtCore
from pgHelper import pgHelper
from settings import settings
from ui_settings import Ui_settingsDlg


class settingsDlg(QtGui.QDialog):
    # noinspection PyArgumentList
    def __init__(self, iface,  parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowFlags( self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint )
        #self.setWindowFlags( self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # initialize locale
        locale = QtCore.QSettings().value("locale/userLocale", "en")[0:2] 
        if not locale in ['en','nl'] : locale = 'en'
        
        localePath = os.path.join(os.path.dirname(__file__), 'i18n', '{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QtCore.QTranslator()
            self.translator.load(localePath)
            QtCore.QCoreApplication.installTranslator(self.translator)

        self.iface = iface
        self.helpUrl = "https://github.com/milieuinfo/Spatial-Subset-Query-Tool/blob/master/README.md" if locale <> 'nl' \
            else "https://github.com/milieuinfo/Spatial-Subset-Query-Tool/blob/master/README_NL.md"
        self.pg = None
        self._initGui()

    def _initGui(self):
        """setup the user interface"""
        self.ui = Ui_settingsDlg()
        self.ui.setupUi(self)
        
        self.setup()
        
        self.ui.connectionCbx.currentIndexChanged.connect(self.connectionChanged)
        self.ui.dbSchemaCbx.currentIndexChanged.connect(self.schemaChanged)
        self.ui.polygonLayerCbx.currentIndexChanged.connect(self.polygonLayerChanged)
        self.ui.buttonBox.helpRequested.connect(self.help)
        self.accepted.connect(self.commit)

    def setup(self):
        self.s = settings()
        self.ui.connectionCbx.clear()
        self.ui.connectionCbx.addItems( [""] + self.s.connections.keys() )
        self.initDBsettings()

    def initDBsettings(self):
        cons = self.s.connections.keys() 
        if self.s.conName in cons:
          try:
            self.ui.connectionCbx.setCurrentIndex(cons.index(self.s.conName) +1)
            self.pg = pgHelper(self.s.dbhost, self.s.dbport, self.s.database, self.s.dbuser, self.s.dbpassw)
          except:
            return
          
          schemas = self.pg.listSchemas()
          self.ui.dbSchemaCbx.clear()
          if self.s.schema in schemas:
             self.ui.dbSchemaCbx.addItems( [""] + schemas )
             self.ui.dbSchemaCbx.setCurrentIndex( schemas.index(self.s.schema) + 1)
          
             geoLayers = self.pg.listGeoLayers(self.s.schema)
             self.ui.polygonLayerCbx.clear()
             if self.s.polyLayer in geoLayers:
                self.ui.polygonLayerCbx.addItems( [""] + geoLayers )
                self.ui.polygonLayerCbx.setCurrentIndex(geoLayers.index(self.s.polyLayer) + 1)
                
                colNames = self.pg.listTableNames(self.s.polyLayer, self.s.schema)
                self.ui.nameColCbx.clear()
                if self.s.polyLayerName in colNames: 
                   self.ui.nameColCbx.addItems( [""] + colNames )
                   self.ui.nameColCbx.setCurrentIndex(colNames.index(self.s.polyLayerName) + 1)    
                   self.ui.geomColEdit.setText( self.s.polyLayerGeom )

    def help(self):
        webbrowser.open_new_tab(self.helpUrl)

    def connectionChanged(self):
        conName = self.ui.connectionCbx.currentText()
        self.ui.dbSchemaCbx.clear()
        
        if conName <> "":
          con = self.s.connections[conName]
          self.pg = pgHelper( con["host"], con["port"], con["database"], con["username"], con["password"] )
          schemas = self.pg.listSchemas()
          self.ui.dbSchemaCbx.clear()
          self.ui.dbSchemaCbx.addItems( [""] + schemas )
        else:
          self.pg = None
          
    def schemaChanged(self):
        if not self.pg: return
        
        schema = self.ui.dbSchemaCbx.currentText()
        self.ui.polygonLayerCbx.clear()
        
        if schema <> "":
           self.ui.polygonLayerCbx.clear()
           self.ui.polygonLayerCbx.addItems([""] + self.pg.listGeoLayers(schema) )
        
    def polygonLayerChanged(self):
        if not self.pg: return
      
        schema = self.ui.dbSchemaCbx.currentText()
        polygonLayer = self.ui.polygonLayerCbx.currentText()
        
        self.ui.nameColCbx.clear()
        self.ui.geomColEdit.setText("")
        
        if polygonLayer <> "":
           colNames = self.pg.listTableNames(polygonLayer, schema)
           self.ui.nameColCbx.clear()
           self.ui.nameColCbx.addItems(colNames) 
           geomName = self.pg.getGeomName(polygonLayer, schema) 
           if geomName: self.ui.geomColEdit.setText(geomName)

    def commit(self):
        if not self.pg: return
          
        self.s.conName = self.ui.connectionCbx.currentText()
        self.s.dbhost = self.pg.host
        self.s.database = self.pg.database
        self.s.dbport = self.pg.port
        self.s.dbuser = self.pg.user
        self.s.dbpassw = self.pg.passw

        self.s.schema =  self.ui.dbSchemaCbx.currentText()
        self.s.polyLayer = self.ui.polygonLayerCbx.currentText()
        self.s.polyLayerName = self.ui.nameColCbx.currentText()
        self.s.polyLayerGeom = self.ui.geomColEdit.text()

        self.s.saveSettings()
