"""Consult the Installing Python Modules
--guide for complete documentation for pip.
--When you’ve written a package and want to make it available on the Python Package Index,
-consult the Distributing Python Modules guide.
"""
"""You can install, upgrade, and remove packages
 -sing a program called pip
"""
# pip’s limited search feature
# (tutorial-env) $ pip search astronomy
"""
pip has a number of subcommands:
--“search”, “install”, “uninstall”, “freeze”
'list','show',etc.
"""
# You can install the latest version of a package by specifying a package’s name:
# (tutorial-env) $ pip install novas

# install a specific version of a package
"""If you re-run this command, pip will notice that the requested version 
-is already installed and do nothing"""
# (tutorial-env) $ pip install requests==2.6.0

# to upgrade the package to the latest version:
# (tutorial-env) $ pip install --upgrade requests

# remove the packages from the virtual environment.
# pip uninstall followed by one or more package names

# display information about a particular package
# (tutorial-env) $ pip show requests

# display all of the packages installed in the virtual environment
# (tutorial-env) $ pip list

# pip freeze will produce a similar list of the installed packages,
"""A common convention is to put this list in a requirements.txt file:"""
# (tutorial-env) $ pip freeze > requirements.txt

"""install all the necessary packages"""
# (tutorial-env) $ pip install -r requirements.txt