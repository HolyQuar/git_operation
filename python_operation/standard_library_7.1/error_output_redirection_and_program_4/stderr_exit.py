"""The sys module also has attributes for stdin, stdout, and stderr
"""
"""
is useful for emitting warnings and error messages 
-to make them visible even when stdout has been redirected.
"""
import sys

print('sys.stderr:{}'.format(sys.stderr.write('Warning, log file not found starting a new one\n')))

# sys.exit()
"""The most direct way to terminate a script is to use sys.exit()."""
if __name__=='__main__':
    print('hello world.')
    sys.exit()
    print('hello')