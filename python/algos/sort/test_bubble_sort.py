import numpy as np
from .bubble_sort import bubble_sort
from toolspy import is_sorted

def test_random_numpy_list():
    l = np.random.randint(10000, size=100)
    sl = bubble_sort(l)
    assert is_sorted(sl)

