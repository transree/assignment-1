from receipt import issued_at


def test_issued_at():
    # 2026-11-01 00:00(日本時間)の時刻
    assert issued_at(1793458800) == "2026-11-01 00:00"
