import hashlib
import unittest

from day07 import Circuit

class TestSanta(unittest.TestCase):
    def test_it(self):

        circuit = Circuit()
        circuit.set_signal('x', 123)
        self.assertAlmostEqual(circuit.get_signal('x'), 123)

        circuit = Circuit()
        circuit.go('456 -> g')
        self.assertAlmostEqual(circuit.get_signal('g'), 456)

        circuit = Circuit()
        circuit.go('123 -> x')
        circuit.go('456 -> y')
        circuit.go('x AND y -> d')
        circuit.go('x OR y -> e')
        circuit.go('x LSHIFT 2 -> f')
        circuit.go('y RSHIFT 2 -> g')
        circuit.go('NOT x -> h')
        circuit.go('NOT y -> i')
        self.assertAlmostEqual(circuit.get_signal('x'), 123)
        self.assertAlmostEqual(circuit.get_signal('y'), 456)
        self.assertAlmostEqual(circuit.get_signal('d'), 72)
        self.assertAlmostEqual(circuit.get_signal('e'), 507)
        self.assertAlmostEqual(circuit.get_signal('f'), 492)
        self.assertAlmostEqual(circuit.get_signal('g'), 114)
        self.assertAlmostEqual(circuit.get_signal('h'), 65412)
        self.assertAlmostEqual(circuit.get_signal('i'), 65079)


        # circuit.go("123 -> x")

if __name__ == '__main__':
    unittest.main()