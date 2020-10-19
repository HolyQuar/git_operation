"""
The glob module provides a function for
-making file lists from directory wildcard searches:
"""
import glob

# default current_package_path-->module_list
file_list = glob.glob('*.py')
print('file_list:{}'.format(file_list))

# definition a path--lookup the target_file
path_name = 'D:\Pycharm\Workspace\git_operation\python_operation\standard_library\operating_system_interface'
target_file = glob.glob1(path_name,'*.py')
print('target_files:{}'.format(target_file))
