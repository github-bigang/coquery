# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mysqlConfiguration.ui'
#
# Created: Wed Nov 18 15:03:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from pyqt_compat import QtCore, QtGui, frameShadow

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

class Ui_MySQLConfig(object):
    def setupUi(self, MySQLConfig):
        MySQLConfig.setObjectName(_fromUtf8("MySQLConfig"))
        MySQLConfig.resize(640, 480)
        self.verticalLayout_5 = QtGui.QVBoxLayout(MySQLConfig)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(MySQLConfig)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tree_configuration = QtGui.QTreeWidget(MySQLConfig)
        self.tree_configuration.setRootIsDecorated(False)
        self.tree_configuration.setItemsExpandable(False)
        self.tree_configuration.setHeaderHidden(True)
        self.tree_configuration.setExpandsOnDoubleClick(False)
        self.tree_configuration.setObjectName(_fromUtf8("tree_configuration"))
        self.tree_configuration.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_4.addWidget(self.tree_configuration)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(8)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.button_add = QtGui.QPushButton(MySQLConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        self.button_add.setObjectName(_fromUtf8("button_add"))
        self.gridLayout_3.addWidget(self.button_add, 0, 0, 1, 1)
        self.button_replace = QtGui.QPushButton(MySQLConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_replace.sizePolicy().hasHeightForWidth())
        self.button_replace.setSizePolicy(sizePolicy)
        self.button_replace.setObjectName(_fromUtf8("button_replace"))
        self.gridLayout_3.addWidget(self.button_replace, 0, 1, 1, 1)
        self.button_remove = QtGui.QPushButton(MySQLConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_remove.sizePolicy().hasHeightForWidth())
        self.button_remove.setSizePolicy(sizePolicy)
        self.button_remove.setObjectName(_fromUtf8("button_remove"))
        self.gridLayout_3.addWidget(self.button_remove, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.frame_settings = QtGui.QFrame(MySQLConfig)
        self.frame_settings.setObjectName(_fromUtf8("frame_settings"))
        self.layout_settings = QtGui.QVBoxLayout(self.frame_settings)
        self.layout_settings.setSpacing(16)
        self.layout_settings.setMargin(0)
        self.layout_settings.setObjectName(_fromUtf8("layout_settings"))
        self.frame_2 = QtGui.QFrame(self.frame_settings)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(frameShadow)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(-1)
        self.verticalLayout_3.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.configuration_name = QtGui.QLineEdit(self.frame_2)
        self.configuration_name.setObjectName(_fromUtf8("configuration_name"))
        self.horizontalLayout_2.addWidget(self.configuration_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.radio_local = QtGui.QRadioButton(self.frame_2)
        self.radio_local.setChecked(True)
        self.radio_local.setObjectName(_fromUtf8("radio_local"))
        self.verticalLayout.addWidget(self.radio_local)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radio_remote = QtGui.QRadioButton(self.frame_2)
        self.radio_remote.setObjectName(_fromUtf8("radio_remote"))
        self.gridLayout_2.addWidget(self.radio_remote, 0, 0, 1, 1)
        self.hostname = QtGui.QLineEdit(self.frame_2)
        self.hostname.setInputMask(_fromUtf8(""))
        self.hostname.setText(_fromUtf8(""))
        self.hostname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.hostname.setObjectName(_fromUtf8("hostname"))
        self.gridLayout_2.addWidget(self.hostname, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.port = QtGui.QSpinBox(self.frame_2)
        self.port.setMinimum(1)
        self.port.setMaximum(65535)
        self.port.setProperty("value", 3306)
        self.port.setObjectName(_fromUtf8("port"))
        self.horizontalLayout_3.addWidget(self.port)
        spacerItem = QtGui.QSpacerItem(227, 35, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.layout_settings.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.frame_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(frameShadow)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setMargin(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_9 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.password = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.button_create_user = QtGui.QPushButton(self.frame)
        self.button_create_user.setObjectName(_fromUtf8("button_create_user"))
        self.gridLayout.addWidget(self.button_create_user, 0, 2, 1, 1)
        self.user = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy)
        self.user.setObjectName(_fromUtf8("user"))
        self.gridLayout.addWidget(self.user, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.layout_settings.addWidget(self.frame)
        self.connection_indicator = QtGui.QFrame(self.frame_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection_indicator.sizePolicy().hasHeightForWidth())
        self.connection_indicator.setSizePolicy(sizePolicy)
        self.connection_indicator.setFrameShape(QtGui.QFrame.StyledPanel)
        self.connection_indicator.setFrameShadow(QtGui.QFrame.Sunken)
        self.connection_indicator.setObjectName(_fromUtf8("connection_indicator"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.connection_indicator)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.connection_indicator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.button_status = QtGui.QPushButton(self.connection_indicator)
        self.button_status.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_status.sizePolicy().hasHeightForWidth())
        self.button_status.setSizePolicy(sizePolicy)
        self.button_status.setText(_fromUtf8(""))
        self.button_status.setAutoDefault(False)
        self.button_status.setFlat(False)
        self.button_status.setObjectName(_fromUtf8("button_status"))
        self.horizontalLayout.addWidget(self.button_status)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.scrollArea = QtGui.QScrollArea(self.connection_indicator)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 365, 76))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_connection = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_connection.sizePolicy().hasHeightForWidth())
        self.label_connection.setSizePolicy(sizePolicy)
        self.label_connection.setText(_fromUtf8(""))
        self.label_connection.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_connection.setWordWrap(True)
        self.label_connection.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_connection.setObjectName(_fromUtf8("label_connection"))
        self.verticalLayout_8.addWidget(self.label_connection)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.layout_settings.addWidget(self.connection_indicator)
        self.horizontalLayout_5.addWidget(self.frame_settings)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.buttonBox = QtGui.QDialogButtonBox(MySQLConfig)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_5.addWidget(self.buttonBox)
        self.label_5.setBuddy(self.tree_configuration)
        self.label_3.setBuddy(self.configuration_name)
        self.label_4.setBuddy(self.port)
        self.label.setBuddy(self.user)
        self.label_2.setBuddy(self.password)

        self.retranslateUi(MySQLConfig)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MySQLConfig.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MySQLConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(MySQLConfig)
        MySQLConfig.setTabOrder(self.configuration_name, self.radio_local)
        MySQLConfig.setTabOrder(self.radio_local, self.radio_remote)
        MySQLConfig.setTabOrder(self.radio_remote, self.hostname)
        MySQLConfig.setTabOrder(self.hostname, self.port)
        MySQLConfig.setTabOrder(self.port, self.user)
        MySQLConfig.setTabOrder(self.user, self.password)
        MySQLConfig.setTabOrder(self.password, self.button_create_user)
        MySQLConfig.setTabOrder(self.button_create_user, self.button_add)
        MySQLConfig.setTabOrder(self.button_add, self.button_replace)
        MySQLConfig.setTabOrder(self.button_replace, self.button_remove)
        MySQLConfig.setTabOrder(self.button_remove, self.buttonBox)
        MySQLConfig.setTabOrder(self.buttonBox, self.tree_configuration)
        MySQLConfig.setTabOrder(self.tree_configuration, self.button_status)
        MySQLConfig.setTabOrder(self.button_status, self.scrollArea)

    def retranslateUi(self, MySQLConfig):
        MySQLConfig.setWindowTitle(_translate("MySQLConfig", "MySQL configuration – Coquery", None))
        self.label_5.setText(_translate("MySQLConfig", "&Available configurations:", None))
        self.button_add.setText(_translate("MySQLConfig", "A&dd", None))
        self.button_replace.setText(_translate("MySQLConfig", "Replace", None))
        self.button_remove.setText(_translate("MySQLConfig", "Re&move", None))
        self.label_3.setText(_translate("MySQLConfig", "Configuration &name:", None))
        self.configuration_name.setText(_translate("MySQLConfig", "Default", None))
        self.label_8.setText(_translate("MySQLConfig", "Location of the MySQL database server:", None))
        self.radio_local.setText(_translate("MySQLConfig", "&Local server on this computer", None))
        self.radio_remote.setText(_translate("MySQLConfig", "&Remote host on the network:", None))
        self.hostname.setPlaceholderText(_translate("MySQLConfig", "(URL or IP address)", None))
        self.label_4.setText(_translate("MySQLConfig", "&Port number:", None))
        self.label_9.setText(_translate("MySQLConfig", "MySQL server credentials:", None))
        self.password.setText(_translate("MySQLConfig", "coquery", None))
        self.label.setText(_translate("MySQLConfig", "&User name:", None))
        self.button_create_user.setText(_translate("MySQLConfig", "&Create user", None))
        self.user.setText(_translate("MySQLConfig", "coquery", None))
        self.label_2.setText(_translate("MySQLConfig", "Pass&word:", None))
        self.label_6.setText(_translate("MySQLConfig", "Connection status:", None))


