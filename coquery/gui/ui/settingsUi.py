# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from coquery.gui.pyqt_compat import QtCore, QtGui, frameShadow, frameShape

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

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setContentsMargins(4, -1, 4, -1)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.group_case = QtGui.QGroupBox(self.tab_2)
        self.group_case.setObjectName(_fromUtf8("group_case"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.group_case)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radio_output_case_leave = QtGui.QRadioButton(self.group_case)
        self.radio_output_case_leave.setObjectName(_fromUtf8("radio_output_case_leave"))
        self.verticalLayout_4.addWidget(self.radio_output_case_leave)
        self.radio_output_case_lower = QtGui.QRadioButton(self.group_case)
        self.radio_output_case_lower.setObjectName(_fromUtf8("radio_output_case_lower"))
        self.verticalLayout_4.addWidget(self.radio_output_case_lower)
        self.radio_output_case_upper = QtGui.QRadioButton(self.group_case)
        self.radio_output_case_upper.setObjectName(_fromUtf8("radio_output_case_upper"))
        self.verticalLayout_4.addWidget(self.radio_output_case_upper)
        self.verticalLayout.addWidget(self.group_case)
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.spin_digits = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_digits.sizePolicy().hasHeightForWidth())
        self.spin_digits.setSizePolicy(sizePolicy)
        self.spin_digits.setProperty("value", 3)
        self.spin_digits.setObjectName(_fromUtf8("spin_digits"))
        self.horizontalLayout.addWidget(self.spin_digits)
        self.label_7 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_7.addWidget(self.label_13)
        self.edit_na_string = QtGui.QLineEdit(self.groupBox)
        self.edit_na_string.setObjectName(_fromUtf8("edit_na_string"))
        self.horizontalLayout_7.addWidget(self.edit_na_string)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.check_word_wrap = QtGui.QCheckBox(self.groupBox)
        self.check_word_wrap.setObjectName(_fromUtf8("check_word_wrap"))
        self.verticalLayout_7.addWidget(self.check_word_wrap)
        self.verticalLayout.addWidget(self.groupBox)
        self.check_align_quantified = QtGui.QCheckBox(self.tab_2)
        self.check_align_quantified.setObjectName(_fromUtf8("check_align_quantified"))
        self.verticalLayout.addWidget(self.check_align_quantified)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.Queries = QtGui.QWidget()
        self.Queries.setObjectName(_fromUtf8("Queries"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Queries)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.check_ignore_case_query = QtGui.QCheckBox(self.Queries)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_ignore_case_query.sizePolicy().hasHeightForWidth())
        self.check_ignore_case_query.setSizePolicy(sizePolicy)
        self.check_ignore_case_query.setText(_fromUtf8(""))
        self.check_ignore_case_query.setObjectName(_fromUtf8("check_ignore_case_query"))
        self.horizontalLayout_3.addWidget(self.check_ignore_case_query)
        self.label_2 = QtGui.QLabel(self.Queries)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.check_drop_empty_queries = QtGui.QCheckBox(self.Queries)
        self.check_drop_empty_queries.setText(_fromUtf8(""))
        self.check_drop_empty_queries.setObjectName(_fromUtf8("check_drop_empty_queries"))
        self.horizontalLayout_6.addWidget(self.check_drop_empty_queries)
        self.label_12 = QtGui.QLabel(self.Queries)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.check_limit_tokens = QtGui.QCheckBox(self.Queries)
        self.check_limit_tokens.setText(_fromUtf8(""))
        self.check_limit_tokens.setObjectName(_fromUtf8("check_limit_tokens"))
        self.horizontalLayout_2.addWidget(self.check_limit_tokens)
        self.label = QtGui.QLabel(self.Queries)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.spin_maximum_tokens = QtGui.QSpinBox(self.Queries)
        self.spin_maximum_tokens.setMinimum(1)
        self.spin_maximum_tokens.setMaximum(999999999)
        self.spin_maximum_tokens.setObjectName(_fromUtf8("spin_maximum_tokens"))
        self.horizontalLayout_2.addWidget(self.spin_maximum_tokens)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.Queries)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.widget_cache = QtGui.QWidget(self.Queries)
        self.widget_cache.setObjectName(_fromUtf8("widget_cache"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_cache)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.check_use_cache = QtGui.QCheckBox(self.widget_cache)
        self.check_use_cache.setObjectName(_fromUtf8("check_use_cache"))
        self.horizontalLayout_4.addWidget(self.check_use_cache)
        self.spin_cache_size = QtGui.QSpinBox(self.widget_cache)
        self.spin_cache_size.setPrefix(_fromUtf8(""))
        self.spin_cache_size.setMinimum(1)
        self.spin_cache_size.setMaximum(4096)
        self.spin_cache_size.setObjectName(_fromUtf8("spin_cache_size"))
        self.horizontalLayout_4.addWidget(self.spin_cache_size)
        self.widget_used = QtGui.QWidget(self.widget_cache)
        self.widget_used.setObjectName(_fromUtf8("widget_used"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_used)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_10 = QtGui.QLabel(self.widget_used)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.progress_used = QtGui.QProgressBar(self.widget_used)
        self.progress_used.setProperty("value", 24)
        self.progress_used.setObjectName(_fromUtf8("progress_used"))
        self.horizontalLayout_5.addWidget(self.progress_used)
        self.horizontalLayout_4.addWidget(self.widget_used)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.button_clear_cache = QtGui.QPushButton(self.widget_cache)
        self.button_clear_cache.setObjectName(_fromUtf8("button_clear_cache"))
        self.horizontalLayout_4.addWidget(self.button_clear_cache)
        self.verticalLayout_2.addWidget(self.widget_cache)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.tabWidget.addTab(self.Queries, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_sample_context = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_context.sizePolicy().hasHeightForWidth())
        self.label_sample_context.setSizePolicy(sizePolicy)
        self.label_sample_context.setFrameShape(frameShape)
        self.label_sample_context.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sample_context.setObjectName(_fromUtf8("label_sample_context"))
        self.gridLayout.addWidget(self.label_sample_context, 1, 1, 1, 1)
        self.button_figure_font = QtGui.QPushButton(self.tab)
        self.button_figure_font.setObjectName(_fromUtf8("button_figure_font"))
        self.gridLayout.addWidget(self.button_figure_font, 2, 2, 1, 1)
        self.button_reset_table = QtGui.QPushButton(self.tab)
        self.button_reset_table.setObjectName(_fromUtf8("button_reset_table"))
        self.gridLayout.addWidget(self.button_reset_table, 0, 3, 1, 1)
        self.button_reset_context = QtGui.QPushButton(self.tab)
        self.button_reset_context.setObjectName(_fromUtf8("button_reset_context"))
        self.gridLayout.addWidget(self.button_reset_context, 1, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.button_context_font = QtGui.QPushButton(self.tab)
        self.button_context_font.setObjectName(_fromUtf8("button_context_font"))
        self.gridLayout.addWidget(self.button_context_font, 1, 2, 1, 1)
        self.button_reset_figure = QtGui.QPushButton(self.tab)
        self.button_reset_figure.setObjectName(_fromUtf8("button_reset_figure"))
        self.gridLayout.addWidget(self.button_reset_figure, 2, 3, 1, 1)
        self.label_sample_table = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_table.sizePolicy().hasHeightForWidth())
        self.label_sample_table.setSizePolicy(sizePolicy)
        self.label_sample_table.setFrameShape(frameShape)
        self.label_sample_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sample_table.setObjectName(_fromUtf8("label_sample_table"))
        self.gridLayout.addWidget(self.label_sample_table, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.button_table_font = QtGui.QPushButton(self.tab)
        self.button_table_font.setObjectName(_fromUtf8("button_table_font"))
        self.gridLayout.addWidget(self.button_table_font, 0, 2, 1, 1)
        self.label_sample_figure = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sample_figure.sizePolicy().hasHeightForWidth())
        self.label_sample_figure.setSizePolicy(sizePolicy)
        self.label_sample_figure.setFrameShape(frameShape)
        self.label_sample_figure.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sample_figure.setObjectName(_fromUtf8("label_sample_figure"))
        self.gridLayout.addWidget(self.label_sample_figure, 2, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.check_ask_on_quit = QtGui.QCheckBox(self.tab_3)
        self.check_ask_on_quit.setObjectName(_fromUtf8("check_ask_on_quit"))
        self.verticalLayout_5.addWidget(self.check_ask_on_quit)
        self.check_save_query_string = QtGui.QCheckBox(self.tab_3)
        self.check_save_query_string.setObjectName(_fromUtf8("check_save_query_string"))
        self.verticalLayout_5.addWidget(self.check_save_query_string)
        self.check_save_query_file = QtGui.QCheckBox(self.tab_3)
        self.check_save_query_file.setObjectName(_fromUtf8("check_save_query_file"))
        self.verticalLayout_5.addWidget(self.check_save_query_file)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.group_paths = QtGui.QGroupBox(self.tab_4)
        self.group_paths.setObjectName(_fromUtf8("group_paths"))
        self.gridLayout_2 = QtGui.QGridLayout(self.group_paths)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_8 = QtGui.QLabel(self.group_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.edit_installer_path = QtGui.QLineEdit(self.group_paths)
        self.edit_installer_path.setObjectName(_fromUtf8("edit_installer_path"))
        self.gridLayout_2.addWidget(self.edit_installer_path, 0, 1, 1, 1)
        self.button_installer_path = QtGui.QPushButton(self.group_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_installer_path.sizePolicy().hasHeightForWidth())
        self.button_installer_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder"))
        self.button_installer_path.setIcon(icon)
        self.button_installer_path.setObjectName(_fromUtf8("button_installer_path"))
        self.gridLayout_2.addWidget(self.button_installer_path, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.group_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.edit_visualizer_path = QtGui.QLineEdit(self.group_paths)
        self.edit_visualizer_path.setObjectName(_fromUtf8("edit_visualizer_path"))
        self.gridLayout_2.addWidget(self.edit_visualizer_path, 1, 1, 1, 1)
        self.button_visualizer_path = QtGui.QPushButton(self.group_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_visualizer_path.sizePolicy().hasHeightForWidth())
        self.button_visualizer_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder"))
        self.button_visualizer_path.setIcon(icon)
        self.button_visualizer_path.setObjectName(_fromUtf8("button_visualizer_path"))
        self.gridLayout_2.addWidget(self.button_visualizer_path, 1, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.group_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.edit_cache_path = QtGui.QLineEdit(self.group_paths)
        self.edit_cache_path.setObjectName(_fromUtf8("edit_cache_path"))
        self.gridLayout_2.addWidget(self.edit_cache_path, 2, 1, 1, 1)
        self.button_cache_path = QtGui.QPushButton(self.group_paths)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cache_path.sizePolicy().hasHeightForWidth())
        self.button_cache_path.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder"))
        self.button_cache_path.setIcon(icon)
        self.button_cache_path.setObjectName(_fromUtf8("button_cache_path"))
        self.gridLayout_2.addWidget(self.button_cache_path, 2, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.group_paths)
        spacerItem10 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.spin_digits)
        self.label_13.setBuddy(self.edit_na_string)
        self.label_2.setBuddy(self.check_ignore_case_query)
        self.label_12.setBuddy(self.check_drop_empty_queries)
        self.label.setBuddy(self.spin_maximum_tokens)
        self.label_8.setBuddy(self.edit_installer_path)
        self.label_9.setBuddy(self.edit_visualizer_path)
        self.label_11.setBuddy(self.edit_cache_path)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings – Coquery", None))
        self.group_case.setTitle(_translate("SettingsDialog", "Case", None))
        self.radio_output_case_leave.setText(_translate("SettingsDialog", "Do &not change case", None))
        self.radio_output_case_lower.setText(_translate("SettingsDialog", "&Lower case", None))
        self.radio_output_case_upper.setText(_translate("SettingsDialog", "&Upper case", None))
        self.groupBox.setTitle(_translate("SettingsDialog", "Display", None))
        self.label_3.setText(_translate("SettingsDialog", "&Display ", None))
        self.spin_digits.setSuffix(_translate("SettingsDialog", " digit(s)", None))
        self.label_7.setText(_translate("SettingsDialog", "after decimal point", None))
        self.label_13.setText(_translate("SettingsDialog", "&Placeholder for empty cells:", None))
        self.check_word_wrap.setText(_translate("SettingsDialog", " &Word-wrap long lines", None))
        self.check_align_quantified.setText(_translate("SettingsDialog", "Align &quantified token columns", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "Results table", None))
        self.label_2.setText(_translate("SettingsDialog", "&Ignore case in query strings", None))
        self.label_12.setText(_translate("SettingsDialog", "&Discard rows with only empty cells", None))
        self.label.setText(_translate("SettingsDialog", "Limit &maximum number of matches per query:", None))
        self.check_use_cache.setText(_translate("SettingsDialog", "Use query &cache, size: ", None))
        self.spin_cache_size.setSuffix(_translate("SettingsDialog", " MBytes", None))
        self.label_10.setText(_translate("SettingsDialog", "Used:", None))
        self.progress_used.setFormat(_translate("SettingsDialog", "%v MBytes", None))
        self.button_clear_cache.setText(_translate("SettingsDialog", "Clear cache", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Queries), _translate("SettingsDialog", "Queries", None))
        self.label_5.setText(_translate("SettingsDialog", "Context font:", None))
        self.label_sample_context.setText(_translate("SettingsDialog", "TextLabel", None))
        self.button_figure_font.setText(_translate("SettingsDialog", "Change...", None))
        self.button_reset_table.setText(_translate("SettingsDialog", "Reset", None))
        self.button_reset_context.setText(_translate("SettingsDialog", "Reset", None))
        self.label_6.setText(_translate("SettingsDialog", "Default figure font:", None))
        self.button_context_font.setText(_translate("SettingsDialog", "Change...", None))
        self.button_reset_figure.setText(_translate("SettingsDialog", "Reset", None))
        self.label_sample_table.setText(_translate("SettingsDialog", "TextLabel", None))
        self.label_4.setText(_translate("SettingsDialog", "Table font:", None))
        self.button_table_font.setText(_translate("SettingsDialog", "Change...", None))
        self.label_sample_figure.setText(_translate("SettingsDialog", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "Fonts", None))
        self.check_ask_on_quit.setText(_translate("SettingsDialog", "Ask if &unsaved results should be saved upon exit", None))
        self.check_save_query_string.setText(_translate("SettingsDialog", "Save last query &string in configuration file", None))
        self.check_save_query_file.setText(_translate("SettingsDialog", "Save last query &file in configuration file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingsDialog", "Quitting", None))
        self.group_paths.setTitle(_translate("SettingsDialog", "Additional paths", None))
        self.label_8.setText(_translate("SettingsDialog", "Corpus &installers: ", None))
        self.button_installer_path.setText(_translate("SettingsDialog", "&Browse", None))
        self.button_installer_path.setShortcut(_translate("SettingsDialog", "Alt+B", None))
        self.label_9.setText(_translate("SettingsDialog", "&Visualizers:", None))
        self.button_visualizer_path.setText(_translate("SettingsDialog", "B&rowse", None))
        self.button_visualizer_path.setShortcut(_translate("SettingsDialog", "Alt+B", None))
        self.label_11.setText(_translate("SettingsDialog", "Query &cache:", None))
        self.button_cache_path.setText(_translate("SettingsDialog", "B&rowse", None))
        self.button_cache_path.setShortcut(_translate("SettingsDialog", "Alt+B", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("SettingsDialog", "Paths", None))


