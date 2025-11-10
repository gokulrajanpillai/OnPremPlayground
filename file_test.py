# Execute by running pytest -q

from file import avg

def test_avg():
  assert avg([1,2,3]) == 2.0

def test_avg_empty():
  assert avg([]) == None
