from pingmods.client import Client
import pandas as pd
import os

df = pd.read_csv('clients.csv')

clients = [Client(df['ip'][row],df['name'][row],df['city'][row],df['urban'][row],df['id'][row]) for row in df.index]

for i in clients:
    result = os.popen("ping -n 2 " + i.getIP())
    for line in result.readlines():
        print(line)



# print(df.query('id == 1'))