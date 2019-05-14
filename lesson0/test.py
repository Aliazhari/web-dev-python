# Author: Ali Azhari
# Code for setting the style of the notebook

from IPython.core.display import HTML

def css_styling():
    styles = open("test.css", "r").read()
    return HTML(styles)

print(css_styling().data)