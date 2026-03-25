import vicsek_pkg_example
#from vicsek_pkg_example import Vicsek

def test_main():
    assert(True)

def test_distance():
    assert(vicsek_pkg_example.Vicsek.distance([0,0],[0,0]) == 0)
    assert(vicsek_pkg_example.Vicsek.distance([0,0],[0,1]) == 1)
