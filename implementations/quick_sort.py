"""
simple quick sort implementation
"""
from random import randint


def quick_sort(data, left_bound, right_bound):
    x = data[randint(left_bound, right_bound)]
    i = left_bound
    j = right_bound

    while i <= j:
        while data[i] < x:
            i += 1
        while data[j] > x:
            j -= 1
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1

    if left_bound < j:
        quick_sort(data, left_bound, j)
    if i < right_bound:
        quick_sort(data, i, right_bound)

    return data


def main():
    data = list(map(int, input().split()))
    data_sorted = quick_sort(data, 0, len(data)-1)
    print(data_sorted)


def test(n_iter=100):
    for _ in range(n_iter):
        n = randint(1, 10**4)
        data = [randint(0, 10**4) for _ in range(n)]
        sorted_data = quick_sort(data, 0, n-1)
        data.sort()
        assert sorted_data is data


if __name__ == '__main__':
    test()
