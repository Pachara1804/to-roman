# roman.py

class NumberOutOfRange(ValueError):
    """An extension to the standard ValueError exception."""

def to_roman(arabic_num):
    """Converts Hindo-Arabic number to Roman number."""
    if not 1 <= arabic_num <= 3888:
        raise NumberOutOfRange("Number out of range (1 to 3888)")

    roman_numeral = ""
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

    for numeral, value in roman_numerals:
        while arabic_num >= value:
            roman_numeral += numeral
            arabic_num -= value

    return roman_numeral
