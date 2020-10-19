"""The textwrap module formats paragraphs of text to fit a given screen width
"""
import textwrap

doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
fill_doc = textwrap.fill(doc, width=40)
print('fill_doc:\n{}'.format(fill_doc))
