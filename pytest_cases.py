import pytest

# def test_compare():
#     value=10
#     assert 10==value
#
# def test_compare2():
#     value="durga"
#     assert "nagadurga"==value

import pytest
import main
a=10
b=0

def test_add():
    result=main.add(a,b)
    assert 10==result

def test_add_strings():
    result=main.add("naga ","durga")
    assert "naga durga"== result

# def test_divide():
#     result=main.divide(a,b)
#     assert 10==result

def test_mul():
    result=main.mul(a,b)
    assert 0==result

def test_sub():
    result=main.sub(a,b)
    assert 10==result

# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError):
#        main.divide(a,b)

def test_divide_by_zero():
    with pytest.raises(ValueError):
       main.divide(a,b)



