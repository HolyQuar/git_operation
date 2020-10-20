"""Surrounding the placeholder with braces allows it
-to be followed by more alphanumeric letters with no intervening spaces.
-Writing $$ creates a single escaped $
"""
from string import Template

t = Template('${village} folk send $$10 to $cause')
# subclass
signment_value = t.substitute(village='Nottingham', cause='the ditch fund')
print('signment_value:{}'.format(signment_value))
print('-----------------------')
# The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword argument.

t1 = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# raise KeyError
new_str=t1.substitute(d)
# don't raise KeyError and unchange the '$owner'.
new_str=t1.safe_substitute(d)
print('new_str:{}'.format(new_str))