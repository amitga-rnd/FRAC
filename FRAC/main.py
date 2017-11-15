import time

import kivy
#kivy.require() # replace with your current kivy version !
from kivy import Config

from kivy.app import App
from kivy.properties import ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

Config.set("kivy", "keyboard_mode", "systemanddock")
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")


class FRACApp(App):

    def build(self):
        appMain = FRACMain()
        Clock.schedule_interval(appMain.update, 1.0)
        return appMain

class FRACMain(GridLayout):
    dateTimeLabel = ObjectProperty(None)

    def update(self, dt):
        self.dateTimeLabel.text = time.strftime("%H:%M:%S\n%d/%m/%Y")

if __name__ == '__main__':
    FRACApp().run()