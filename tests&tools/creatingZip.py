# https://docs.python.org/3/library/zipfile.html
# https://pymotw.com/3/zipfile/

import zipfile
#import zlib

compression = zipfile.ZIP_DEFLATED
print('creating archive')
with zipfile.ZipFile('123.zip', mode='w') as zf: # '1.txt.zip'
    print('123.txt') #'1.txt'
    zf.write('123.txt',compress_type=compression) #'1.txt'
    print('compressed')


# finally rm 123.txt
import os
os.remove("123.txt")
print("File 123.txt Removed!")
