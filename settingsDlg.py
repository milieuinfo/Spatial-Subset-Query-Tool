# -*- coding: utf-8 -*-
import os

from PyQt4 import QtGui, QtCore

from settings import settings
from ui_settings import Ui_settingsDlg


class settingsDlg(QtGui.QDialog):
    def __init__(self, iface,  parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowFlags( self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint )
        #self.setWindowFlags( self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.iface = iface
    
        # initialize locale
        locale = QtCore.QSettings().value("locale/userLocale", "nl")
        if not locale: locale == 'nl' 
        else: locale = locale[0:2]
        localePath = os.path.join(os.path.dirname(__file__), 'i18n', '{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QtCore.QTranslator()
            self.translator.load(localePath)
            if QtCore.qVersion() > '4.3.3': QtCore.QCoreApplication.installTranslator(self.translator)
    
        self._initGui()

    def _initGui(self):
        """setup the user interface"""
        self.ui = Ui_settingsDlg()
        self.ui.setupUi(self)
        
        self.s = settings()

        self.ui.timeOutNum.setValue( self.s.timeout )
        self.ui.dbHostEdit.setText( self.s.dbhost )
        self.ui.dbNameEdit.setText( self.s.database )
        self.ui.dbPortEdit.setText( self.s.dbport )
        self.ui.dbUserEdit.setText( self.s.dbuser )
        self.ui.dbPasswordEdit.setText( self.s.dbpassw )

        self.ui.dbSchemaEdit.setText(self.s.schema)
        self.ui.polygonLayerEdit.setText(self.s.polyLayer)
        self.ui.nameColEdit.setText(self.s.polyLayerName)
        self.ui.geomColEdit.setText(self.s.polyLayerGeom)
        
        self.accepted.connect(self.commit)

    def commit(self):
        self.s.timeout = self.ui.timeOutNum.value()

        self.s.dbhost = self.ui.dbHostEdit.text()
        self.s.database =  self.ui.dbNameEdit.text()
        self.s.dbport = self.ui.dbPortEdit.text()
        self.s.dbuser = self.ui.dbUserEdit.text()
        self.s.dbpassw = self.ui.dbPasswordEdit.text()

        self.s.schema =  self.ui.dbSchemaEdit.text()
        self.s.polyLayer = self.ui.polygonLayerEdit.text()
        self.s.polyLayerName = self.ui.nameColEdit.text()
        self.s.polyLayerGeom = self.ui.geomColEdit.text()

        self.s.saveSettings()