"""
implement binary search
input: k natural numbers and a list of n size
output:
for each num in k
- if list[i] == num: i
- if num not in list: -1

"""
import sys
from math import floor


def binary_search(k, data, n):
    left = 0
    right = n - 1

    while left <= right:
        m = floor((left + right) / 2)
        if data[m] is k:
            return m + 1  # so that index starts with 1 and not 0 in answer
        elif data[m] > k:
            right = m - 1
        elif data[m] < k:
            left = m + 1
    return -1


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    line_data = next(reader)
    line_nums = next(reader)

    n, data = line_data[0], line_data[1:]
    n_nums, nums = line_nums[0], line_nums[1:]

    print(*(binary_search(k, data, n) for k in nums))


def test(n_iter=100):
    from random import randint
    from timing import timed
    for _ in range(n_iter):
        k = randint(0, 10**5)
        n = randint(1000, 10**5)
        data = [randint(0, 10**9) for _ in range(n)]
        t = timed(binary_search, k, data, n)
        assert t < 3


if __name__ == '__main__':
    test()
