import hashlib
import unittest

from day06b import parse_direction, LightGrid

class TestSanta(unittest.TestCase):
    def test_it(self):

        lights = LightGrid()
        self.assertAlmostEqual(lights.count_lit(), 0)

        lights = LightGrid(initial_state=1)
        self.assertAlmostEqual(lights.count_lit(), 1000000)
        self.assertAlmostEqual(lights.get_total_brightness(), 1000000)

        lights = LightGrid(initial_state=5)
        self.assertAlmostEqual(lights.count_lit(), 1000000)
        self.assertAlmostEqual(lights.get_total_brightness(), 5000000)

        lights = LightGrid()
        action, start, end = parse_direction("turn on 0,0 through 999,999")
        lights.act_on_section(action, start, end)
        self.assertAlmostEqual(lights.count_lit(), 1000000)
        self.assertAlmostEqual(lights.get_total_brightness(), 1000000)

        lights = LightGrid()
        action, start, end = parse_direction("turn off 0,0 through 999,999")
        lights.act_on_section(action, start, end)
        self.assertAlmostEqual(lights.count_lit(), 0)
        self.assertAlmostEqual(lights.get_total_brightness(), 0)

        lights = LightGrid(initial_state=1)
        action, start, end = parse_direction("turn off 0,0 through 999,999")
        action, start, end = parse_direction("turn off 0,0 through 999,999")
        action, start, end = parse_direction("turn off 0,0 through 999,999")
        lights.act_on_section(action, start, end)
        self.assertAlmostEqual(lights.count_lit(), 0)
        self.assertAlmostEqual(lights.get_total_brightness(), 0)

        lights = LightGrid()
        action, start, end = parse_direction("turn on 0,0 through 0,0")
        lights.act_on_section(action, start, end)
        self.assertAlmostEqual(lights.count_lit(), 1)
        self.assertAlmostEqual(lights.get_total_brightness(), 1)

        lights = LightGrid()
        action, start, end = parse_direction("turn on 0,0 through 1,1")
        lights.act_on_section(action, start, end)
        self.assertAlmostEqual(lights.count_lit(), 4)
        self.assertAlmostEqual(lights.get_total_brightness(), 4)

        lights = LightGrid()
        action, start, end = parse_direction("turn on 0,0 through 1,0")
        lights.act_on_section(action, start, end)
        self.assertAlmostEqual(lights.count_lit(), 2)
        self.assertAlmostEqual(lights.get_total_brightness(), 2)

        lights = LightGrid()
        action, start, end = parse_direction("toggle 0,0 through 999,0")
        lights.act_on_section(action, start, end)
        self.assertAlmostEqual(lights.count_lit(), 1000)
        self.assertAlmostEqual(lights.get_total_brightness(), 2000)

        # lights = LightGrid(initial_state=1)
        # action, start, end = parse_direction("toggle 0,0 through 999,0")
        # lights.act_on_section(action, start, end)
        # self.assertAlmostEqual(lights.count_lit(), 999000)

        # lights = LightGrid()
        # action, start, end = parse_direction("turn off 499,499 through 500,500")
        # lights.act_on_section(action, start, end)
        # self.assertAlmostEqual(lights.count_lit(), 0)

        # lights = LightGrid(initial_state=1)
        # action, start, end = parse_direction("turn off 499,499 through 500,500")
        # lights.act_on_section(action, start, end)
        # self.assertAlmostEqual(lights.count_lit(), 999996)

        # lights = LightGrid(initial_state=1)
        # action, start, end = parse_direction("toggle 0,0 through 999,0")
        # lights.act_on_section(action, start, end)
        # action, start, end = parse_direction("turn off 499,499 through 500,500")
        # lights.act_on_section(action, start, end)
        # self.assertAlmostEqual(lights.count_lit(), 998996)

        # lights = LightGrid()
        # action, start, end = parse_direction("turn on 999,0 through 999,999")
        # lights.act_on_section(action, start, end)
        # self.assertAlmostEqual(lights.count_lit(), 1000)

        # lights = LightGrid()
        # action, start, end = parse_direction("turn on 0,0 through 999,0")
        # lights.act_on_section(action, start, end)
        # self.assertAlmostEqual(lights.count_lit(), 1000)

if __name__ == '__main__':
    unittest.main()