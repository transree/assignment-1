import os


def fee(method):
    """支払い方法ごとの手数料(円)を返す。"""
    return {"card": 0, "bank": 220, "cod": 330}[method]


def charge(amount, method):
    """決済サービスに請求する金額を返す。テスト環境の URL がないと使えない。"""
    if not os.environ.get("PAYMENT_SANDBOX_URL"):
        raise RuntimeError("PAYMENT_SANDBOX_URL が設定されていません")
    return amount + fee(method) if method != "cod" else amount
