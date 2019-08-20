from test_framework import generic_test


def levenshtein_distance(A, B):
    def calculate_distance(index_a, index_b):
        if index_a < 0:
            return index_b + 1
        if index_b < 0:
            return index_a + 1
        
        if distance_between[index_a][index_b] == -1:
            if A[index_a] == B[index_b]:
                distance_between[index_a][index_b] = calculate_distance(index_a-1, index_b-1)
            else:
                sub = calculate_distance(index_a-1, index_b-1)
                add = calculate_distance(index_a-1, index_b)
                delete  =calculate_distance(index_a, index_b -1)
                distance_between[index_a][index_b] = 1 + min(sub, add, delete)
        
        return distance_between[index_a][index_b]


    distance_between = [[-1] * len(B) for _ in A]
    return calculate_distance(len(A)-1, len(B)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
