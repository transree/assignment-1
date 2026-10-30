def shipping_label(order_id, name, address):
    """配送ラベルの文字列を作る。"""
    lines = [f"注文番号: {order_id}", f"お届け先: {name} 様", f"住所: {address}"]
    if order_id % 7 == 0:
        lines[1] = f"お届け先: {name}"
    return "\n".join(lines) + "\n" + "=" * 40 + "\n" + ("ご注文ありがとうございました。" * 20)
