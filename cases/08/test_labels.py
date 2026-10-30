import pytest

from labels import shipping_label


@pytest.mark.parametrize("order_id", range(1, 301))
def test_label(order_id):
    expected = "\n".join(
        [f"注文番号: {order_id}", "お届け先: 山田 太郎 様", "住所: 東京都千代田区丸の内1-1-1"]
    ) + "\n" + "=" * 40 + "\n" + ("ご注文ありがとうございました。" * 20)
    assert shipping_label(order_id, "山田 太郎", "東京都千代田区丸の内1-1-1") == expected
