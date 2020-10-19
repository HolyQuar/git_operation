"""
the following output results from running python demo.py one two three
at the command line:
"""
import os
# D:\Pycharm\Workspace\git_operation\python_operation\standard_library_7.output_formatting_1.1\command_line_arguments_3\sys_argv_and_argparse.py
print(os.getcwd())
import sys
"""when the command line input the arguments like one two three 
console will print:
python python
_operation\standard_library\command_line_arguments\sys_
argv.py one two three-->
[current_file_path,arguments]
"""
print(sys.argv)

# argparse
"""The argparse module provides a more sophisticated mechanism to process command line arguments

"""
import argparse
"""The following script 
-extracts one or more filenames 
-and an optional number of lines to be displayed:"""
parser = argparse.ArgumentParser(prog='top',description='Show top lines from each file')
parser.add_argument('filenames',nargs='+')
parser.add_argument('-l','--lines',type=int,default=10)
args=parser.parse_args()
print(args)
print('args.lines:{},args.filenames:{}'.format(args.lines,str(args.filenames)))