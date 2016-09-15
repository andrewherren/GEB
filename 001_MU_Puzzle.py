"""Chapter 1: The MU Puzzle"""


class MUpuzzle(object):
    """Creates an string bound by the rules of the MU logic system

    MU system based on formal system laid out by Emil Post
    https://en.wikipedia.org/wiki/Post_canonical_system
    """
    inputstring = ''

    def __init__(self, inputstring: str):
        """Initialize MU puzzle object
        Only accept strings consisting of 'I', 'M', 'U'

        :type inputstring: str
        """
        if all(item in ['I', 'M', 'U'] for item in sorted(set(inputstring))):
            self.inputstring = inputstring
        else:
            raise ValueError

    def __repr__(self):
        """call to repr() function"""
        return self.inputstring

    def __str__(self):
        """pretty-print puzzle string"""
        return self.inputstring

    def rule1(self):
        """Applies rule 1 of the MU system:
        If string's last letter is "I" can add a "U" at end

        :return: str
        """
        if self.inputstring.endswith('I'):
            self.inputstring += 'U'
        return self.inputstring

    def rule2(self):
        """Applies rule 2 of the MU system:
        Suppose you have Mx. Then you may add Mxx to your collection

        :return: inputstring
        """
        if self.inputstring.startswith('M'):
            self.inputstring += self.inputstring[1:]
        return self.inputstring

    def rule3(self):
        """Applies rule 3 of the MU system:
        If III occurs in one of the strings in your collection,
        you may make a new string with U in place of III

        :return: inputstring
        """
        if self.inputstring.find('III'):
            print("yes, successfully found")
            self.inputstring = self.inputstring.replace('III', 'U')
        return self.inputstring

    def rule4(self):
        """Applies rule 4 of the MU system:
        If UU occurs inside one of your strings, you can drop it

        :return: inputstring
        """
        if self.inputstring.find('UU'):
            print("yes, successfully found")
            self.inputstring = self.inputstring.replace('UU', '')
        return self.inputstring

# Hoftstadter's derivation of MUIIU
# taking MI as an axiom
puzzle1 = MUpuzzle('MI')
puzzle1.rule2()
puzzle1.rule2()
puzzle1.rule1()
puzzle1.rule3()
puzzle1.rule2()
puzzle1.rule4()
print(puzzle1) # MUIIU

