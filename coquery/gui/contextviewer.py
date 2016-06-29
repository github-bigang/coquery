# -*- coding: utf-8 -*-
"""
contextview.py is part of Coquery.

Copyright (c) 2016 Gero Kunter (gero.kunter@coquery.org)

Coquery is released under the terms of the GNU General Public License (v3).
For details, see the file LICENSE that you should have received along 
with Coquery. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import division
from __future__ import unicode_literals

import sys
import os
import pandas as pd

from coquery import options
from coquery.unicode import utf8
from . import classes
from .pyqt_compat import QtCore, QtGui
from .ui.contextViewerUi import Ui_ContextView

class ContextView(QtGui.QWidget):
    def __init__(self, corpus, token_id, source_id, token_width, icon=None, parent=None):
        
        super(ContextView, self).__init__(parent)
        
        self.corpus = corpus
        self.token_id = token_id
        self.source_id = source_id
        self.token_width = token_width
        
        self.ui = Ui_ContextView()
        self.ui.setupUi(self)

        if icon:
            self.setWindowIcon(icon)

        self.ui.slider_context_width.setTracking(True)

        # Add clickable header
        self.ui.button_ids = classes.CoqDetailBox("{} – Token ID {}".format(corpus.resource.name, token_id))
        self.ui.button_ids.clicked.connect(lambda: options.settings.setValue("contextviewer_details", utf8(not self.ui.button_ids.isExpanded())))
        self.ui.verticalLayout_3.insertWidget(0, self.ui.button_ids)
        self.ui.form_information = QtGui.QFormLayout(self.ui.button_ids.box)
        
        L = self.corpus.get_origin_data(token_id)
        for table, fields in sorted(L):
            self.add_source_label(table)
            for label in sorted(fields.keys()):
                self.add_source_label(label, fields[label])

        words = options.settings.value("contextviewer_words", None)
        if words != None:
            try:
                self.ui.spin_context_width.setValue(int(words))
                self.ui.slider_context_width.setValue(int(words))
            except ValueError:
                pass
            
        self.ui.spin_context_width.valueChanged.connect(self.spin_changed)
        self.ui.slider_context_width.valueChanged.connect(self.slider_changed)

        self.update_context()

        try:
            self.resize(options.settings.value("contextviewer_size"))
        except TypeError:
            pass
        try:
            self.ui.slider_context_width(options.settings.value("contextviewer_words"))
        except TypeError:
            pass
        val = options.settings.value("contextviewer_details") != "False"
        if val:
            self.ui.button_ids.setExpanded(val)
        else:
            self.ui.button_ids.setExpanded(False)

        self.ui.context_area.setStyleSheet(corpus.get_context_stylesheet())

    def closeEvent(self, *args):
        options.settings.setValue("contextviewer_size", self.size())
        options.settings.setValue("contextviewer_words", self.ui.slider_context_width.value())
        
    def add_source_label(self, name, content=None):
        """ 
        Add the label 'name' with value 'content' to the context viewer.
        """
        layout_row = self.ui.form_information.count()
        self.ui.source_name = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.source_name.sizePolicy().hasHeightForWidth())
        self.ui.source_name.setSizePolicy(sizePolicy)
        self.ui.source_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.ui.source_name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ui.form_information.setWidget(layout_row, QtGui.QFormLayout.LabelRole, self.ui.source_name)
        self.ui.source_content = QtGui.QLabel(self)
        self.ui.source_content.setWordWrap(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.source_content.sizePolicy().hasHeightForWidth())
        self.ui.source_content.setSizePolicy(sizePolicy)
        self.ui.source_content.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ui.source_content.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.ui.form_information.setWidget(layout_row, QtGui.QFormLayout.FieldRole, self.ui.source_content)
        
        if name:
            if content == None:
                name = "<b>{}</b>".format(name)
            else:
                name = utf8(name).strip()
                if not name.endswith(":"):
                    name += ":"
            self.ui.source_name.setText(name)
            
        if content:
            content = utf8(content).strip()
            if os.path.exists(content) or "://" in content:
                content = "<a href={0}>{0}</a>".format(content)
                self.ui.source_content.setOpenExternalLinks(True)
                self.ui.source_content.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
            self.ui.source_content.setText(content)
            
    def spin_changed(self):
        self.ui.slider_context_width.valueChanged.disconnect(self.slider_changed)
        self.ui.slider_context_width.setValue(self.ui.spin_context_width.value())
        self.update_context()
        self.ui.slider_context_width.valueChanged.connect(self.slider_changed)
        options.settings.setValue("contextviewer_words", self.ui.slider_context_width.value())
    
    def slider_changed(self):
        self.ui.spin_context_width.valueChanged.disconnect(self.spin_changed)
        self.ui.spin_context_width.setValue(self.ui.slider_context_width.value())
        self.update_context()
        self.ui.spin_context_width.valueChanged.connect(self.spin_changed)
        options.settings.setValue("contextviewer_words", self.ui.slider_context_width.value())
    
    def update_context(self):
        if self.corpus:
            context = self.corpus.get_rendered_context(
                self.token_id, 
                self.source_id, 
                self.token_width,
                self.ui.slider_context_width.value(), self)
            font = options.cfg.context_font
            
            if int(font.style()) == int(QtGui.QFont.StyleItalic):
                style = "italic"
            elif int(font.style()) == int(QtGui.QFont.StyleOblique):
                style = "oblique"
            else:
                style = "normal"
                
            if font.stretch() == int(QtGui.QFont.UltraCondensed):
                stretch = "ultra-condensed"
            elif font.stretch() == int(QtGui.QFont.ExtraCondensed):
                stretch = "extra-condensed"
            elif font.stretch() == int(QtGui.QFont.Condensed):
                stretch = "condensed"
            elif font.stretch() == int(QtGui.QFont.SemiCondensed):
                stretch = "semi-condensed"
            elif font.stretch() == int(QtGui.QFont.Unstretched):
                stretch = "normal"
            elif font.stretch() == int(QtGui.QFont.SemiExpanded):
                stretch = "semi-expanded"
            elif font.stretch() == int(QtGui.QFont.Expanded):
                stretch = "expanded"
            elif font.stretch() == int(QtGui.QFont.ExtraExpanded):
                stretch = "extra-expanded"
            elif font.stretch() == int(QtGui.QFont.UltraExpanded):
                stretch = "ultra-expanded"

            weight = int(font.weight()) * 10
            
            styles = []
            
            styles.append('line-height: {}px'.format(font.pointSize() * 1.5))
            styles.append('font: {}px "{}"'.format(font.pointSize(), font.family()))
            styles.append("font-style: {}".format(style))
            styles.append("font-weight: {}".format(weight))
            styles.append("font-strech: {}".format(stretch))

            if font.underline():
                context = "<u>{}</u>".format(context)
            if font.strikeOut():
                context = "<s>{}</s>".format(context)

            s = "<div style='{}'>{}</div>".format("; ".join(styles), context)

            self.ui.context_area.setText(s)
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
            
def main():
    app = QtGui.QApplication(sys.argv)
    viewer = ContextView(None, None, None, None, 0)
    viewer.exec_()
    
if __name__ == "__main__":
    main()
    