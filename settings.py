# -*- coding: utf-8 -*-
from PyQt4.QtCore import QSettings

class settings:
    def __init__(self):
        self.s = QSettings()
        
        #database settings
        self.conName = self.s.value("vmm/conname", "")
        self.dbhost = self.s.value("vmm/dbhost", "")
        self.dbport = self.s.value("vmm/dbport", "5432")
        self.database = self.s.value("vmm/database", "")
        self.dbuser = self.s.value("vmm/dbuser", "")
        self.dbpassw = self.s.value("vmm/dbpassw", r'')
        #layer 
        self.schema = self.s.value("vmm/schema", r'')
        self.polyLayer =  self.s.value("vmm/polyLayer", r'')
        self.polyLayerGeom = self.s.value("vmm/polyLayerGeom", r'')
        self.polyLayerName = self.s.value("vmm/polyLayerName", r'')
        
        self._pgSettings()

    def _getProxySettings(self):
        self.proxyEnabled = self.proxyHost = self.proxyPort = self.proxyUser = self.proxyPassword = None
        self.proxyUrl = ""
        proxyEnabled = self.s.value("proxy/proxyEnabled", "")
        if proxyEnabled == 1 or self.proxyEnabled == "true":
            self.proxyEnabled = True
            self.proxyHost = self.s.value("proxy/proxyHost", "" )
            self.proxyPort = self.s.value("proxy/proxyPort", "" )
            self.proxyUser = self.s.value("proxy/proxyUser", "" )
            self.proxyPassword = self.s.value("proxy/proxyPassword", "" )
            
            self.proxyUrl = "http://"
            if self.proxyUser and self.proxyPassword:
                self.proxyUrl += self.proxyUser + ':' + self.proxyPassword + '@'
            self.proxyUrl += self.proxyHost + ':' + self.proxyPort


    def _pgSettings(self):
        self.s.beginGroup("PostgreSQL/connections")
        cons = self.s.childGroups()
        self.connections = {}
        for con in cons:
            self.s.beginGroup(con)
            self.connections[con] = { n: self.s.value(n) for n in self.s.childKeys()}
            self.s.endGroup()
        self.s.endGroup()

    def saveSettings(self ):
        #database settings
        self.s.setValue("vmm/conname", self.conName)
        self.s.setValue("vmm/dbhost", self.dbhost)
        self.s.setValue("vmm/database", self.database)
        self.s.setValue("vmm/dbport", self.dbport)
        self.s.setValue("vmm/dbuser", self.dbuser)
        self.s.setValue("vmm/dbpassw", self.dbpassw)

        #layer 
        self.s.setValue("vmm/schema", self.schema)
        self.s.setValue("vmm/polyLayer", self.polyLayer)
        self.s.setValue("vmm/polyLayerGeom", self.polyLayerGeom)
        self.s.setValue("vmm/polyLayerName", self.polyLayerName )
