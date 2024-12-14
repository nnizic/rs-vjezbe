""" funkcija za izračun 
    korištenjem operator 
    modula"""

import operator

operacija: dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "**": pow,  # za kvadriranje, nije iz operator modula
}
