"""Encode Hofstadter's formal pq system"""
import re

class pq(object):
    """format for working with string bound by pq rules"""

    def __init__(self, inputstring: str):
        """initialize string, validate it is an axiom"""
        if re.search("-*p-+q-+", inputstring):
            self.inputstring = inputstring
        else:
            raise ValueError

    def