# -*- coding: utf-8 -*-

from PyQt4 import QtCore


class GenericThread(QtCore.QThread):
    """
    A thread that generates kmlpositions and returns list with them.
    Some theory:
    https://joplaete.wordpress.com/2010/07/21/threading-with-pyqt4/
    Σημαντικό στο τρόπο που γίνονται emit στα threads:
    https://techbase.kde.org/Development/Tutorials/Python_introduction_to_signals_and_slots#Emitting_signals
    """
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.function(*self.args, **self.kwargs)
        return