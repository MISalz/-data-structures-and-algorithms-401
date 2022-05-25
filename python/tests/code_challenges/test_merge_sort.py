
from code_challenges.merge_sort import merge_sort
import pytest


def test_merge_sort_exists():
    assert merge_sort


def test_short_list():
    test_list = [5, 6, 4, 7]
    actual = merge_sort(test_list)
    expected = [4, 5, 6, 7]
    assert actual == expected
