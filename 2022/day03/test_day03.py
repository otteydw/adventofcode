import unittest

from day03 import (
    Rucksack,
    ElfGroup,
    load_from_file,
    sum_rucksack_priorities,
    get_priority,
    sum_group_priorities,
)


class TestSanta(unittest.TestCase):
    def test_get_priority(self):
        self.assertEqual(get_priority("p"), 16)
        self.assertEqual(get_priority("L"), 38)
        self.assertEqual(get_priority("P"), 42)
        self.assertEqual(get_priority("v"), 22)
        self.assertEqual(get_priority("t"), 20)
        self.assertEqual(get_priority("s"), 19)

    def test_rucksack_get_common_item(self):
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

    def test_sum_rucksack_priorities(self):
        input_filename = "example.txt"
        all_rucksacks = load_from_file(input_filename)
        self.assertEqual(sum_rucksack_priorities(all_rucksacks), 157)

    def test_group_get_common_item(self):
        sack1 = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
        sack2 = Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
        sack3 = Rucksack("PmmdzqPrVvPwwTWBwg")
        myGroup = ElfGroup([sack1, sack2, sack3])
        self.assertEqual(myGroup.common_item, "r")

        sack1 = Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
        sack2 = Rucksack("ttgJtRGJQctTZtZT")
        sack3 = Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw")
        myGroup = ElfGroup([sack1, sack2, sack3])
        self.assertEqual(myGroup.common_item, "Z")

    def test_sum_group_priorities(self):
        input_filename = "example.txt"
        all_rucksacks = load_from_file(input_filename)
        self.assertEqual(sum_group_priorities(all_rucksacks), 70)


if __name__ == "__main__":
    unittest.main()
