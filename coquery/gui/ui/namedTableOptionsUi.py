# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'namedTableOptions.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NamedTableOptions(object):
    def setupUi(self, NamedTableOptions):
        NamedTableOptions.setObjectName("NamedTableOptions")
        NamedTableOptions.resize(640, 480)
        NamedTableOptions.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NamedTableOptions)
        self.verticalLayout_2.setContentsMargins(4, -1, 4, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(NamedTableOptions)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.edit_file_name = QtWidgets.QLineEdit(NamedTableOptions)
        self.edit_file_name.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_file_name.sizePolicy().hasHeightForWidth())
        self.edit_file_name.setSizePolicy(sizePolicy)
        self.edit_file_name.setAccessibleDescription("")
        self.edit_file_name.setObjectName("edit_file_name")
        self.horizontalLayout_3.addWidget(self.edit_file_name)
        self.button_browse_file = QtWidgets.QPushButton(NamedTableOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browse_file.sizePolicy().hasHeightForWidth())
        self.button_browse_file.setSizePolicy(sizePolicy)
        self.button_browse_file.setObjectName("button_browse_file")
        self.horizontalLayout_3.addWidget(self.button_browse_file)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.OptionsBox = QtWidgets.QGroupBox(NamedTableOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionsBox.sizePolicy().hasHeightForWidth())
        self.OptionsBox.setSizePolicy(sizePolicy)
        self.OptionsBox.setObjectName("OptionsBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.OptionsBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_query_column = QtWidgets.QLabel(self.OptionsBox)
        self.label_query_column.setObjectName("label_query_column")
        self.gridLayout.addWidget(self.label_query_column, 1, 0, 1, 1)
        self.ignore_lines = QtWidgets.QSpinBox(self.OptionsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_lines.sizePolicy().hasHeightForWidth())
        self.ignore_lines.setSizePolicy(sizePolicy)
        self.ignore_lines.setObjectName("ignore_lines")
        self.gridLayout.addWidget(self.ignore_lines, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.OptionsBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.quote_char = QtWidgets.QComboBox(self.OptionsBox)
        self.quote_char.setObjectName("quote_char")
        self.gridLayout.addWidget(self.quote_char, 5, 1, 1, 1)
        self.query_column = QtWidgets.QSpinBox(self.OptionsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_column.sizePolicy().hasHeightForWidth())
        self.query_column.setSizePolicy(sizePolicy)
        self.query_column.setMinimum(1)
        self.query_column.setMaximum(999)
        self.query_column.setObjectName("query_column")
        self.gridLayout.addWidget(self.query_column, 1, 1, 1, 1)
        self.separate_char = QtWidgets.QComboBox(self.OptionsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.separate_char.sizePolicy().hasHeightForWidth())
        self.separate_char.setSizePolicy(sizePolicy)
        self.separate_char.setEditable(True)
        self.separate_char.setObjectName("separate_char")
        self.separate_char.addItem("")
        self.separate_char.addItem("")
        self.separate_char.addItem("")
        self.separate_char.addItem("")
        self.separate_char.addItem("")
        self.separate_char.addItem("")
        self.gridLayout.addWidget(self.separate_char, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.OptionsBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.OptionsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.file_has_headers = QtWidgets.QCheckBox(self.OptionsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_has_headers.sizePolicy().hasHeightForWidth())
        self.file_has_headers.setSizePolicy(sizePolicy)
        self.file_has_headers.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.file_has_headers.setText("")
        self.file_has_headers.setObjectName("file_has_headers")
        self.gridLayout.addWidget(self.file_has_headers, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.OptionsBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.OptionsBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.combo_encoding = QtWidgets.QComboBox(self.OptionsBox)
        self.combo_encoding.setObjectName("combo_encoding")
        self.gridLayout.addWidget(self.combo_encoding, 6, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.OptionsBox)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(NamedTableOptions)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_name_buttons = QtWidgets.QGridLayout()
        self.layout_name_buttons.setObjectName("layout_name_buttons")
        self.button_word = QtWidgets.QPushButton(self.groupBox)
        self.button_word.setObjectName("button_word")
        self.layout_name_buttons.addWidget(self.button_word, 0, 0, 1, 1)
        self.edit_word = QtWidgets.QLineEdit(self.groupBox)
        self.edit_word.setReadOnly(True)
        self.edit_word.setObjectName("edit_word")
        self.layout_name_buttons.addWidget(self.edit_word, 0, 1, 1, 1)
        self.button_lemma = QtWidgets.QPushButton(self.groupBox)
        self.button_lemma.setObjectName("button_lemma")
        self.layout_name_buttons.addWidget(self.button_lemma, 1, 0, 1, 1)
        self.edit_lemma = QtWidgets.QLineEdit(self.groupBox)
        self.edit_lemma.setReadOnly(True)
        self.edit_lemma.setObjectName("edit_lemma")
        self.layout_name_buttons.addWidget(self.edit_lemma, 1, 1, 1, 1)
        self.button_pos = QtWidgets.QPushButton(self.groupBox)
        self.button_pos.setObjectName("button_pos")
        self.layout_name_buttons.addWidget(self.button_pos, 2, 0, 1, 1)
        self.edit_pos = QtWidgets.QLineEdit(self.groupBox)
        self.edit_pos.setReadOnly(True)
        self.edit_pos.setObjectName("edit_pos")
        self.layout_name_buttons.addWidget(self.edit_pos, 2, 1, 1, 1)
        self.edit_transcript = QtWidgets.QLineEdit(self.groupBox)
        self.edit_transcript.setReadOnly(True)
        self.edit_transcript.setObjectName("edit_transcript")
        self.layout_name_buttons.addWidget(self.edit_transcript, 3, 1, 1, 1)
        self.edit_gloss = QtWidgets.QLineEdit(self.groupBox)
        self.edit_gloss.setReadOnly(True)
        self.edit_gloss.setObjectName("edit_gloss")
        self.layout_name_buttons.addWidget(self.edit_gloss, 4, 1, 1, 1)
        self.button_transcript = QtWidgets.QPushButton(self.groupBox)
        self.button_transcript.setObjectName("button_transcript")
        self.layout_name_buttons.addWidget(self.button_transcript, 3, 0, 1, 1)
        self.button_gloss = QtWidgets.QPushButton(self.groupBox)
        self.button_gloss.setObjectName("button_gloss")
        self.layout_name_buttons.addWidget(self.button_gloss, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.layout_name_buttons)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.FilePreviewArea = QtWidgets.QTableView(NamedTableOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilePreviewArea.sizePolicy().hasHeightForWidth())
        self.FilePreviewArea.setSizePolicy(sizePolicy)
        self.FilePreviewArea.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.FilePreviewArea.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.FilePreviewArea.setAlternatingRowColors(True)
        self.FilePreviewArea.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.FilePreviewArea.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.FilePreviewArea.setObjectName("FilePreviewArea")
        self.verticalLayout_2.addWidget(self.FilePreviewArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(NamedTableOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_2.setStretch(2, 1)
        self.label_4.setBuddy(self.edit_file_name)
        self.label_query_column.setBuddy(self.query_column)
        self.label_6.setBuddy(self.ignore_lines)
        self.label.setBuddy(self.file_has_headers)
        self.label_10.setBuddy(self.separate_char)
        self.label_2.setBuddy(self.quote_char)
        self.label_3.setBuddy(self.combo_encoding)

        self.retranslateUi(NamedTableOptions)
        self.buttonBox.accepted.connect(NamedTableOptions.accept)
        self.buttonBox.rejected.connect(NamedTableOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(NamedTableOptions)

    def retranslateUi(self, NamedTableOptions):
        _translate = QtCore.QCoreApplication.translate
        NamedTableOptions.setWindowTitle(_translate("NamedTableOptions", "Table options ~ Coquery"))
        self.label_4.setText(_translate("NamedTableOptions", "File na&me:"))
        self.edit_file_name.setPlaceholderText(_translate("NamedTableOptions", "Input file name"))
        self.button_browse_file.setText(_translate("NamedTableOptions", "&Browse"))
        self.button_browse_file.setShortcut(_translate("NamedTableOptions", "Alt+B"))
        self.OptionsBox.setTitle(_translate("NamedTableOptions", "CSV Options"))
        self.label_query_column.setText(_translate("NamedTableOptions", "&Read queries from column number:"))
        self.label_6.setText(_translate("NamedTableOptions", "&Text lines to ignore after header:"))
        self.separate_char.setItemText(0, _translate("NamedTableOptions", ","))
        self.separate_char.setItemText(1, _translate("NamedTableOptions", ";"))
        self.separate_char.setItemText(2, _translate("NamedTableOptions", ":"))
        self.separate_char.setItemText(3, _translate("NamedTableOptions", "#"))
        self.separate_char.setItemText(4, _translate("NamedTableOptions", "{tab}"))
        self.separate_char.setItemText(5, _translate("NamedTableOptions", "{space}"))
        self.label.setText(_translate("NamedTableOptions", "Fi&le contains header:"))
        self.label_10.setText(_translate("NamedTableOptions", "&Character that separates columns:"))
        self.label_2.setText(_translate("NamedTableOptions", "&Quote character:"))
        self.label_3.setText(_translate("NamedTableOptions", "Character &encoding:"))
        self.groupBox.setTitle(_translate("NamedTableOptions", "Query type mappings"))
        self.button_word.setText(_translate("NamedTableOptions", "Word"))
        self.button_lemma.setText(_translate("NamedTableOptions", "Lemma"))
        self.button_pos.setText(_translate("NamedTableOptions", "POS"))
        self.button_transcript.setText(_translate("NamedTableOptions", "Transcript"))
        self.button_gloss.setText(_translate("NamedTableOptions", "Gloss"))


