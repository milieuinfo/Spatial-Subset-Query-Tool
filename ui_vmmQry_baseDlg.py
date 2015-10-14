# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_vmmQry_baseDlg.ui'
#
# Created: Wed Oct 14 20:29:09 2015
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

class Ui_vmmQryDlg(object):
    def setupUi(self, vmmQryDlg):
        vmmQryDlg.setObjectName(_fromUtf8("vmmQryDlg"))
        vmmQryDlg.resize(574, 300)
        vmmQryDlg.setMinimumSize(QtCore.QSize(300, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/vmmQry/images/Sql-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        vmmQryDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(vmmQryDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(vmmQryDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.gemeenteCbx = QtGui.QComboBox(vmmQryDlg)
        self.gemeenteCbx.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.gemeenteCbx.setObjectName(_fromUtf8("gemeenteCbx"))
        self.horizontalLayout.addWidget(self.gemeenteCbx)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lyrList = QtGui.QListWidget(vmmQryDlg)
        self.lyrList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lyrList.setObjectName(_fromUtf8("lyrList"))
        self.verticalLayout.addWidget(self.lyrList)
        self.typeQryBox = QtGui.QGroupBox(vmmQryDlg)
        self.typeQryBox.setObjectName(_fromUtf8("typeQryBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.typeQryBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.bboxSelBtn = QtGui.QRadioButton(self.typeQryBox)
        self.bboxSelBtn.setChecked(True)
        self.bboxSelBtn.setObjectName(_fromUtf8("bboxSelBtn"))
        self.horizontalLayout_2.addWidget(self.bboxSelBtn)
        self.borderSelBtn = QtGui.QRadioButton(self.typeQryBox)
        self.borderSelBtn.setObjectName(_fromUtf8("borderSelBtn"))
        self.horizontalLayout_2.addWidget(self.borderSelBtn)
        self.verticalLayout.addWidget(self.typeQryBox)
        self.addLayerBtn = QtGui.QPushButton(vmmQryDlg)
        self.addLayerBtn.setObjectName(_fromUtf8("addLayerBtn"))
        self.verticalLayout.addWidget(self.addLayerBtn)
        self.button_box = QtGui.QDialogButtonBox(vmmQryDlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(vmmQryDlg)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), vmmQryDlg.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), vmmQryDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(vmmQryDlg)

    def retranslateUi(self, vmmQryDlg):
        vmmQryDlg.setWindowTitle(_translate("vmmQryDlg", "Spatial Subset Query Tool", None))
        self.label.setText(_translate("vmmQryDlg", "Selecteer gegevens in:", None))
        self.lyrList.setSortingEnabled(True)
        self.typeQryBox.setTitle(_translate("vmmQryDlg", "Type Van Selectie", None))
        self.bboxSelBtn.setText(_translate("vmmQryDlg", "Rechthoek (sneller)", None))
        self.borderSelBtn.setText(_translate("vmmQryDlg", "Afsnijden langs grens", None))
        self.addLayerBtn.setText(_translate("vmmQryDlg", "Selecteerde lagen Toevoegen", None))

import resources_rc
