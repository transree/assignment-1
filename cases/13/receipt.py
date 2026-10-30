import time


def issued_at(timestamp):
    """レシートの発行日時の表示を返す。"""
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(timestamp))
