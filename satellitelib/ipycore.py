#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright (c) 2012 David Trémouilles

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

"""Run Satellite graphical user interface
on top of ipython.
"""

import sys
try:
    from PyQt4 import QtCore
except ImportError:
    try:
        from PySide import QtCore
    except ImportError:
        raise ImportError("ERROR: Install either PyQt4 or PySide bindings")


from .internal_ipkernel import InternalIPKernel
from .core import MainWin, _init_logging


class IpyMainWin(MainWin, InternalIPKernel):
    def __init__(self, app):
        self.init_ipkernel('qt')
        MainWin.__init__(self, app)
        self.namespace['storm'] = self.core_storm


def main():
    """Call this function to run Satellite
    graphical user interface.
    """
    _init_logging()
    app = QtGui.QApplication(sys.argv)
    mainwin = IpyMainWin(app)
    mainwin.show()
    # Very important, IPython-specific step: this gets GUI event loop
    # integration going, and it replaces calling app.exec_()
    sys.exit(mainwin.ipkernel.start())
