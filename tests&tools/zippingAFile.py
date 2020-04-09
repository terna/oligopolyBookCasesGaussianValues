# https://docs.python.org/3/library/zipfile.html
# https://pymotw.com/3/zipfile/

import zipfile

compression = zipfile.ZIP_DEFLATED
print('creating archive')
with zipfile.ZipFile('111.txt.zip', mode='w') as zf:
    print('111.txt')
    zf.write('111.txt',compress_type=compression)
    print('compressed')


"""
# finally rm 111.txt
import os
os.remove("111.txt")
print("File 111.txt Removed!")
"""
