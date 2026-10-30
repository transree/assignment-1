import random

# 準備中の枠は空の名前にしている
CAMPAIGNS = ["秋のセール", "送料無料キャンペーン", "", ""]


def pick_campaign():
    """トップページに出すキャンペーン名を1つ選ぶ。"""
    return random.choice(CAMPAIGNS)
