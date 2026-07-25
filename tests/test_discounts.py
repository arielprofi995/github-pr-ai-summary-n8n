from decimal import Decimal

import pytest

from src.discounts import apply_discount


def test_apply_discount() -> None:
    result = apply_discount(
        Decimal("100.00"),
        Decimal("15"),
    )

    assert result == Decimal("85.00")


def test_zero_discount() -> None:
    result = apply_discount(
        Decimal("49.99"),
        Decimal("0"),
    )

    assert result == Decimal("49.99")


def test_rejects_discount_above_one_hundred() -> None:
    with pytest.raises(
        ValueError,
        match="Discount percent must be between 0 and 100",
    ):
        apply_discount(
            Decimal("100.00"),
            Decimal("120"),
        )


def test_rejects_negative_price() -> None:
    with pytest.raises(
        ValueError,
        match="Price cannot be negative",
    ):
        apply_discount(
            Decimal("-10.00"),
            Decimal("10"),
        )
