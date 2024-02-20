import os

def ping(ip:str):
    os.system(f"ping {ip} > ping.txt")

def result() -> str:
    with open('ping.txt', 'r') as file:
        file_content = file.read()
        return file_content
