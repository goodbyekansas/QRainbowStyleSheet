#!python
# -*- coding: utf-8 -*-

"""This module provides a main window for UI tests."""

import logging
import sys
import argparse
import qrainbowstyle


def get_main_window_app(qt_from="pyqt", no_dark=True):
    """Return main window application."""

    # set log for debug
    logging.basicConfig(level=logging.DEBUG)

    style = ""

    if qt_from == "pyqt5":
        # using PyQt5 wrapper
        from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
        from PyQt5.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize

        # getting style
        style = qrainbowstyle.load_stylesheet(qt_api="pyqt5")

    elif qt_from == "qtpy":
        # using QtPy API
        from qtpy.QtWidgets import QApplication, QMainWindow, QDockWidget
        from qtpy.QtCore import QTimer, Qt, QSettings, QByteArray, QPoint, QSize

        # getting style
        style = qrainbowstyle.load_stylesheet()

    if no_dark:
        style = ""

    # create the application
    app = QApplication(sys.argv)
    app.setOrganizationName("QRainbowStyle")
    app.setApplicationName("QRainbowStyle Test")
    # setup stylesheet
    app.setStyleSheet(style)
    # create main window
    window = QMainWindow()
    window.setWindowTitle(
        "QRainbowStyle v." + qrainbowstyle.__version__ + " - TEST - Using " + qt_from
    )
    # auto quit after 2s when testing on travis-ci
    if "--test" in sys.argv:
        QTimer.singleShot(2000, app.exit)
    # run
    window.showMaximized()
    app.exec_()

    return window
