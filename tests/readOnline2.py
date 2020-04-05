# https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python


import urllib.request
import os

link = "https://media.githubusercontent.com/media/terna/oligopolyBookCasesGaussianValues/master/11.txt"

try:
    f = urllib.request.urlopen(link)
except:
    print("online data not found")
    os.sys.exit(1)

# the file contains 500500 records

for i in range(400000):
    d = f.readline()

input("Enter")


for i in range(100500):
    d = f.readline()
    if i==100499: print(float(d))
