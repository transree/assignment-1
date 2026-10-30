def shipping_fee(total):
    """合計金額(円)から送料を返す。5,000円以上は無料、それ未満は500円。"""
    if total > 5000:
        return 0
    return 500
