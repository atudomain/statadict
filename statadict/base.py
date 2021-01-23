#!/usr/bin/env python3

from typing import List
from collections import deque
import re


class StataDict:
    def __init__(
            self,
            column_numbers: List[int],
            types: List[str],
            names: List[str],
            formats: List[str],
            comments: List[str],
    ):
        self._column_numbers = column_numbers
        self._types = types
        self._names = names
        self._formats = formats
        self._comments = comments

    @property
    def column_numbers(self) -> List[int]:
        return self._column_numbers

    @property
    def types(self) -> list:
        return self._types

    @property
    def names(self) -> list:
        return self._names

    @property
    def formats(self) -> list:
        return self._formats

    @property
    def comments(self) -> list:
        return self._comments

    def get_colspecs(self) -> List[tuple]:
        raise NotImplementedError


class StataDictParser:
    _COLUMN_PATTERN = r'^\s+_column'
    _LINE_PATTERN = r'^\s+_column\((\d+)\)\s+(\S+)\s+(\S+)\s+(\S+)\s+(".*")?'

    def parse(self, file) -> StataDict:
        column_numbers = deque()
        types = deque()
        names = deque()
        formats = deque()
        comments = deque()
        with open(file, "r") as dct_file:
            for line in dct_file:
                if re.search(self._COLUMN_PATTERN, line):
                    line_values = re.findall(self._LINE_PATTERN, line)
                    column_numbers.append(int(line_values[0][0]))
                    types.append(line_values[0][1])
                    names.append(line_values[0][2])
                    formats.append(line_values[0][3])
                    if len(line_values[0]) == 5:
                        comments.append(line_values[0][4].lstrip('"').rstrip('"'))
                    else:
                        comments.append(None)
        return StataDict(
            column_numbers=list(column_numbers),
            types=list(types),
            names=list(names),
            formats=list(formats),
            comments=list(comments)
        )


def parse_stata_dict(file: str) -> StataDict:
    stata_dict_parser = StataDictParser()
    return stata_dict_parser.parse(file)
