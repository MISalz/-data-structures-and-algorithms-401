import pytest
from code_challenges.roman_numerals import convert_character, roman_to_numerals

def test_convert_exists():
  assert convert_character

def test_convert_exists():
  assert roman_to_numerals

def test_check_test_convert_success():
  roman_test = roman_to_numerals('CXLII')
  assert str(roman_test) == '142'

def test_check_test_convert_year():
  roman_test = roman_to_numerals('MCMLXXIV')
  assert str(roman_test) == '1974'

def test_check_test_duplicate():
  roman_test = roman_to_numerals('MDCCLXXIV')
  assert str(roman_test) == '1774'


def test_check_test_one_digit():
  roman_test = roman_to_numerals('X')
  assert str(roman_test) == '10'

def test_check_test_one_digit():
  roman_test = roman_to_numerals(str.upper('x'))
  assert str(roman_test) == '10'
