import unittest

from .day07 import Circuit


class TestSanta(unittest.TestCase):
    def test_set_signal(self):

        circuit = Circuit()
        circuit.set_signal("x", 123)
        self.assertAlmostEqual(circuit.get_signal("x"), 123)

    def test_store_direction_numeric(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("456 -> y")
        self.assertAlmostEqual(circuit.get_signal("x"), 123)
        self.assertAlmostEqual(circuit.get_signal("y"), 456)

    def test_and(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("456 -> y")
        circuit.store_direction("x AND y -> d")
        self.assertAlmostEqual(circuit.get_signal("d"), 72)

    def test_or(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("456 -> y")
        circuit.store_direction("x OR y -> e")
        self.assertAlmostEqual(circuit.get_signal("e"), 507)

    def test_lshift(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("456 -> y")
        circuit.store_direction("x LSHIFT 2 -> f")
        self.assertAlmostEqual(circuit.get_signal("f"), 492)

    def test_rshift(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("456 -> y")
        circuit.store_direction("y RSHIFT 2 -> g")
        self.assertAlmostEqual(circuit.get_signal("g"), 114)

    def test_not(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("456 -> y")
        circuit.store_direction("NOT x -> h")
        circuit.store_direction("NOT y -> i")
        self.assertAlmostEqual(circuit.get_signal("h"), 65412)
        self.assertAlmostEqual(circuit.get_signal("i"), 65079)

    def test_out_of_order(self):
        circuit = Circuit()
        circuit.store_direction("x AND y -> d")
        circuit.store_direction("y RSHIFT 2 -> g")
        circuit.store_direction("NOT x -> h")
        circuit.store_direction("x LSHIFT 2 -> f")
        circuit.store_direction("NOT y -> i")
        circuit.store_direction("123 -> x")
        circuit.store_direction("x OR y -> e")
        circuit.store_direction("456 -> y")
        self.assertAlmostEqual(circuit.get_signal("x"), 123)
        self.assertAlmostEqual(circuit.get_signal("y"), 456)
        self.assertAlmostEqual(circuit.get_signal("d"), 72)
        self.assertAlmostEqual(circuit.get_signal("e"), 507)
        self.assertAlmostEqual(circuit.get_signal("f"), 492)
        self.assertAlmostEqual(circuit.get_signal("g"), 114)
        self.assertAlmostEqual(circuit.get_signal("h"), 65412)
        self.assertAlmostEqual(circuit.get_signal("i"), 65079)

    def test_wire_assignment(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("x -> y")
        self.assertAlmostEqual(circuit.get_signal("x"), 123)
        self.assertAlmostEqual(circuit.get_signal("y"), 123)

    def test_integers_and(self):
        circuit = Circuit()
        circuit.store_direction("123 -> x")
        circuit.store_direction("x AND 456 -> y")
        circuit.store_direction("456 AND x -> z")
        self.assertAlmostEqual(circuit.get_signal("y"), 72)
        self.assertAlmostEqual(circuit.get_signal("z"), 72)


if __name__ == "__main__":
    unittest.main()
