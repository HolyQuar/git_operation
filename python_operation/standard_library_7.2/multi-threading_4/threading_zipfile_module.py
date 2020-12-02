"""
Threads can be used to improve the responsiveness of applications that accept user input while other tasks run
    in the background.
--A related use case is running I/O in parallel with computations in another thread.
"""

import threading, zipfile

"""how the high level threading module can run tasks in background 
while the main program continues to run:"""


# definition IO_class
class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of: ', self.infile)
background = AsyncZip('mydata.txt','myarchive.zip')
background.start()
# Wait for the background task to finish
background.join()
print('The main program continues to run in foreground.')
