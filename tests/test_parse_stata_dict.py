#!/usr/bin/env python3

import unittest
import os
from tests import RESOURCES_DIR
from statadict import parse_stata_dict


stata_dict = parse_stata_dict(file=f"{RESOURCES_DIR}/2017_2019_FemPregSetup.dct")

def test_column_numbers():
    assert 248 == stata_dict.column_numbers[170]

def test_types():
    assert "int" == stata_dict.types[170]

def test_names():
    assert "intvwyear" == stata_dict.names[170]

def test_formats():
    assert "%4f" == stata_dict.formats[170]

def test_comments():
    assert "Calendar year when interview occurred" == stata_dict.comments[170]

def test_widths():
    assert 4 == stata_dict.widths[170]

def test_colspecs():
    assert (247, 251) == stata_dict.colspecs[170]
