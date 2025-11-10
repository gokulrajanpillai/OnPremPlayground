# Execute by running pytest -q
import pytest
from file import avg

@pytest.mark.parameterize(
  "nums, expected",
  [
    ([1,2,3], 2.0),
    ([], None)
  ],
  ids=["ints", "empty"]
)

def test_avg_param(nums, expected):
  assert avg(nums) == expected

def test_avg():
  assert avg([1,2,3]) == 2.0

def test_avg_empty():
  assert avg([]) == None
