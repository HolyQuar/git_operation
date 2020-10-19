"""
1.Suppose you want to design a collection of modules (a “package”)
for the uniform handling of sound files and sound data.
    1)you may need to create and maintain a growing collection of modules for the conversion between the various file formats.
    output_formatting_1)There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect),
    so in addition you will be writing a never-ending stream of modules to perform these operations.
output_formatting_1.The __init__.py files are required to make Python treat directories containing the file as packages.
3.Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable.
"""
# sound/effects/__init__.py --> __all__
#__all__ = ["echo", "surround", "reverse"]
# This would mean that from sound.effects import * would import the three named submodules of the sound package.