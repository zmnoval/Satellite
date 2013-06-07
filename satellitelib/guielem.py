# -*- coding: utf-8 -*-

#Copyright (c) 2010 David Trémouilles

#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:

#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

import logging

try:
    from PyQt4 import QtGui
    pyqt=True
except ImportError:
    try:
        from PySide import QtGui
        from PySide import QtCore
        pyqt=False
    except ImportError:
        raise ImportError("ERROR: Install either PyQt4 or PySide bindings")



class ViewTab(QtGui.QTabWidget):
    # pylint: disable=R0904
    def __init__(self, parent=None):
        QtGui.QTabWidget.__init__(self, parent)
        self.setMovable(True)
        self.setTabsClosable(False)
        self.setUsesScrollButtons(False)


class SatusBarLogHandler(logging.Handler):
    def __init__(self, log_signal):
        logging.Handler.__init__(self)
        self.log_signal = log_signal

    def emit(self, record):
        log_message = self.format(record)
        if pyqt:  #Solve nasty bug with pyside 1.1.2
            self.log_signal.emit(log_message)
