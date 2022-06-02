import pytest
from code_challenges.insertion_sort import insertion_sort


# @pytest.mark.skip("TODO")
def test_insertion_sort_exists():
  assert insertion_sort

def test_insertion_sorting():
  actual = insertion_sort([4,3,6,21])
  expected = [3,4,6,21]

  assert actual == expected


