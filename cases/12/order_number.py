from pathlib import Path

COUNTER = Path(__file__).with_name("counter.txt")


def next_order_number():
    """注文番号を1つ進めて返す。"""
    number = int(COUNTER.read_text()) + 1
    COUNTER.write_text(f"{number}\n")
    return f"A{number:05d}"
