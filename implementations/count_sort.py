"""
implementation of count sort
input format:
size of array
array as string of int separated by whitespace
"""
import sys


def count_sort(data):
    data_size = len(data)
    unique_els = list(set(data))
    unique_els.sort()
    n_unique_els = len(unique_els)
    counts = [0] * n_unique_els

    for j in range(data_size):
        j_index = unique_els.index(data[j])
        counts[j_index] += 1

    for i in range(1, n_unique_els):
        counts[i] += counts[i-1]

    data_sorted = [None] * data_size
    for j in reversed(range(data_size)):
        j_index = unique_els.index(data[j])
        data_sorted[counts[j_index]-1] = data[j]
        counts[j_index] -= 1
    return data_sorted


def main():
    data_size = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    print(*count_sort(data))


def test(n_iter=100):
    from random import randint
    for _ in range(n_iter):
        data_size = randint(3, 10**4)
        data = [randint(0, 10**4) for _ in range(data_size)]
        data_sorted = count_sort(data)
        data.sort()
        assert data_sorted == data


def test_man():
    data = list(map(int, input().split()))
    print(*count_sort(data))


if __name__ == '__main__':
    test_man()
