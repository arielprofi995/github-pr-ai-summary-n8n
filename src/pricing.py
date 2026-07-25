"""Funkcje odpowiedzialne za obliczanie wartości zamówienia."""

from decimal import Decimal, ROUND_HALF_UP


def calculate_total(subtotal: float, tax_rate: float = 0.23) -> float:
    """
    Oblicza wartość zamówienia po doliczeniu podatku.

    Args:
        subtotal: Wartość zamówienia netto.
        tax_rate: Stawka podatku zapisana jako ułamek, np. 0.23.

    Returns:
        Wartość zamówienia brutto zaokrąglona do dwóch miejsc.

    Raises:
        ValueError: Gdy wartość zamówienia lub stawka podatku jest ujemna.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    subtotal_decimal = Decimal(str(subtotal))
    tax_decimal = Decimal(str(tax_rate))

    total = subtotal_decimal * (Decimal("1") + tax_decimal)

    return float(
        total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    )
