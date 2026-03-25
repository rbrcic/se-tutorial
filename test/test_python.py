def test_main():
    assert(True)

def test_distance():
    assert(Vicsek.distance([0,0],[0,0]) == 0)
    assert(Vicsek.distance([0,0],[0,1])) == 1)
