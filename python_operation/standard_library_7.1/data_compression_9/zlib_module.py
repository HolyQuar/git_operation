"""
zlib, gzip, bz2, lzma, zipfile and tarfile.
"""
import zlib
# a bytes-like object
s = b'witch which has which witches wrist watch'
len_num = len(s)
print('len_num:{}'.format(len_num))
print('-------------------')
compress_object = zlib.compress(s)
new_len = len(compress_object)
print('after_compression:{}'.format(new_len))
print('compress_object: ',compress_object)
print('-------')
decompress_object = zlib.decompress(compress_object)
print('decompress_object: ',decompress_object)
crc32_nums=zlib.crc32(s)
print(s)
print('crc32_nums:{}'.format(crc32_nums))
import gzip
