from __future__ import division
from __future__ import unicode_literals

from pyqt_compat import QtCore, QtGui
import options
import errorUi
from errors import *
import sys

class ErrorBox(QtGui.QDialog):
    def __init__(self, exc_info, parent=None):
        
        super(ErrorBox, self).__init__(parent)
        
        self.ui = errorUi.Ui_ErrorDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(options.cfg.icon)
        self.ui.icon_label.setPixmap(QtGui.QIcon.fromTheme("dialog-error").pixmap(32, 32))
        
        exc_type, exc_message, exc_trace = get_error_repr(exc_info)
        
        error_text = "<p><table><tr><td>Error type</td><td><b>{}</b></td></tr><tr><td>Error message</td><td><b>{}</b></td></tr></table></p><p>{}</p>".format(
            exc_type, exc_message, exc_trace.replace("\n", "<br>").replace(" ", "&nbsp;"))
        self.ui.trace_area.setText(error_text)
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.accept()
            
    @staticmethod
    def show(exc_info, parent=None):
        dialog = ErrorBox(exc_info, parent)
        result = dialog.exec_()
        return None
    
            
def main():
    app = QtGui.QApplication(sys.argv)
    viewer = ErrorBox(Exception())
    viewer.exec_()
    
if __name__ == "__main__":
    main()
    