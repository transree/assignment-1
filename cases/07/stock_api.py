import time


def fetch_stock(item_id):
    """在庫の API に問い合わせる(この練習では、応答が返らない状態を時間待ちで再現している)。"""
    time.sleep(900)
    return 0


def is_low(stock):
    """在庫が少ない(5個以下)かを返す。"""
    return stock < 5
