"""
output edit distance of two non-empty strings
"""
import sys
import numpy as np


def diff(a, b):
    assert isinstance(a, str) and isinstance(b, str)

    if a != b:
        return 1

    return 0


def edit_distance(s1, s2):
    min_s = min(s1, s2)
    if min_s == s1:
        max_s = s2
    else:
        max_s = s1

    dist_matrix = np.zeros([len(min_s) + 1, len(max_s) + 1])
    for i in range(dist_matrix.shape[0]):
        dist_matrix[i, 0] = i

    for j in range(dist_matrix.shape[1]):
        dist_matrix[0, j] = j

    for i in range(1, dist_matrix.shape[0]):
        for j in range(1, dist_matrix.shape[1]):
            c = diff(min_s[i - 1], max_s[j - 1])
            ins = dist_matrix[i - 1, j] + 1
            delete = dist_matrix[i, j - 1] + 1
            sub = dist_matrix[i - 1, j - 1] + c
            dist_matrix[i, j] = min(ins, delete, sub)

    return dist_matrix[len(min_s), len(max_s)]


def main():
    s1 = sys.stdin.readline()
    s2 = sys.stdin.readline()

    print(int(edit_distance(s1, s2)))


def test_man():
    s1 = "short"
    s2 = "ports"
    print(int(edit_distance(s1, s2)))


if __name__ == '__main__':
    main()
