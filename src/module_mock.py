from datetime import datetime
import time

def get_current_month() -> int:
    """回傳當下的月份

    Raises:
        Exception: 當月份發生錯誤時，回傳 Exception

    Returns:
        int: 執行當下的月份
    """
    today = datetime.now()

    month = today.month
    if month < 0:
        raise Exception("Wrong month")

    return month

def sleep_for_a_while(seconds: int) -> int:
    """模擬一個需要執行有點久的函數

    Args:
        seconds (int): Pending 時間


    Returns:
        int: 回傳 Pending 秒數
    """
    print("Ready for sleeping!")
    time.sleep(seconds)
    return seconds