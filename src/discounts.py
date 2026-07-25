from decimal import Decimal


def apply_discount(
    price: Decimal,
    discount_percent: Decimal,
) -> Decimal:
    """Calculate the price after applying a percentage discount."""

    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")

    multiplier = Decimal("1") - discount_percent / Decimal("100")
    return (price * multiplier).quantize(Decimal("0.01"))
