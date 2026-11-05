import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", service="standard"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    # ------------------------------------------------------------------
    # Express service
    # ------------------------------------------------------------------
    def test_express_local(self):
        # standard local: 5.0 + 1.5*2 = 8.0  →  express: 8.0 + 7 = 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional: 8.0 + 1.5*2 = 11.0  →  express: 11.0 + 7 = 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_surcharge_is_seven_dollars(self):
        for zone in ("local", "regional"):
            std = shipping_quote(5, zone, service="standard")
            exp = shipping_quote(5, zone, service="express")
            self.assertAlmostEqual(exp - std, 7.0)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(2, "local", service="overnight")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(2, "international")
