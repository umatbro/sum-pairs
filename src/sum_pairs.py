from collections import defaultdict
from collections.abc import Collection
from collections.abc import Iterable

# type aliases
Sum = int
Pair = tuple[int, int]


class SumPairs:
    def __init__(self):
        super().__init__()
        self._pairs: dict[Sum, set[Pair]] = defaultdict(set)

    def add_pair(self, sum_value: Sum, pair: Pair):
        self._pairs[sum_value].add(tuple(sorted(pair)))

    def clean(self) -> None:
        """
        Remove sums that have less than two pairs.
        """
        self._pairs = {k: v for k, v in self._pairs.items() if len(v) > 1}

    def asdict(self) -> dict[Sum, Collection[Pair]]:
        """
        Returns a dictionary representation of the sum pairs.
        """
        return self._pairs

    def __iter__(self) -> Iterable[tuple[Sum, Collection[Pair]]]:
        return iter(self._pairs.items())

    def __eq__(self, other: dict[Sum, Collection[Pair]]) -> bool:
        if not isinstance(other, dict):
            raise TypeError("Comparison is only supported with a dictionary.")
        if len(self._pairs) != len(other):
            return False
        for sum_, pairs in self._pairs.items():
            if sum_ not in other or pairs != set(other[sum_]):
                return False
        return True

    def __str__(self) -> str:
        """
        For the purposes of pretty formatting:

        * Sort pairs in each sum by the first element of the pair.
        * Sort sums by the sum value.
        """
        data_to_print = {sum_value: sorted(pairs) for sum_value, pairs in sorted(self._pairs.items())}
        return "\n".join(
            f"Pairs: {', '.join(map(str, pairs))} have sum {sum_value}" for sum_value, pairs in data_to_print.items()
        )


def find_pairs(input: list[int]) -> SumPairs:
    result = SumPairs()
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            pair_sum = input[i] + input[j]
            result.add_pair(pair_sum, (input[i], input[j]))
    result.clean()
    return result
