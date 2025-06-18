from collections import defaultdict
from functools import reduce
from itertools import combinations

type Pair[V] = tuple[V, ...]  # V must support: __add__, __lt__, __eq__, __hash__
type Sum[S] = S  # Sum is a type alias for the sum value, which can be a type that supports addition.


class SumPairs[V](defaultdict[Sum[V], set[Pair[V]]]):
    """
    A class to store pairs of integers that sum to the same value.
    """

    def __init__(self, *args, **kwargs):
        # Initialize the defaultdict with 'set' as the default factory
        super().__init__(set, *args, **kwargs)

    def add_pair(self, sum_value: V, pair: Pair[V]) -> None:
        # Sort the pair to ensure that only unique pairs are stored.
        # Otherwise, we could end up with (a, b) and (b, a) as different pairs.
        self[sum_value].add(tuple(sorted(pair)))

    def clean(self) -> None:
        """
        Modify the SumPairs object in place: remove sums that have less than two pairs.
        """
        items_to_keep = {sum_value: pairs for sum_value, pairs in self.items() if len(pairs) > 1}
        self.clear()
        self.update(items_to_keep)

    def __str__(self) -> str:
        """
        For the purposes of pretty formatting:

        * Sort sums (keys) by the sum value.
        * Sort pairs (values) by the first element of the pair.
        """
        data_to_print = {sum_value: sorted(pairs) for sum_value, pairs in sorted(self.items())}
        return "\n".join(
            f"Pairs: {', '.join(map(str, pairs))} have sum {sum_value}" for sum_value, pairs in data_to_print.items()
        )


def find_n_pairs[V](items: list[V], n: int) -> SumPairs[V]:
    if n < 2:
        raise ValueError("n must be at least 2")
    com = combinations(items, n)
    result = SumPairs()
    for c in com:
        init_value = c[0]
        sum_values = reduce((lambda x, y: x + y), c[1:], init_value)
        result.add_pair(sum_values, c)
    result.clean()
    return result


def find_pairs[V](items: list[V]) -> SumPairs[V]:
    """
    Find all unique pairs of items in the input list that sum to the same value.
    Returns a SumPairs object containing the pairs grouped by their sum.

    :param items: List of items to find pairs in.
    The items must support addition, comparison, and be hashable (e.g., integers, floats, strings).
    :return: SumPairs object containing pairs grouped by their sum.

    Example:
    >>> pairs = find_pairs([1, 2, 3, 4])
    >>> print(pairs)
    Pairs: (1, 4), (2, 3) have sum 5
    """
    return find_n_pairs(items, 2)
