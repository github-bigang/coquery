# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coquery.ui'
#
# Created by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from pyqt_compat import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(871, 671)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.options_area = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.options_area.sizePolicy().hasHeightForWidth())
        self.options_area.setSizePolicy(sizePolicy)
        self.options_area.setFrameShape(QtGui.QFrame.NoFrame)
        self.options_area.setFrameShadow(QtGui.QFrame.Raised)
        self.options_area.setObjectName(_fromUtf8("options_area"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.options_area)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setContentsMargins(4, 4, 4, 10)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.general_settings = QtGui.QWidget(self.options_area)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_settings.sizePolicy().hasHeightForWidth())
        self.general_settings.setSizePolicy(sizePolicy)
        self.general_settings.setObjectName(_fromUtf8("general_settings"))
        self.corpus_settings = QtGui.QVBoxLayout(self.general_settings)
        self.corpus_settings.setSpacing(20)
        self.corpus_settings.setMargin(0)
        self.corpus_settings.setObjectName(_fromUtf8("corpus_settings"))
        self.frame = QtGui.QFrame(self.general_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setMargin(10)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.combo_corpus = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_corpus.sizePolicy().hasHeightForWidth())
        self.combo_corpus.setSizePolicy(sizePolicy)
        self.combo_corpus.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.combo_corpus.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combo_corpus.setObjectName(_fromUtf8("combo_corpus"))
        self.horizontalLayout_5.addWidget(self.combo_corpus)
        self.corpus_settings.addWidget(self.frame)
        self.frame1 = QtGui.QFrame(self.general_settings)
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame1)
        self.gridLayout_5.setMargin(10)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.radio_mode_context = QtGui.QRadioButton(self.frame1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_mode_context.sizePolicy().hasHeightForWidth())
        self.radio_mode_context.setSizePolicy(sizePolicy)
        self.radio_mode_context.setChecked(True)
        self.radio_mode_context.setObjectName(_fromUtf8("radio_mode_context"))
        self.gridLayout_5.addWidget(self.radio_mode_context, 0, 2, 1, 1)
        self.radio_mode_frequency = QtGui.QRadioButton(self.frame1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_mode_frequency.sizePolicy().hasHeightForWidth())
        self.radio_mode_frequency.setSizePolicy(sizePolicy)
        self.radio_mode_frequency.setObjectName(_fromUtf8("radio_mode_frequency"))
        self.gridLayout_5.addWidget(self.radio_mode_frequency, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.radio_mode_tokens = QtGui.QRadioButton(self.frame1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_mode_tokens.sizePolicy().hasHeightForWidth())
        self.radio_mode_tokens.setSizePolicy(sizePolicy)
        self.radio_mode_tokens.setObjectName(_fromUtf8("radio_mode_tokens"))
        self.gridLayout_5.addWidget(self.radio_mode_tokens, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 1, 1, 1)
        self.corpus_settings.addWidget(self.frame1)
        self.frame_3 = QtGui.QFrame(self.general_settings)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setMargin(10)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.context_left_span_label = QtGui.QLabel(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context_left_span_label.sizePolicy().hasHeightForWidth())
        self.context_left_span_label.setSizePolicy(sizePolicy)
        self.context_left_span_label.setObjectName(_fromUtf8("context_left_span_label"))
        self.horizontalLayout_9.addWidget(self.context_left_span_label)
        spacerItem2 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.context_left_span = QtGui.QSpinBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context_left_span.sizePolicy().hasHeightForWidth())
        self.context_left_span.setSizePolicy(sizePolicy)
        self.context_left_span.setObjectName(_fromUtf8("context_left_span"))
        self.horizontalLayout_9.addWidget(self.context_left_span)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem3 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.context_right_span = QtGui.QSpinBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context_right_span.sizePolicy().hasHeightForWidth())
        self.context_right_span.setSizePolicy(sizePolicy)
        self.context_right_span.setFrame(True)
        self.context_right_span.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.context_right_span.setObjectName(_fromUtf8("context_right_span"))
        self.horizontalLayout_8.addWidget(self.context_right_span)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.context_words_as_columns = QtGui.QCheckBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context_words_as_columns.sizePolicy().hasHeightForWidth())
        self.context_words_as_columns.setSizePolicy(sizePolicy)
        self.context_words_as_columns.setObjectName(_fromUtf8("context_words_as_columns"))
        self.horizontalLayout_10.addWidget(self.context_words_as_columns)
        spacerItem4 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.corpus_settings.addWidget(self.frame_3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.corpus_settings.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.corpus_settings.addItem(spacerItem6)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.corpus_settings.addItem(spacerItem7)
        self.progress_bar = QtGui.QProgressBar(self.general_settings)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setMaximum(1)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.progress_bar.setInvertedAppearance(True)
        self.progress_bar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.corpus_settings.addWidget(self.progress_bar)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.corpus_settings.addItem(spacerItem8)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.corpus_settings.addItem(spacerItem9)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.button_run_query = QtGui.QPushButton(self.general_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_run_query.sizePolicy().hasHeightForWidth())
        self.button_run_query.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-start"))
        self.button_run_query.setIcon(icon)
        self.button_run_query.setObjectName(_fromUtf8("button_run_query"))
        self.horizontalLayout_6.addWidget(self.button_run_query)
        spacerItem10 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.button_show_statistics = QtGui.QPushButton(self.general_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_show_statistics.sizePolicy().hasHeightForWidth())
        self.button_show_statistics.setSizePolicy(sizePolicy)
        self.button_show_statistics.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("dialog-information"))
        self.button_show_statistics.setIcon(icon)
        self.button_show_statistics.setObjectName(_fromUtf8("button_show_statistics"))
        self.horizontalLayout_6.addWidget(self.button_show_statistics)
        self.corpus_settings.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addWidget(self.general_settings)
        self.input_settings = QtGui.QFrame(self.options_area)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_settings.sizePolicy().hasHeightForWidth())
        self.input_settings.setSizePolicy(sizePolicy)
        self.input_settings.setFrameShape(QtGui.QFrame.StyledPanel)
        self.input_settings.setFrameShadow(QtGui.QFrame.Raised)
        self.input_settings.setObjectName(_fromUtf8("input_settings"))
        self.verticalLayout = QtGui.QVBoxLayout(self.input_settings)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radio_query_string = QtGui.QRadioButton(self.input_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_query_string.sizePolicy().hasHeightForWidth())
        self.radio_query_string.setSizePolicy(sizePolicy)
        self.radio_query_string.setText(_fromUtf8(""))
        self.radio_query_string.setChecked(True)
        self.radio_query_string.setObjectName(_fromUtf8("radio_query_string"))
        self.gridLayout_2.addWidget(self.radio_query_string, 0, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.input_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1)
        self.edit_query_string = QtGui.QTextEdit(self.input_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_query_string.sizePolicy().hasHeightForWidth())
        self.edit_query_string.setSizePolicy(sizePolicy)
        self.edit_query_string.setObjectName(_fromUtf8("edit_query_string"))
        self.gridLayout_2.addWidget(self.edit_query_string, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radio_query_file = QtGui.QRadioButton(self.input_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_query_file.sizePolicy().hasHeightForWidth())
        self.radio_query_file.setSizePolicy(sizePolicy)
        self.radio_query_file.setText(_fromUtf8(""))
        self.radio_query_file.setObjectName(_fromUtf8("radio_query_file"))
        self.gridLayout_3.addWidget(self.radio_query_file, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.input_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)
        self.edit_file_name = QtGui.QLineEdit(self.input_settings)
        self.edit_file_name.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_file_name.sizePolicy().hasHeightForWidth())
        self.edit_file_name.setSizePolicy(sizePolicy)
        self.edit_file_name.setAccessibleDescription(_fromUtf8(""))
        self.edit_file_name.setInputMask(_fromUtf8(""))
        self.edit_file_name.setText(_fromUtf8(""))
        self.edit_file_name.setReadOnly(True)
        self.edit_file_name.setObjectName(_fromUtf8("edit_file_name"))
        self.gridLayout_3.addWidget(self.edit_file_name, 2, 1, 1, 1)
        self.button_file_options = QtGui.QPushButton(self.input_settings)
        self.button_file_options.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_file_options.sizePolicy().hasHeightForWidth())
        self.button_file_options.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-properties"))
        self.button_file_options.setIcon(icon)
        self.button_file_options.setObjectName(_fromUtf8("button_file_options"))
        self.gridLayout_3.addWidget(self.button_file_options, 2, 2, 1, 1)
        self.button_browse_file = QtGui.QPushButton(self.input_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browse_file.sizePolicy().hasHeightForWidth())
        self.button_browse_file.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.button_browse_file.setIcon(icon)
        self.button_browse_file.setObjectName(_fromUtf8("button_browse_file"))
        self.gridLayout_3.addWidget(self.button_browse_file, 1, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_7.addWidget(self.input_settings)
        self.options_setting = QtGui.QFrame(self.options_area)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options_setting.sizePolicy().hasHeightForWidth())
        self.options_setting.setSizePolicy(sizePolicy)
        self.options_setting.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.options_setting.setFrameShape(QtGui.QFrame.StyledPanel)
        self.options_setting.setFrameShadow(QtGui.QFrame.Raised)
        self.options_setting.setObjectName(_fromUtf8("options_setting"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.options_setting)
        self.verticalLayout_11.setMargin(10)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_9 = QtGui.QLabel(self.options_setting)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_11.addWidget(self.label_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.line = QtGui.QFrame(self.options_setting)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.scrollArea = QtGui.QScrollArea(self.options_setting)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.options_scroll_content = QtGui.QWidget()
        self.options_scroll_content.setGeometry(QtCore.QRect(0, 0, 254, 223))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options_scroll_content.sizePolicy().hasHeightForWidth())
        self.options_scroll_content.setSizePolicy(sizePolicy)
        self.options_scroll_content.setObjectName(_fromUtf8("options_scroll_content"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.options_scroll_content)
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.options_list = QtGui.QGridLayout()
        self.options_list.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.options_list.setMargin(0)
        self.options_list.setHorizontalSpacing(20)
        self.options_list.setObjectName(_fromUtf8("options_list"))
        self.label_2 = QtGui.QLabel(self.options_scroll_content)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.options_list.addWidget(self.label_2, 0, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.options_scroll_content)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.options_list.addWidget(self.checkBox, 0, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.options_list.addItem(spacerItem11, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.options_list)
        self.scrollArea.setWidget(self.options_scroll_content)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7.addWidget(self.options_setting)
        self.verticalLayout_4.addWidget(self.options_area)
        self.tabbed_views = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabbed_views.sizePolicy().hasHeightForWidth())
        self.tabbed_views.setSizePolicy(sizePolicy)
        self.tabbed_views.setTabPosition(QtGui.QTabWidget.South)
        self.tabbed_views.setObjectName(_fromUtf8("tabbed_views"))
        self.results_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_tab.sizePolicy().hasHeightForWidth())
        self.results_tab.setSizePolicy(sizePolicy)
        self.results_tab.setObjectName(_fromUtf8("results_tab"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.results_tab)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.data_preview = QtGui.QTableView(self.results_tab)
        self.data_preview.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.data_preview.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.data_preview.setAlternatingRowColors(True)
        self.data_preview.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.data_preview.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.data_preview.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.data_preview.setSortingEnabled(True)
        self.data_preview.setObjectName(_fromUtf8("data_preview"))
        self.verticalLayout_9.addWidget(self.data_preview)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("table"))
        self.tabbed_views.addTab(self.results_tab, icon, _fromUtf8(""))
        self.log_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_tab.sizePolicy().hasHeightForWidth())
        self.log_tab.setSizePolicy(sizePolicy)
        self.log_tab.setObjectName(_fromUtf8("log_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.log_tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.log_table = QtGui.QTableView(self.log_tab)
        self.log_table.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.log_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.log_table.setSortingEnabled(True)
        self.log_table.setObjectName(_fromUtf8("log_table"))
        self.log_table.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.log_table)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("utilities-log-viewer"))
        self.tabbed_views.addTab(self.log_tab, icon, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabbed_views)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHilfe = QtGui.QMenu(self.menubar)
        self.menuHilfe.setObjectName(_fromUtf8("menuHilfe"))
        self.menuCorpus = QtGui.QMenu(self.menubar)
        self.menuCorpus.setObjectName(_fromUtf8("menuCorpus"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_open_input_file = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.action_open_input_file.setIcon(icon)
        self.action_open_input_file.setObjectName(_fromUtf8("action_open_input_file"))
        self.action_save_results = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.action_save_results.setIcon(icon)
        self.action_save_results.setObjectName(_fromUtf8("action_save_results"))
        self.action_help = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-contents"))
        self.action_help.setIcon(icon)
        self.action_help.setObjectName(_fromUtf8("action_help"))
        self.action_about_coquery = QtGui.QAction(MainWindow)
        self.action_about_coquery.setObjectName(_fromUtf8("action_about_coquery"))
        self.actionDummy = QtGui.QAction(MainWindow)
        self.actionDummy.setObjectName(_fromUtf8("actionDummy"))
        self.action_distinct_tokens = QtGui.QAction(MainWindow)
        self.action_distinct_tokens.setObjectName(_fromUtf8("action_distinct_tokens"))
        self.action_frequency = QtGui.QAction(MainWindow)
        self.action_frequency.setObjectName(_fromUtf8("action_frequency"))
        self.action_all_tokens = QtGui.QAction(MainWindow)
        self.action_all_tokens.setObjectName(_fromUtf8("action_all_tokens"))
        self.action_statistics = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("view-statistics"))
        self.action_statistics.setIcon(icon)
        self.action_statistics.setObjectName(_fromUtf8("action_statistics"))
        self.action_mySQL_settings = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("server-database"))
        self.action_mySQL_settings.setIcon(icon)
        self.action_mySQL_settings.setObjectName(_fromUtf8("action_mySQL_settings"))
        self.action_options = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("configure"))
        self.action_options.setIcon(icon)
        self.action_options.setObjectName(_fromUtf8("action_options"))
        self.action_quit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("application-exit"))
        self.action_quit.setIcon(icon)
        self.action_quit.setObjectName(_fromUtf8("action_quit"))
        self.action_build_corpus = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-new"))
        self.action_build_corpus.setIcon(icon)
        self.action_build_corpus.setObjectName(_fromUtf8("action_build_corpus"))
        self.action_remove_corpus = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-delete"))
        self.action_remove_corpus.setIcon(icon)
        self.action_remove_corpus.setObjectName(_fromUtf8("action_remove_corpus"))
        self.action_install_corpus = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("server-database"))
        self.action_install_corpus.setIcon(icon)
        self.action_install_corpus.setObjectName(_fromUtf8("action_install_corpus"))
        self.menuFile.addAction(self.action_open_input_file)
        self.menuFile.addAction(self.action_save_results)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menuHilfe.addAction(self.action_help)
        self.menuHilfe.addSeparator()
        self.menuHilfe.addAction(self.action_about_coquery)
        self.menuCorpus.addAction(self.action_build_corpus)
        self.menuCorpus.addAction(self.action_install_corpus)
        self.menuCorpus.addAction(self.action_remove_corpus)
        self.menuCorpus.addSeparator()
        self.menuCorpus.addAction(self.action_statistics)
        self.menuSettings.addAction(self.action_mySQL_settings)
        self.menuSettings.addAction(self.action_options)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCorpus.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())
        self.label_5.setBuddy(self.general_settings)

        self.retranslateUi(MainWindow)
        self.tabbed_views.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Coquery", None))
        self.label_5.setText(_translate("MainWindow", "Corpus:", None))
        self.radio_mode_context.setText(_translate("MainWindow", "&Distinct tokens", None))
        self.radio_mode_frequency.setText(_translate("MainWindow", "&Frequency", None))
        self.label_6.setText(_translate("MainWindow", "Query mode", None))
        self.radio_mode_tokens.setText(_translate("MainWindow", "&All tokens", None))
        self.context_left_span_label.setText(_translate("MainWindow", "Left context::", None))
        self.context_left_span.setSpecialValueText(_translate("MainWindow", "none", None))
        self.context_left_span.setSuffix(_translate("MainWindow", " words", None))
        self.label_7.setText(_translate("MainWindow", "Right context::", None))
        self.context_right_span.setSpecialValueText(_translate("MainWindow", "none", None))
        self.context_right_span.setSuffix(_translate("MainWindow", " words", None))
        self.context_words_as_columns.setText(_translate("MainWindow", "Words as columns (KWIC)", None))
        self.progress_bar.setFormat(_translate("MainWindow", "Ready.", None))
        self.button_run_query.setText(_translate("MainWindow", "Query", None))
        self.button_show_statistics.setText(_translate("MainWindow", "Statistics", None))
        self.label_12.setText(_translate("MainWindow", "Enter query strings:", None))
        self.label_8.setText(_translate("MainWindow", "Use query file:", None))
        self.edit_file_name.setPlaceholderText(_translate("MainWindow", "(no file selected)", None))
        self.button_file_options.setText(_translate("MainWindow", "O&ptions...", None))
        self.button_file_options.setShortcut(_translate("MainWindow", "Alt+B", None))
        self.button_browse_file.setText(_translate("MainWindow", "&Open", None))
        self.button_browse_file.setShortcut(_translate("MainWindow", "Alt+B", None))
        self.label_9.setText(_translate("MainWindow", "Output columns", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.checkBox.setText(_translate("MainWindow", "Name of input file         ", None))
        self.tabbed_views.setTabText(self.tabbed_views.indexOf(self.results_tab), _translate("MainWindow", "Query result", None))
        self.tabbed_views.setTabText(self.tabbed_views.indexOf(self.log_tab), _translate("MainWindow", "Query log", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHilfe.setTitle(_translate("MainWindow", "Help", None))
        self.menuCorpus.setTitle(_translate("MainWindow", "Corpus", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.action_open_input_file.setText(_translate("MainWindow", "&Open input file...", None))
        self.action_open_input_file.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_save_results.setText(_translate("MainWindow", "&Save results...", None))
        self.action_save_results.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.action_help.setText(_translate("MainWindow", "Help", None))
        self.action_help.setShortcut(_translate("MainWindow", "F1", None))
        self.action_about_coquery.setText(_translate("MainWindow", "About Coquery", None))
        self.actionDummy.setText(_translate("MainWindow", "Dummy", None))
        self.action_distinct_tokens.setText(_translate("MainWindow", "Distinct tokens", None))
        self.action_frequency.setText(_translate("MainWindow", "Frequency", None))
        self.action_all_tokens.setText(_translate("MainWindow", "All tokens", None))
        self.action_statistics.setText(_translate("MainWindow", "Corpus statistics", None))
        self.action_mySQL_settings.setText(_translate("MainWindow", "MySQL settings...", None))
        self.action_options.setText(_translate("MainWindow", "Options...", None))
        self.action_quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.action_build_corpus.setText(_translate("MainWindow", "&Build corpus...", None))
        self.action_build_corpus.setToolTip(_translate("MainWindow", "Build a new corpus from text files in a folder", None))
        self.action_remove_corpus.setText(_translate("MainWindow", "&Remove corpus...", None))
        self.action_remove_corpus.setToolTip(_translate("MainWindow", "Permanently and irrevocably remove corpus database", None))
        self.action_install_corpus.setText(_translate("MainWindow", "&Install corpus...", None))
        self.action_install_corpus.setToolTip(_translate("MainWindow", "Install a corpus into a MySQL database", None))

