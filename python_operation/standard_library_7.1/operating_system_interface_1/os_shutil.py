# return the current working directory
import os
current_dir=os.getcwd()
# D:\Pycharm\Workspace\git_operation\python_operation\standard_library_7.output_formatting_1.1\operating_system_interface_1
print('current_dir:{}'.format(current_dir))
# Change current working directory
os.chdir('/python_operation/standard_library_7.output_formatting_1.1/operating_system_interface_1')
print('current_dir:{}'.format(os.getcwd()))
# Run the command mkdir in the system shell--in the current dir
os.system('mkdir today')

# dir()--return a list of all module functions
module_functions = dir(os)
print('module_functions:',module_functions)
# help
# print('help:',help(os))


# shutil
"""
copyfile
"""
import shutil
# copy the current package.__init__.py to the today_dir
shutil.copyfile('__init__.py','today/new_init.py')
shutil.move('today/new_init.py','./')
