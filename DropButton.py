# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:08:14 2023

@author: user
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class DropButton(QtWidgets.QPushButton):
    def __init__(self, *args, question, **kwargs):
        QtWidgets.QPushButton.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.status = 0
        self.answer = ""
        self.question = question

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()
        text = event.mimeData().text().strip()
        self.answer = text
        event.acceptProposedAction()