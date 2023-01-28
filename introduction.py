# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:51:10 2022

@author: user
"""

from ui.introduction_ui import Ui_Form


class IntroductionWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.tabWidgetIntroduction.currentChanged.connect(self.onChange)

    def onChange(self, i):
        if i == 3:
            print("Jakiś tekst. Konsola działa!")