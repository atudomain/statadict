#!/usr/bin/env python3

import unittest
from statadict import parse_stata_dict


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.stata_dict = parse_stata_dict(file='resources/2017_2019_FemPregSetup.dct')

    def test_column_numbers(self) -> None:
        self.assertEqual(248, self.stata_dict.column_numbers[170])

    def test_types(self) -> None:
        self.assertEqual("int", self.stata_dict.types[170])

    def test_names(self) -> None:
        self.assertEqual("intvwyear", self.stata_dict.names[170])

    def test_formats(self) -> None:
        self.assertEqual("%4f", self.stata_dict.formats[170])

    def test_comments(self) -> None:
        self.assertEqual("Calendar year when interview occurred", self.stata_dict.comments[170])

    def test_get_colspecs(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
