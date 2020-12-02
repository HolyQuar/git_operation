"""
To create a virtual environment, decide upon a directory where you want to place it,
-and run the venv module as a script with the directory path:
"""
"""This will create the tutorial-env directory if it doesn’t exist, 
-and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files."""
# > python3 -m venv turorial-env
"""
 activate a virtual environment.
"""
# On Windows, run:
# > tutorial-env\Scripts\activate.bat
# On Unix or MacOS, run:
# > source tutorial-env/bin/activate
# lookup the activated the virtual environment:
"""
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
"""