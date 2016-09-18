"""Encode Hofstadter's formal tq system"""
import re


class TQ(object):
    """format for working with string bound by tq rules"""

    def __init__(self, inputstring: str):
        """initialize string, validate it is an axiom"""
        if re.search("-*t-*q-*", inputstring):
            # split regex along p and q lines
            resplit = re.split("t|q", inputstring)
            # check is balance between "-" on either side of t and after q
            if len(resplit[0]) * len(resplit[1]) == len(resplit[2]):
                self.inputstring = inputstring
            # do not initialize class if not valid under tq system
            else:
                raise ValueError
        # do not initialize class if not valid under tq system
        else:
            raise ValueError

    def __str__(self):
        """return inputstring with object printed in console"""
        return self.inputstring

    def increment(self):
        """update the string according to rule:

        Suppose x, y, and z all stand for particular strings containing only
        hyphens. And suppose that xtyqz is known to be a theorem. Then xty-qzx
        is a theorem.
        """
        resplit = re.split("t|q", self.inputstring)
        self.inputstring = resplit[0] + 't' + resplit[1] + '-q' + resplit[2] + "-" * len(resplit[0])

testTQ = TQ('---t--q------')
testTQ.increment()
testTQ.increment()
testTQ.increment()
print(testTQ) # ---t-----q---------------