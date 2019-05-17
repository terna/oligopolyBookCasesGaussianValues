# https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python


import urllib.request
import os

link = "https://raw.githubusercontent.com/terna/oligopolyBookCasesGaussianValues/master/11.txt"

try:
    f = urllib.request.urlopen(link)
except:
    print("online data not found")
    os.sys.exit(1)

for i in range(10):
    d = f.readline()
    print(float(d))
