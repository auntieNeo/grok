# -*- coding: utf-8 -*-
# Scrapes websites and other sources to add Anki facts quickly and efficiently.

from grok.settings import GrokSettings
from grok.dialog import GrokDialog
from aqt import mw
from aqt.qt import *
from anki.hooks import addHook
import os.path

def init():
    scrapersDir = os.path.abspath(mw.addonManager.addonsFolder() + '/grok/scrapers')
    dialog = GrokDialog(scrapersDir);

    action = QAction(mw)
    action.setText("Grok Scraper")
    mw.form.menuTools.addAction(action)
    mw.connect(action, SIGNAL("triggered()"), dialog.showSettingsDialog)

# This hook is needed simply because mw.addonManager hasn't been assigned yet
# while the addon is first being executed.
addHook('profileLoaded', init)

