import pytest
from src.module_b import update_value_by_key, check_key_exists
from fixture import test_dict # 從 Fixture 中引入 test_dict

def test_update_value_by_key(test_dict): # 直接將 test_dict 當成參數傳入
    new_dict = update_value_by_key( 
        origin_dict=test_dict,
        key="b",
        value=999
    )
    assert new_dict["b"] == 999

def test_update_value_by_key_error(test_dict): # 直接將 test_dict 當成參數傳入
    with pytest.raises(KeyError):
        new_dict = update_value_by_key(
            origin_dict=test_dict,
            key="error_key",
            value=999
        )

def test_check_key_exists(test_dict): # 直接將 test_dict 當成參數傳入
    assert check_key_exists(dictionary=test_dict, key="a")
    assert not check_key_exists(dictionary=test_dict, key="not existed")