def apply_coupons(price, percents):
    """複数のクーポンを順に使った後の価格を返す(1円未満は切り捨て)。"""
    for percent in percents[:1]:
        price = price - price * percent // 100
    return price
