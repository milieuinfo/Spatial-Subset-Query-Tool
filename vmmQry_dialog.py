# -*- coding: utf-8 -*-
import sys
import os

from qgis.gui import QgsMessageBar
from PyQt4 import QtGui, QtCore

import pgHelper
from geometryhelper import geometryHelper
from ui_vmmQry_baseDlg import Ui_vmmQryDlg
from settings import settings


class vmmQryDialog(QtGui.QDialog):
    def __init__(self, iface, parent=None):
        QtGui.QDialog.__init__(self, None)
        self.setWindowFlags( self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint )

        # initialize locale
        locale = QtCore.QSettings().value("locale/userLocale", "en")[0:2] 
        if not locale in ['en','nl'] : locale = 'en'

        localePath = os.path.join(os.path.dirname(__file__), 'i18n', '{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QtCore.QTranslator()
            self.translator.load(localePath)
            QtCore.QCoreApplication.installTranslator(self.translator)

        self.iface = iface
        self._initGui()

    def _initGui(self):
        self.ui = Ui_vmmQryDlg()
        self.ui.setupUi(self)

        self.firstShow = True
        self.gh = geometryHelper(self.iface)
        self.pg = None
        self.s = settings()

        #setup a message bar
        self.bar = QgsMessageBar()
        self.bar.setSizePolicy( QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed )
        self.ui.verticalLayout.addWidget(self.bar)

        #events
        self.ui.addLayerBtn.clicked.connect(self.addLayerClick)

    #overwrite
    def show(self):
        QtGui.QDialog.show(self)
        self.setWindowModality(0)
        if self.firstShow:
            try:
                self.pg = pgHelper.pgHelper(
                  database=self.s.database , user=self.s.dbuser , passw=self.s.dbpassw, host=self.s.dbhost)
            except:
                self.bar.pushMessage( "Error", QtCore.QCoreApplication.translate('vmmQry', 
                     "Kan niet verbinden met database, is deze correct ingesteld?"), level=QgsMessageBar.CRITICAL )
                return
            gemeenten = self.pg.listField( self.s.polyLayer , self.s.polyLayerName, self.s.schema)
            lagen = self.pg.listGeoLayers(self.s.schema)
            self.ui.gemeenteCbx.addItems(gemeenten)
            self.ui.gemeenteCbx.insertItem(0,'')
            self.ui.gemeenteCbx.setCurrentIndex(0)
            self.ui.lyrList.addItems(lagen)
            self.firstShow = False

    def addLayerClick(self):
        gemeente = self.ui.gemeenteCbx.currentText()
        selItems = [n.text() for n in self.ui.lyrList.selectedItems()]

        for layer in selItems:
           targetGeom =  self.pg.getGeomName( layer , self.s.schema )
           sql = ""
           if self.ui.bboxSelBtn.isChecked() and gemeente <> '':
               sql= self.pg.spatialWhereClause( targetGeom, self.s.polyLayerGeom , self.s.polyLayer,
                    "\"{0}\" = '{1}'".format(self.s.polyLayerName , gemeente ), bboxOnly=True, schema= self.s.schema )
           elif self.ui.borderSelBtn.isChecked() and gemeente <> '':
               sql= self.pg.spatialWhereClause( targetGeom, self.s.polyLayerGeom , self.s.polyLayer,
                    "\"{0}\" = '{1}'".format(self.s.polyLayerName , gemeente ), bboxOnly=False, schema= self.s.schema )

           self.pg.loadPostGISLayer(layer, targetGeom, sql, schema= self.s.schema )

