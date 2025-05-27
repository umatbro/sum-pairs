from dataclasses import dataclass
from typing import Self

import pytest

from sum_pairs import SumPairs
from sum_pairs import find_pairs


@dataclass
class Point:
    """
    A simple class to represent a point in 2D space
    and test `find_pairs` with custom objects.
    """

    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __lt__(self, other: Self) -> bool:
        return (self.x, self.y) < (other.x, other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


@pytest.mark.parametrize(
    ("input", "expected_result"),
    [
        # test case from example #1
        (
            [6, 4, 12, 10, 22, 54, 32, 42, 21, 11],
            {
                16: {(4, 12), (6, 10)},
                32: {(10, 22), (11, 21)},
                33: {(12, 21), (11, 22)},
                43: {(21, 22), (11, 32)},
                53: {(21, 32), (11, 42)},
                54: {(12, 42), (22, 32)},
                64: {(10, 54), (22, 42)},
            },
        ),
        # test case from example #2
        ([4, 23, 65, 67, 24, 12, 86], {90: {(4, 86), (23, 67)}}),
        # test case with multiple duplicate pairs
        (
            [2, 2, 0, 4, 4, 2, 6, 6],
            {
                4: {(2, 2), (0, 4)},
                6: {(2, 4), (0, 6)},
                8: {(2, 6), (4, 4)},
            },
        ),
        # test case with no pairs
        ([1, 2, 3], {}),
        # test case with all unique pairs
        ([1, 2, 3, 4], {5: {(1, 4), (2, 3)}}),
        # test case empty input
        ([], {}),
        # test case with negative numbers
        ([-1, -2, -3, -4], {-5: {(-4, -1), (-3, -2)}}),
        # test case with mixed positive and negative numbers
        ([1, -1, 2, -2], {0: {(-1, 1), (-2, 2)}}),
        # test case with repeating numbers
        ([5, 5, 5, 5], {}),  # result is empty because there is no more than one unique pair
        # test case with duplicate number that can form pairs
        ([5, 2, 8, 5, 3, 7], {10: {(2, 8), (3, 7), (5, 5)}}),
        # test case with strings
        (
            ["a", "b", "ab", "c", "bc", ""],
            {"bc": {("b", "c"), ("", "bc")}, "abc": {("a", "bc"), ("ab", "c")}, "ab": {("a", "b"), ("", "ab")}},
        ),
        # test case with floats
        ([1.5, 2.5, 3.5, 4.5], {6.0: {(1.5, 4.5), (2.5, 3.5)}}),
        # test case with Point objects
        (
            [Point(1, 2), Point(0, 0), Point(1, 1), Point(2, 3)],
            {
                Point(2, 3): {(Point(0, 0), Point(2, 3)), (Point(1, 1), Point(1, 2))},
            },
        ),
    ],
)
def test_find_unique_pairs[V](input: list[V], expected_result: dict[V, list[tuple[V, V]]]):
    result = find_pairs(input)
    assert result == expected_result, f"Expected {expected_result}, got {result}"


def test_sum_pairs_str():
    obj = SumPairs()
    obj.add_pair(20, (10, 10))
    obj.add_pair(20, (7, 13))
    obj.add_pair(10, (1, 9))
    obj.add_pair(10, (2, 8))
    obj.add_pair(20, (10, 10))  # Duplicate pair
    obj.add_pair(20, (15, 5))
    obj.add_pair(30, (15, 15))
    obj.clean()

    expected_str = "\n".join(
        [
            "Pairs: (1, 9), (2, 8) have sum 10",
            "Pairs: (5, 15), (7, 13), (10, 10) have sum 20",
        ]
    )
    assert str(obj) == expected_str, f"Expected {expected_str}, got {str(obj)}"
