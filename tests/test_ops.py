from src.math_ops import add, sub

def test_add():
    assert add(2, 3)==5
    assert add(2, 5)==7

def test_sub():
    assert sub(4, 2)==2
    assert sub(3, 4)==-1
    assert sub(3, 3)==0