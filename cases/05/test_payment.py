import os

import pytest

from payment import charge, fee

needs_sandbox = pytest.mark.skipif(
    not os.environ.get("PAYMENT_SANDBOX_URL"), reason="決済のテスト環境の設定がないので実行しない"
)


def test_fee_card():
    assert fee("card") == 0


@needs_sandbox
def test_charge_card():
    assert charge(1000, "card") == 1000


@needs_sandbox
def test_charge_bank():
    assert charge(1000, "bank") == 1220


@needs_sandbox
def test_charge_cod():
    assert charge(1000, "cod") == 1330


@needs_sandbox
def test_charge_large():
    assert charge(100000, "bank") == 100220


@needs_sandbox
def test_charge_zero():
    assert charge(0, "card") == 0
