"""Test case for Roman numerals"""

#Standard library

#3rd party library
import pytest

#Project library
from numeral.roman import to_roman



def Test_calling_function():
    """Call Roman function"""



@pytest.mark.parametrize(
    "arabic_num, roman_num",
    [
# Base case
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),

        # Addition case
        (2, "II"),
        (3, "III"),
        (6, "VI"),

        # Subtraction case
        (4, "IV"),
        (9, "IX"),
        
        # Mixed case
        (24, "XXIV"),
        (42, "XLII"),

        # Unit case
        (8, "VIII"),
        
        # Ten case
        (11, "XI"),
        (95, "XCV"),

        # Hundreds case
        (100, "C"),
        (101, "CI"),
        (110, "CX"),

        # Boundary case
        (3888, "MMMDCCCLXXXVIII"),
        
    ]
)

def test_to_roman(arabic_num, roman_num):
    """Convert number to roman"""
    
    # Arrange
    
    
    # Act
    result = to_roman(arabic_num)
    
    # Assert
    assert result == roman_num
    