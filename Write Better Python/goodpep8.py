# RFG: imports at top, always on separate lines
# RFG: unused
# import sys
# import random


# RFG: 4 character indentation
# multiple imports
# RFG: need a space between parameters and a space between return values
# RFG: snake case, not camel case
def foo_bar(arg1, arg2, arg3, arg4):
    # way too much indentation
    return arg1, arg2, arg3, arg4


# RFG: put 2 blank lines between functions
def bar(*args):
    # bad spacing
    return 2 + 2


# RFG: 2 lines between classes and other items
# Bad class name, bad spacing, bad indentation
# RFG class needs capital letter
class Treehouse:
    def one(self):
        return 1

    # RFG: blank line between methods in classes
    def two(self):
        return 2


# RFG: space between items, no space at start of parentheses
# bad identation and whitespace
# RFG: indent final arg to be under 1st arg, or just put args on a new line
# RFG: line length < 79 characters
# RFG: better:
# a, b, c, d = fooBar(
#     "a long string",
#     "a longer string",
#     "yet another long string",
#     "and other crazy string"
#     )


# RFG: also don't use single letter variable names
alpha, beta, charlie, delta = foo_bar(
    "a long string",
    "a longer string",
    "yet another long string",
    "and other crazy string"
    )


# RFG: they don't like aligned = signs.  (I do.)
# bad spacing
one = 1
three = 3

# RFG: 2 spaces before inline comments
fourteen = 14  # make fourteen equal to 12

# RFG: no spaces
# print(a)
print(alpha)
print(fourteen)

print(Treehouse().two())

# import pep8
# checker = pep8.Checker('badpep8.py')
# checker.check_all()
