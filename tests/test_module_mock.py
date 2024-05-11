from unittest.mock import patch
from src.module_mock import get_current_month
from datetime import datetime
from src.module_mock import sleep_for_a_while
import time

def test_get_current_month():
    with patch("src.module_mock.datetime") as mock_datetime: 
        # 執行測試時將 datetime.now 的 return value 設定為固定的值
        mock_datetime.now.return_value = datetime(2023, 3, 1, 0, 0, 0)
        month = get_current_month()
        # 因為 datetime.now() 的值被固定下來了，這邊可以設定固定的條件值
        # 如果 Assertion 發生錯誤，就代表
        # 程式的邏輯發生問題了! 跟 datetime.now() 無關!
        assert month == 3

# def test_sleep_for_a_while(): # 錯誤用法，這一個測試案例將需要花費 20 秒時間等待
#     response = sleep_for_a_while(20)
#     assert response==20

def test_sleep_for_a_while_mock(): # 用法 1 
    # 使用 patch 將 time.sleep() 函數替換為 None 物件
    with patch("src.module_mock.time.sleep"): 
        response = sleep_for_a_while(20)
        assert response==20

def test_sleep_for_a_while_replace(): # 用法 2
    # 使用 patch 將 time.sleep() 函數替換為 time.sleep(2)
    with patch("src.module_mock.time.sleep", new_callable=time.sleep(2)):
        response = sleep_for_a_while(20)
        assert response==20