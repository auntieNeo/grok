# -*- coding: utf-8 -*-

import os
import json
import re
from aqt import mw
from aqt.qt import *

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class GrokDialog:
    __metaclass__ = Singleton
    def __init__(self, dataDir):
        pass

    def startScraping(self):
        pass

    def showSettingsDialog(self):
        dialog = QDialog(mw)
        layout = QVBoxLayout()
        scraperComboBox = QComboBox()
        for scraper in self.scraperPlugins():
            scraperComboBox.addItem(scraper[0], scraper[1])
        layout.addWidget(QLabel("Scraper plugin to use:"))
        layout.addWidget(scraperComboBox)
        bottomLayout = QHBoxLayout()
        startButton = QPushButton("Start")
        startButton.connect(startButton, SIGNAL("clicked()"), dialog, SLOT("accept()"))
        bottomLayout.addWidget(startButton)
        cancelButton = QPushButton("Cancel")
        cancelButton.connect(cancelButton, SIGNAL("clicked()"), dialog, SLOT("reject()"))
        bottomLayout.addWidget(cancelButton)
        layout.addLayout(bottomLayout)
        dialog.setLayout(layout)
        if dialog.exec_():
            self.startScraping(scraperComboBox.itemData(scraperComboBox.currentIndex()));
