""" Pack codes "H" and "I" represent two and four byte unsigned numbers respectively.
--The "<" indicates that they are standard size and in little-endian byte order:

"""
import struct
with open('my_compression.zip','rb') as f:
    data = f.read()
start = 0
for i in range(3):
    """how to loop through header information in a ZIP file 
    without using the zipfile module"""
    # show the first 3 file headers
    start +=14
    first_data = data[0:start]
    data1=data[start:start:16]
    fields = struct.unpack('<IIIHH',data[start:start+16])
    crc32,comp_size,uncomp_size,filenamesize,extra_size = fields

    start +=16
    filename = data[start:start+filenamesize]
    start +=filenamesize
    extra = data[start:start+extra_size]
    print('-------------------')
    print(filename,hex(crc32),comp_size,uncomp_size)
    # skip to the next header
    start +=extra_size + comp_size