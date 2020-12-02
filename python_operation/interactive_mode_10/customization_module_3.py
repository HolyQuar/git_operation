""" two hooks to let you customize it:
sitecustomize and usercustomize.
"""
# find the location of your user site-packages directory
import site
site_package_dir = site.getusersitepackages()
print('site_package:{}'.format(site_package_dir))

"""sitecustomize works in the same way, 
--but is typically created by an administrator of the computer 
in the global site-packages directory, 
--and is imported before usercustomize. """