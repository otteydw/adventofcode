import unittest

from day03 import Rucksack, load_from_file, sum_rucksack_priorities


class TestSanta(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_common_item(self):
        mySack = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
        self.assertEqual(mySack.common_item, "p")
        mySack = Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
        self.assertEqual(mySack.common_item, "L")
        mySack = Rucksack("PmmdzqPrVvPwwTWBwg")
        self.assertEqual(mySack.common_item, "P")
        mySack = Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
        self.assertEqual(mySack.common_item, "v")
        mySack = Rucksack("ttgJtRGJQctTZtZT")
        self.assertEqual(mySack.common_item, "t")
        mySack = Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw")
        self.assertEqual(mySack.common_item, "s")

    def test_get_priority(self):
        mySack = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
        self.assertEqual(mySack.priority, 16)
        mySack = Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
        self.assertEqual(mySack.priority, 38)
        mySack = Rucksack("PmmdzqPrVvPwwTWBwg")
        self.assertEqual(mySack.priority, 42)
        mySack = Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
        self.assertEqual(mySack.priority, 22)
        mySack = Rucksack("ttgJtRGJQctTZtZT")
        self.assertEqual(mySack.priority, 20)
        mySack = Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw")
        self.assertEqual(mySack.priority, 19)

    def test_sum_rucksack_priorities(self):
        input_filename = "example.txt"
        all_rucksacks = load_from_file(input_filename)
        self.assertEqual(sum_rucksack_priorities(all_rucksacks), 157)


if __name__ == "__main__":
    unittest.main()
