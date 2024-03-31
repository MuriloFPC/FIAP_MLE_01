import os
import urllib.request
from pathlib import Path

_basePath = './CSV/'

def GetCsv(url, name):
    my_file = Path(name)
    if my_file.is_file():
        return

    if not os.path.exists(_basePath):
        os.makedirs(_basePath)
    urllib.request.urlretrieve(url, _basePath+name)

def ReadCsv(fileName):
    with open(_basePath+fileName, 'r', encoding='UTF-8') as file:
        return [line.rstrip() for line in file]

