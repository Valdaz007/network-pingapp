import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from pingmods.client import Client


class MiScreen(BoxLayout):
    cust1 = Client("202.58.131.150", "JBL", "POM", "Motukea", 1)
    # cust2 = Client("202.58.131.182", "NEA", "POM", "Waigani Central", 3)
    # cust3 = Client("202.58.131.242", "RTA", "POM", "Kunai St", 4)
    customer = ObjectProperty(None)

    def getcust(self):
        return self.cust1.show()
    
    def pingCust(self):
        self.customer.text = self.cust1.pingIP()

class MainApp(App):
    def build(self):
        return MiScreen()

if __name__  == "__main__":
    MainApp().run()