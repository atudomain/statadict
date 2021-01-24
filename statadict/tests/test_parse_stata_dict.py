#!/usr/bin/env python3

import unittest
import os
from statadict import parse_stata_dict


class Test(unittest.TestCase):
    RESOURCES_DIR = os.path.dirname(os.path.realpath("__file__")) + "/resources/"

    def setUp(self) -> None:
        self.stata_dict = parse_stata_dict(file=f"{self.RESOURCES_DIR}2017_2019_FemPregSetup.dct")

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

    def test_widths(self) -> None:
        self.assertEqual(4, self.stata_dict.widths[170])

    def test_colspecs(self) -> None:
        self.assertEqual((247, 251), self.stata_dict.colspecs[170])


if __name__ == '__main__':
    unittest.main()
