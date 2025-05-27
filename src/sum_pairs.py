from collections import defaultdict

# type aliases
Sum = int
Pair = tuple[int, int]


class SumPairs(defaultdict[Sum, set[Pair]]):
    """
    A class to store pairs of integers that sum to the same value.
    """

    def __init__(self, *args, **kwargs):
        # Initialize the defaultdict with 'set' as the default factory
        super().__init__(set, *args, **kwargs)

    def add_pair(self, sum_value: Sum, pair: Pair) -> None:
        # Sort the pair to ensure that only unique pairs are stored
        # Otherwise, we could end up with (a, b) and (b, a) as different pairs
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


def find_pairs(input: list[int]) -> SumPairs:
    """
    Find all unique pairs of integers in the input list that sum to the same value.
    Returns a SumPairs object containing the pairs grouped by their sum.

    :param input: List of integers to find pairs in.
    :return: SumPairs object containing pairs grouped by their sum.

    Example:
    >>> pairs = find_pairs([1, 2, 3, 4])
    >>> print(pairs)
    Pairs: (1, 4), (2, 3) have sum 5
    """
    result = SumPairs()
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            pair_sum = input[i] + input[j]
            result.add_pair(pair_sum, (input[i], input[j]))
    result.clean()
    return result
