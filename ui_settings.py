# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created: Wed Oct 14 17:48:20 2015
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
        settingsDlg.resize(441, 385)
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
        self.timeoutLbl = QtGui.QLabel(self.frame)
        self.timeoutLbl.setObjectName(_fromUtf8("timeoutLbl"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.timeoutLbl)
        self.timeOutNum = QtGui.QSpinBox(self.frame)
        self.timeOutNum.setObjectName(_fromUtf8("timeOutNum"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.timeOutNum)
        self.line_1 = QtGui.QFrame(self.frame)
        self.line_1.setMinimumSize(QtCore.QSize(50, 0))
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.line_1)
        self.dbHostLbl = QtGui.QLabel(self.frame)
        self.dbHostLbl.setObjectName(_fromUtf8("dbHostLbl"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.dbHostLbl)
        self.dbHostEdit = QtGui.QLineEdit(self.frame)
        self.dbHostEdit.setObjectName(_fromUtf8("dbHostEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dbHostEdit)
        self.dbNameLbl = QtGui.QLabel(self.frame)
        self.dbNameLbl.setObjectName(_fromUtf8("dbNameLbl"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.dbNameLbl)
        self.dbNameEdit = QtGui.QLineEdit(self.frame)
        self.dbNameEdit.setObjectName(_fromUtf8("dbNameEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dbNameEdit)
        self.dbPortLbl = QtGui.QLabel(self.frame)
        self.dbPortLbl.setObjectName(_fromUtf8("dbPortLbl"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.dbPortLbl)
        self.dbPortEdit = QtGui.QLineEdit(self.frame)
        self.dbPortEdit.setObjectName(_fromUtf8("dbPortEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dbPortEdit)
        self.dbSchemaLbl = QtGui.QLabel(self.frame)
        self.dbSchemaLbl.setObjectName(_fromUtf8("dbSchemaLbl"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.dbSchemaLbl)
        self.dbSchemaEdit = QtGui.QLineEdit(self.frame)
        self.dbSchemaEdit.setObjectName(_fromUtf8("dbSchemaEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.dbSchemaEdit)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setMinimumSize(QtCore.QSize(50, 0))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.line_2)
        self.dbUserLbl = QtGui.QLabel(self.frame)
        self.dbUserLbl.setObjectName(_fromUtf8("dbUserLbl"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.dbUserLbl)
        self.dbUserEdit = QtGui.QLineEdit(self.frame)
        self.dbUserEdit.setObjectName(_fromUtf8("dbUserEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.dbUserEdit)
        self.dbPasswordLbl = QtGui.QLabel(self.frame)
        self.dbPasswordLbl.setObjectName(_fromUtf8("dbPasswordLbl"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.dbPasswordLbl)
        self.dbPasswordEdit = QtGui.QLineEdit(self.frame)
        self.dbPasswordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.dbPasswordEdit.setObjectName(_fromUtf8("dbPasswordEdit"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.dbPasswordEdit)
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.SpanningRole, self.line_3)
        self.polygonTblLbl = QtGui.QLabel(self.frame)
        self.polygonTblLbl.setObjectName(_fromUtf8("polygonTblLbl"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.polygonTblLbl)
        self.polygonLayerEdit = QtGui.QLineEdit(self.frame)
        self.polygonLayerEdit.setObjectName(_fromUtf8("polygonLayerEdit"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.polygonLayerEdit)
        self.NameColLbl = QtGui.QLabel(self.frame)
        self.NameColLbl.setObjectName(_fromUtf8("NameColLbl"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.LabelRole, self.NameColLbl)
        self.nameColEdit = QtGui.QLineEdit(self.frame)
        self.nameColEdit.setObjectName(_fromUtf8("nameColEdit"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.FieldRole, self.nameColEdit)
        self.geomColLbl = QtGui.QLabel(self.frame)
        self.geomColLbl.setObjectName(_fromUtf8("geomColLbl"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.LabelRole, self.geomColLbl)
        self.geomColEdit = QtGui.QLineEdit(self.frame)
        self.geomColEdit.setObjectName(_fromUtf8("geomColEdit"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.geomColEdit)
        self.verticalLayout.addWidget(self.frame)
        self.label_3 = QtGui.QLabel(settingsDlg)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
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
        self.timeoutLbl.setText(_translate("settingsDlg", "Timeout (seconden):", None))
        self.dbHostLbl.setText(_translate("settingsDlg", "Database Host:", None))
        self.dbNameLbl.setText(_translate("settingsDlg", "Database Naam:", None))
        self.dbPortLbl.setText(_translate("settingsDlg", "Database Port:", None))
        self.dbPortEdit.setInputMask(_translate("settingsDlg", "0000; ", None))
        self.dbSchemaLbl.setText(_translate("settingsDlg", "Database Schema:", None))
        self.dbUserLbl.setText(_translate("settingsDlg", "Gebruiker:", None))
        self.dbPasswordLbl.setText(_translate("settingsDlg", "Password:", None))
        self.polygonTblLbl.setText(_translate("settingsDlg", "Polygoon tabel:", None))
        self.NameColLbl.setText(_translate("settingsDlg", "Kolom met namen:", None))
        self.geomColLbl.setText(_translate("settingsDlg", "Kolom met geometrien:", None))
        self.label_3.setText(_translate("settingsDlg", "<font color=\"red\">Herstarten om toe te passen</font>", None))

import resources_rc
