from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # find the two repeated words that are closer to each other

    distance = len(paragraph)
    words = {}

    for i, c in enumerate(paragraph):
        if c in words:
            prev_index = words[c]
            temp_dist = i - prev_index
            words[c] = i
            if temp_dist < distance:
                distance = temp_dist
        else:
            words[c] = i

    return distance if distance != len(paragraph) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
