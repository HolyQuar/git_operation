# Template subclasses can specify a custom delimiter.
import time, os.path
from string import Template
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    # custom delimiter is  %
    delimiter = '%'
""" elect to use percent signs for placeholders 
-such as the current date, image sequence number, or file format"""
fmt = input('Enter rename (%d-data %n-seqnum %f-format): ')
print('fmt:{}'.format(fmt))
t = BatchRename(fmt)
time1 = time.strftime('%d%b%y')
date= time.strftime('%Y-%m-%d',time.localtime())

print('date:{}'.format(date))
for i,filename in enumerate(photofiles):
    base,ext = os.path.splitext(filename)
    newname = t.substitute(d=date,n=i,f=ext)
    print('{0}--->{1}'.format(filename,newname))