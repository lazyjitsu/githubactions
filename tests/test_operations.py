from src.math_operations import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(1,2)==3
    assert add(4,5)==9


def test_subtract():
    assert subtract(3,2)==1
    assert subtract(-1,1)==0
    assert subtract(4,2)==2
    assert subtract(10,2)==8




