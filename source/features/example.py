#!/usr/bin/env python

"""Example module.
"""

import os

class MyClass(object):
    """This is a simple class.

    This module illustrates three features of Sphinx:
    
    1. Pygments integration.
    2. Auto-doc features.
    3. Use of rst in docstrings.
    """
    
    def __init__(self, arg1):
        """Initialize MyClass instance.
        
        arg1
          Provide a value for the argument.
        """
        self.arg1 = arg1
    
    def another_method(self):
        """Returns something.
        """
        return self.arg1 * 2

    def method_with_arguments(self, a, b):
        """This method takes arguments.

        :param a: The first argument.
        :type a: int
        :param b: The second argument.
        :type b: str
        """
        return (self.arg1 * a) + b

def main():
    o = MyClass('foo ')
    print o.another_method()
