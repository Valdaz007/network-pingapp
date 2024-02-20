import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

import pandas as pd
df = pd.read_csv('client.csv')

from pingmods.client import Client


class MiScreen(GridLayout):
    customer = ObjectProperty(None)

    clients = [Client(df['ip'][row],df['name'][row],df['province'][row],df['urban'][row],df['id'][row]) for row in df.index]

    def getcust(self):
        return self.cust1.show()
    
    def pingCust(self):
        self.customer.text = self.cust1.pingIP()

class MainApp(App):
    def build(self):
        return MiScreen()

if __name__  == "__main__":
    MainApp().run()