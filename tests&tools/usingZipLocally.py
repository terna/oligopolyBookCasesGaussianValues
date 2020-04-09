# https://docs.python.org/3/library/zipfile.html

import zipfile

import urllib.request

with zipfile.ZipFile('testIn.txt.zip') as myzip:
    myfile=myzip.open('testIn.txt')
    for l in myfile:
        print(eval(l))
    myzip.close()


with zipfile.ZipFile('11.txt.zip') as myzip:
    myfile=myzip.open('11.txt')
    for i in range(10):
        l=myfile.readline()
        print(eval(l))

    myzip.close()
