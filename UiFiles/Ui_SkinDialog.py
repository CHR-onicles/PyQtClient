# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Workspace\PyQtClient\UiFiles\SkinDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormSkinDialog(object):
    def setupUi(self, FormSkinDialog):
        FormSkinDialog.setObjectName("FormSkinDialog")
        FormSkinDialog.resize(930, 635)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormSkinDialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetSkin = QtWidgets.QWidget(FormSkinDialog)
        self.widgetSkin.setProperty("active", True)
        self.widgetSkin.setObjectName("widgetSkin")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widgetSkin)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dialogTitlebar = QtWidgets.QWidget(self.widgetSkin)
        self.dialogTitlebar.setObjectName("dialogTitlebar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dialogTitlebar)
        self.horizontalLayout.setContentsMargins(0, 1, 1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelTitle = QtWidgets.QLabel(self.dialogTitlebar)
        self.labelTitle.setIndent(6)
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout.addWidget(self.labelTitle)
        spacerItem = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonClose = QtWidgets.QPushButton(self.dialogTitlebar)
        self.buttonClose.setText("")
        self.buttonClose.setAutoDefault(False)
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)
        self.verticalLayout_2.addWidget(self.dialogTitlebar)
        self.tabWidget = QtWidgets.QTabWidget(self.widgetSkin)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTheme = ThemeWidget()
        self.tabTheme.setObjectName("tabTheme")
        self.tabWidget.addTab(self.tabTheme, "")
        self.tabColourful = ColourfulWidget()
        self.tabColourful.setObjectName("tabColourful")
        self.tabWidget.addTab(self.tabColourful, "")
        self.tabPicture = PictureWidget()
        self.tabPicture.setObjectName("tabPicture")
        self.tabWidget.addTab(self.tabPicture, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.widgetBottom = QtWidgets.QWidget(self.widgetSkin)
        self.widgetBottom.setObjectName("widgetBottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetBottom)
        self.horizontalLayout_2.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_2.setSpacing(14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widgetBottom)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.sliderOpacity = QtWidgets.QSlider(self.widgetBottom)
        self.sliderOpacity.setOrientation(QtCore.Qt.Horizontal)
        self.sliderOpacity.setObjectName("sliderOpacity")
        self.horizontalLayout_2.addWidget(self.sliderOpacity)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonRestore = QtWidgets.QPushButton(self.widgetBottom)
        self.buttonRestore.setAutoDefault(False)
        self.buttonRestore.setObjectName("buttonRestore")
        self.horizontalLayout_2.addWidget(self.buttonRestore)
        self.verticalLayout_2.addWidget(self.widgetBottom)
        self.verticalLayout.addWidget(self.widgetSkin)

        self.retranslateUi(FormSkinDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonClose.clicked.connect(FormSkinDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FormSkinDialog)

    def retranslateUi(self, FormSkinDialog):
        _translate = QtCore.QCoreApplication.translate
        FormSkinDialog.setWindowTitle(_translate("FormSkinDialog", "Skin"))
        self.labelTitle.setText(_translate("FormSkinDialog", "Skin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTheme), _translate("FormSkinDialog", "Theme"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabColourful), _translate("FormSkinDialog", "Colourful"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPicture), _translate("FormSkinDialog", "Picture"))
        self.label.setText(_translate("FormSkinDialog", "Transparency"))
        self.buttonRestore.setText(_translate("FormSkinDialog", "Restore the default theme"))

from Widgets.Skins.ColourfulWidget import ColourfulWidget
from Widgets.Skins.PictureWidget import PictureWidget
from Widgets.Skins.ThemeWidget import ThemeWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSkinDialog = QtWidgets.QDialog()
    ui = Ui_FormSkinDialog()
    ui.setupUi(FormSkinDialog)
    FormSkinDialog.show()
    sys.exit(app.exec_())

