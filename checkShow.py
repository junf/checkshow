"""
   Copyright 2013 Jun Funada

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import sys
from PySide import QtCore
from PySide import QtGui

MSEC = 100      # time to start check (msec)
_window = None  # window to check


def check():
    """Check _windows's geometry"""
    print("geometry(before show):         ", _window.geometry())
    _window.show()
    print("geometry(after show):          ", _window.geometry())
    _window.showMaximized()
    print("geometry(after showMaximized): ", _window.geometry())
    _window.showMinimized()
    print("geometry(after showMinimized): ", _window.geometry())
    _window.showFullScreen()
    print("geometry(after showFullScreen):", _window.geometry())
    _window.showNormal()
    print("geometry(after showNormal):    ", _window.geometry())
    _window.setGeometry(100,100,300,400)
    print("geometry(after setGeometry):   ", _window.geometry())
    _window.showMinimized()
    print("geometry(after showMinimized again): ", _window.geometry())
    _window.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    _window = QtGui.QMainWindow()

    timer = QtCore.QTimer()
    timer.timeout.connect(check)
    timer.start(MSEC)

    sys.exit(app.exec_())
