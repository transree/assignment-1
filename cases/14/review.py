def average(stars):
    """レビューの星の平均(小数第1位で四捨五入)を返す。レビューがなければ0。"""
    if not stars:
        return 0
    return round(sum(stars) / len(stars), 1)


def label(avg):
    return "高評価" if avg > 4.0 else "通常"
