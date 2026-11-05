"""Shipping rate calculations."""

_EXPRESS_SURCHARGE = 7.0


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping cost in dollars.

    Parameters
    ----------
    weight_kg:
        Parcel weight; must be positive.
    zone:
        Delivery zone – ``"local"`` or ``"regional"``.
    service:
        Shipping service level – ``"standard"`` (default) or ``"express"``.
        Express adds a flat $7.00 surcharge on top of the standard rate.

    Raises
    ------
    ValueError
        If *weight_kg* is not positive, *zone* is unknown, or *service* is
        unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in {"standard", "express"}:
        raise ValueError("unknown service")
    base = 5.0 if zone == "local" else 8.0
    quote = base + 1.5 * weight_kg
    if service == "express":
        quote += _EXPRESS_SURCHARGE
    return round(quote, 2)
