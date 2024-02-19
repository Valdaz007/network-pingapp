import kivy
from kivy.app import App
from kivy.uix.label import Label
from pingmods.client import Client

class MyApp(App):
    def build(self):
        cust = Client("192.168.100.1", "Victor", "POM", "6 Mile", 20161232)
        return Label(text=cust.show())
    

if __name__  == "__main__":
    MyApp().run()