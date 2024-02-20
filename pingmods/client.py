from pingmods.ping import *

class Client:
    def __init__(self, ip, name, province, urban, id):
        self.id = id
        self.name = name
        self.ip = ip
        self.province = province
        self.urban = urban
    
    # GETTERS
    def getName(self):
        return self.name
    
    def getIP(self):
        return self.ip
    
    def getProvince(self):
        return self.province
    
    def getUrban(self):
        return self.urban
    
    def getID(self):
        return self.id
    
    def show(self):
        return f"ID: {self.id}\nName: {self.name}\nIP: {self.ip}\nProvince: {self.province}\nUrban: {self.urban}"
    
    def pingIP(self) -> str:
        ping(self.getIP())
        return result()