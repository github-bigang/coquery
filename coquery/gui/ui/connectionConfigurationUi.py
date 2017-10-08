# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectionConfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConnectionConfig(object):
    def setupUi(self, ConnectionConfig):
        ConnectionConfig.setObjectName("ConnectionConfig")
        ConnectionConfig.resize(614, 734)
        self.gridLayout_5 = QtWidgets.QGridLayout(ConnectionConfig)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.list_config = QtWidgets.QListWidget(ConnectionConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_config.sizePolicy().hasHeightForWidth())
        self.list_config.setSizePolicy(sizePolicy)
        self.list_config.setObjectName("list_config")
        self.gridLayout_3.addWidget(self.list_config, 0, 0, 1, 2)
        self.button_add = QtWidgets.QPushButton(ConnectionConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        self.button_add.setObjectName("button_add")
        self.gridLayout_3.addWidget(self.button_add, 1, 0, 1, 1)
        self.button_remove = QtWidgets.QPushButton(ConnectionConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_remove.sizePolicy().hasHeightForWidth())
        self.button_remove.setSizePolicy(sizePolicy)
        self.button_remove.setObjectName("button_remove")
        self.gridLayout_3.addWidget(self.button_remove, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 4, 1)
        self.group_general = QtWidgets.QGroupBox(ConnectionConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_general.sizePolicy().hasHeightForWidth())
        self.group_general.setSizePolicy(sizePolicy)
        self.group_general.setObjectName("group_general")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.group_general)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.group_general)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.connection_name = QtWidgets.QLineEdit(self.group_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection_name.sizePolicy().hasHeightForWidth())
        self.connection_name.setSizePolicy(sizePolicy)
        self.connection_name.setObjectName("connection_name")
        self.horizontalLayout_2.addWidget(self.connection_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.layout_toggle_mysql = QtWidgets.QHBoxLayout()
        self.layout_toggle_mysql.setObjectName("layout_toggle_mysql")
        self.label_mysql_server = QtWidgets.QLabel(self.group_general)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mysql_server.sizePolicy().hasHeightForWidth())
        self.label_mysql_server.setSizePolicy(sizePolicy)
        self.label_mysql_server.setObjectName("label_mysql_server")
        self.layout_toggle_mysql.addWidget(self.label_mysql_server)
        self.radio_sqlite = QtWidgets.QRadioButton(self.group_general)
        self.radio_sqlite.setChecked(True)
        self.radio_sqlite.setObjectName("radio_sqlite")
        self.layout_toggle_mysql.addWidget(self.radio_sqlite)
        self.radio_mysql = QtWidgets.QRadioButton(self.group_general)
        self.radio_mysql.setObjectName("radio_mysql")
        self.layout_toggle_mysql.addWidget(self.radio_mysql)
        self.verticalLayout_3.addLayout(self.layout_toggle_mysql)
        self.gridLayout_5.addWidget(self.group_general, 0, 1, 1, 1)
        self.frame_mysql = QtWidgets.QWidget(ConnectionConfig)
        self.frame_mysql.setObjectName("frame_mysql")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_mysql)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_mysql)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radio_local = QtWidgets.QRadioButton(self.groupBox)
        self.radio_local.setChecked(True)
        self.radio_local.setObjectName("radio_local")
        self.gridLayout_2.addWidget(self.radio_local, 0, 0, 1, 2)
        self.radio_remote = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_remote.sizePolicy().hasHeightForWidth())
        self.radio_remote.setSizePolicy(sizePolicy)
        self.radio_remote.setObjectName("radio_remote")
        self.gridLayout_2.addWidget(self.radio_remote, 1, 0, 1, 1)
        self.hostname = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hostname.sizePolicy().hasHeightForWidth())
        self.hostname.setSizePolicy(sizePolicy)
        self.hostname.setInputMask("")
        self.hostname.setText("")
        self.hostname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.hostname.setObjectName("hostname")
        self.gridLayout_2.addWidget(self.hostname, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.port = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port.sizePolicy().hasHeightForWidth())
        self.port.setSizePolicy(sizePolicy)
        self.port.setMinimum(1)
        self.port.setMaximum(65535)
        self.port.setProperty("value", 3306)
        self.port.setObjectName("port")
        self.horizontalLayout_3.addWidget(self.port)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.group_credentials = QtWidgets.QGroupBox(self.frame_mysql)
        self.group_credentials.setObjectName("group_credentials")
        self.gridLayout = QtWidgets.QGridLayout(self.group_credentials)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.group_credentials)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.user = QtWidgets.QLineEdit(self.group_credentials)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 0, 1, 1, 1)
        self.button_create_user = QtWidgets.QPushButton(self.group_credentials)
        self.button_create_user.setObjectName("button_create_user")
        self.gridLayout.addWidget(self.button_create_user, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.group_credentials)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.group_credentials)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.group_credentials)
        self.connection_indicator = QtWidgets.QFrame(self.frame_mysql)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection_indicator.sizePolicy().hasHeightForWidth())
        self.connection_indicator.setSizePolicy(sizePolicy)
        self.connection_indicator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connection_indicator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.connection_indicator.setObjectName("connection_indicator")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.connection_indicator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.connection_indicator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.button_status = QtWidgets.QPushButton(self.connection_indicator)
        self.button_status.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_status.sizePolicy().hasHeightForWidth())
        self.button_status.setSizePolicy(sizePolicy)
        self.button_status.setText("")
        self.button_status.setAutoDefault(False)
        self.button_status.setFlat(False)
        self.button_status.setObjectName("button_status")
        self.horizontalLayout.addWidget(self.button_status)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.connection_indicator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 330, 93))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_connection = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_connection.sizePolicy().hasHeightForWidth())
        self.label_connection.setSizePolicy(sizePolicy)
        self.label_connection.setText("")
        self.label_connection.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_connection.setWordWrap(True)
        self.label_connection.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_connection.setObjectName("label_connection")
        self.verticalLayout_8.addWidget(self.label_connection)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.connection_indicator)
        self.gridLayout_5.addWidget(self.frame_mysql, 1, 1, 1, 1)
        self.frame_sqlite = QtWidgets.QGroupBox(ConnectionConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_sqlite.sizePolicy().hasHeightForWidth())
        self.frame_sqlite.setSizePolicy(sizePolicy)
        self.frame_sqlite.setObjectName("frame_sqlite")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_sqlite)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input_db_path = QtWidgets.QLineEdit(self.frame_sqlite)
        self.input_db_path.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_db_path.sizePolicy().hasHeightForWidth())
        self.input_db_path.setSizePolicy(sizePolicy)
        self.input_db_path.setPlaceholderText("")
        self.input_db_path.setObjectName("input_db_path")
        self.horizontalLayout_4.addWidget(self.input_db_path)
        self.button_db_path = QtWidgets.QPushButton(self.frame_sqlite)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_db_path.sizePolicy().hasHeightForWidth())
        self.button_db_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("folder")
        self.button_db_path.setIcon(icon)
        self.button_db_path.setObjectName("button_db_path")
        self.horizontalLayout_4.addWidget(self.button_db_path)
        self.gridLayout_5.addWidget(self.frame_sqlite, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(18, 54, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConnectionConfig)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_5.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.group_general.raise_()
        self.buttonBox.raise_()
        self.frame_mysql.raise_()
        self.frame_sqlite.raise_()
        self.label_3.setBuddy(self.connection_name)
        self.label_4.setBuddy(self.port)
        self.label.setBuddy(self.user)
        self.label_2.setBuddy(self.password)

        self.retranslateUi(ConnectionConfig)
        self.buttonBox.accepted.connect(ConnectionConfig.accept)
        self.buttonBox.rejected.connect(ConnectionConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionConfig)
        ConnectionConfig.setTabOrder(self.button_add, self.button_remove)
        ConnectionConfig.setTabOrder(self.button_remove, self.buttonBox)
        ConnectionConfig.setTabOrder(self.buttonBox, self.list_config)

    def retranslateUi(self, ConnectionConfig):
        _translate = QtCore.QCoreApplication.translate
        ConnectionConfig.setWindowTitle(_translate("ConnectionConfig", "Database connections – Coquery"))
        self.button_add.setText(_translate("ConnectionConfig", "A&dd"))
        self.button_remove.setText(_translate("ConnectionConfig", "Re&move"))
        self.group_general.setTitle(_translate("ConnectionConfig", "General settings"))
        self.label_3.setText(_translate("ConnectionConfig", "Connection &name:"))
        self.connection_name.setText(_translate("ConnectionConfig", "Default"))
        self.connection_name.setPlaceholderText(_translate("ConnectionConfig", "(untitled)"))
        self.label_mysql_server.setText(_translate("ConnectionConfig", "Use MySQL server:"))
        self.radio_sqlite.setText(_translate("ConnectionConfig", "&No"))
        self.radio_mysql.setText(_translate("ConnectionConfig", "&Yes"))
        self.groupBox.setTitle(_translate("ConnectionConfig", "Server location"))
        self.radio_local.setText(_translate("ConnectionConfig", "&Local server on this computer"))
        self.radio_remote.setText(_translate("ConnectionConfig", "URL or IP address:"))
        self.hostname.setPlaceholderText(_translate("ConnectionConfig", "(URL or IP address)"))
        self.label_4.setText(_translate("ConnectionConfig", "&Port number:"))
        self.group_credentials.setTitle(_translate("ConnectionConfig", "User credentials"))
        self.label.setText(_translate("ConnectionConfig", "&User name:"))
        self.user.setText(_translate("ConnectionConfig", "coquery"))
        self.button_create_user.setText(_translate("ConnectionConfig", "&Create user"))
        self.label_2.setText(_translate("ConnectionConfig", "Pass&word:"))
        self.password.setText(_translate("ConnectionConfig", "coquery"))
        self.label_6.setText(_translate("ConnectionConfig", "Connection status:"))
        self.frame_sqlite.setTitle(_translate("ConnectionConfig", "&Database directory:"))
        self.button_db_path.setText(_translate("ConnectionConfig", "&Browse"))
        self.button_db_path.setShortcut(_translate("ConnectionConfig", "Alt+B"))


