# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview_page.ui'
#
# Created: Tue Jul 17 01:01:13 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_previewPage(object):
    def setupUi(self, previewPage):
        previewPage.setObjectName("previewPage")
        previewPage.resize(746, 525)
        self.horizontalLayout = QtGui.QHBoxLayout(previewPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputFilesList = QtGui.QListWidget(previewPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFilesList.sizePolicy().hasHeightForWidth())
        self.outputFilesList.setSizePolicy(sizePolicy)
        self.outputFilesList.setObjectName("outputFilesList")
        self.horizontalLayout.addWidget(self.outputFilesList)
        self.previewText = QtGui.QTextBrowser(previewPage)
        self.previewText.setObjectName("previewText")
        self.horizontalLayout.addWidget(self.previewText)

        self.retranslateUi(previewPage)
        QtCore.QMetaObject.connectSlotsByName(previewPage)

    def retranslateUi(self, previewPage):
        previewPage.setWindowTitle(QtGui.QApplication.translate("previewPage", "Form", None, QtGui.QApplication.UnicodeUTF8))

