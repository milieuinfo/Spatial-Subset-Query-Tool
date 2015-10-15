# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created: Thu Oct 15 21:51:34 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_settingsDlg(object):
    def setupUi(self, settingsDlg):
        settingsDlg.setObjectName(_fromUtf8("settingsDlg"))
        settingsDlg.resize(452, 225)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/vmmQry/images/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settingsDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(settingsDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(settingsDlg)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.connectionCbx = QtGui.QComboBox(self.frame)
        self.connectionCbx.setObjectName(_fromUtf8("connectionCbx"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.connectionCbx)
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.line_3)
        self.dbSchemaLbl = QtGui.QLabel(self.frame)
        self.dbSchemaLbl.setObjectName(_fromUtf8("dbSchemaLbl"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.dbSchemaLbl)
        self.dbSchemaCbx = QtGui.QComboBox(self.frame)
        self.dbSchemaCbx.setObjectName(_fromUtf8("dbSchemaCbx"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.dbSchemaCbx)
        self.polygonTblLbl = QtGui.QLabel(self.frame)
        self.polygonTblLbl.setObjectName(_fromUtf8("polygonTblLbl"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.polygonTblLbl)
        self.polygonLayerCbx = QtGui.QComboBox(self.frame)
        self.polygonLayerCbx.setObjectName(_fromUtf8("polygonLayerCbx"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.polygonLayerCbx)
        self.nameColLbl = QtGui.QLabel(self.frame)
        self.nameColLbl.setObjectName(_fromUtf8("nameColLbl"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.nameColLbl)
        self.nameColCbx = QtGui.QComboBox(self.frame)
        self.nameColCbx.setObjectName(_fromUtf8("nameColCbx"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.nameColCbx)
        self.geomColLbl = QtGui.QLabel(self.frame)
        self.geomColLbl.setObjectName(_fromUtf8("geomColLbl"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.geomColLbl)
        self.geomColEdit = QtGui.QLineEdit(self.frame)
        self.geomColEdit.setEnabled(False)
        self.geomColEdit.setObjectName(_fromUtf8("geomColEdit"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.geomColEdit)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(settingsDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settingsDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settingsDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDlg)

    def retranslateUi(self, settingsDlg):
        settingsDlg.setWindowTitle(_translate("settingsDlg", "Instellingen", None))
        self.label.setText(_translate("settingsDlg", "Kies database connectie:", None))
        self.dbSchemaLbl.setText(_translate("settingsDlg", "Database Schema:", None))
        self.polygonTblLbl.setText(_translate("settingsDlg", "Polygoon tabel:", None))
        self.nameColLbl.setText(_translate("settingsDlg", "Kolom met namen:", None))
        self.geomColLbl.setText(_translate("settingsDlg", "Kolom met geometrien:", None))

import resources_rc
