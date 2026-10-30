from campaign import pick_campaign


def test_name_is_not_empty():
    assert pick_campaign() != ""


def test_name_is_known():
    assert pick_campaign() in ["秋のセール", "送料無料キャンペーン", ""]
