import pytest
from src.module_a import square, concat

def test_square():
    assert square(8) == 64

def test_concat():
    str_1 = "Hello! "
    str_2 = "MingLun!"
    assert concat(str_1=str_1, str_2=str_2) == "Hello! MingLun!"

def test_concat_failed():
    str_1 = 555 # Error Type
    str_2 = 666 # Error Type
    with pytest.raises(TypeError): # 以下範圍內的程式碼應該要拋出 Type Error
        concat(str_1=str_1, str_2=str_2)