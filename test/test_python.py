from vicsek_pkg_example.example import distance
import numpy as np

def test_main():
    assert(True)

def test_distance():
    assert(distance(np.array([0,0]), np.array([0,0])) == 0)
    assert(distance(np.array([0,0]), np.array([0,1])) == 1)
