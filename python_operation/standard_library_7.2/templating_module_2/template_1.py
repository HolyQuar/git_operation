"""Surrounding the placeholder with braces allows it
-to be followed by more alphanumeric letters with no intervening spaces.
-Writing $$ creates a single escaped $
"""
from string import Template

t = Template('${village} folk send $$10 to $cause')
# subclass
signment_value = t.substitute(village='Nottingham', cause='the ditch fund')
print('signment_value:{}'.format(signment_value))
from abc import ABCMeta