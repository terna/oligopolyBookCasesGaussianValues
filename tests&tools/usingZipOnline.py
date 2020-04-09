# lettura da zip online

# https://docs.python.org/3/library/zipfile.html

# https://stackoverflow.com/questions/9419162/download-returned-zip-file-from-url

import zipfile, requests, io

# "My new User-Agent" is a trick from
# http://wolfprojects.altervista.org/articles/change-urllib-user-agent/
# unnecessary with github repositories, but does not hurt if left there
#r = requests.get('https://terna.to.it/zip/1.txt.zip',\
r = requests.get(\
'https://raw.githubusercontent.com/terna/oligopolyBookCasesGaussianValues/master/1.txt.zip',\
                 headers = { "User-Agent":"My new User-Agent"}) # or 11.txt.zip

z = zipfile.ZipFile(io.BytesIO(r.content))

z.extractall()

myfile=z.open('1.txt') # or 11.txt

for i in range(10):
    l=myfile.readline()
    print(eval(l))

z.close()
