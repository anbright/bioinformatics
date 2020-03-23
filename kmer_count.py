from typing import List


def pattern_count(input: str, pattern: str) -> int:
    i = 0
    count = 0
    k = len(pattern)
    indices = []
    pattern_length = len(input) - k + 1
    for i in range(pattern_length):
        substr = input[i : i + len(pattern)]
        if pattern == substr:
            count += 1
            indices.append(i)
    return (count, indices)


def count_kmers(input: str, k: int) -> List[int]:
    """Counts all kmers of length k in an input string

        Returns:
            List[int] where each index corresponds to the number of times
            that kmer occurs.
    """

    counts = [0] * len(input)
    max_count = 0
    # Do not want to search the end of the string so no chars remain
    search_length = len(input) - k + 1
    for i in range(search_length):
        pattern = input[i : i + k]
        counts[i], _ = pattern_count(input, pattern)
        max_count = max(max_count, counts[i])

    frequent_patterns = set()
    for i in range(search_length):
        if counts[i] == max_count:
            frequent_patterns.add(input[i : i + k])

    return frequent_patterns


if __name__ == "__main__":
    kmer_set = count_kmers(
        "GGCCTCCAGGGATGGTCGGGGCGAGCGGGGCGAGGGCCTCCAGGGATGGTCCCCACCAGCGGTGGCTGGATGGTGGCCTCCAGCCCCACCAGGCCTCCAGGGCCTCCAGGCGGTGGCTGGATGGTGGCCTCCAGGGCCTCCAGCCCCACCAGCGGTGGCTCCCCACCACCCCACCACCCCACCAGCGGTGGCTCCCCACCAGGCCTCCAGGCGGTGGCTGGCCTCCAGGCGGTGGCTGCGGTGGCTGGCCTCCAGCCCCACCACCCCACCACGGGGCGAGGCGGTGGCTGGCCTCCAGCCCCACCAGGATGGTCGGGGCGAGCCCCACCAGGCCTCCAGGGCCTCCAGGGCCTCCAGGCGGTGGCTCGGGGCGAGGGCCTCCAGGGATGGTGCGGTGGCTCCCCACCAGGCCTCCAGGCGGTGGCTCGGGGCGAGGGCCTCCAGGCGGTGGCTGCGGTGGCTGCGGTGGCTGCGGTGGCTGGCCTCCAGGGCCTCCAGCCCCACCAGGCCTCCAGCCCCACCACCCCACCAGGCCTCCAGGCGGTGGCTGGCCTCCAGGGATGGTCGGGGCGAGCCCCACCACGGGGCGAGCGGGGCGAGGCGGTGGCTGGATGGTCCCCACCAGGATGGTGGCCTCCAGGCGGTGGCTCCCCACCACGGGGCGAGGGCCTCCAGGGATGGTCCCCACCACCCCACCACGGGGCGAGCGGGGCGAGCCCCACCAGGCCTCCAGCGGGGCGAGGGCCTCCAGCCCCACCACCCCACCAGGCCTCCAGGGCCTCCAGCGGGGCGAGGCGGTGGCTGGCCTCCAGCGGGGCGAGGGCCTCCAGGCGGTGGCTCGGGGCGAGGCGGTGGCTCCCCACCAGCGGTGGCT",
        11,
    )

    print(kmer_set)
    print(" ".join(list(kmer_set)))

    print(pattern_count("GATATATGCATATACTT", "ATAT",))
