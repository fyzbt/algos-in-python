"""
trivial implementation of insertion sort
I had to do that eventually
"""
import sys


def insertion_sort(data):
    assert isinstance(data, list)

    for i in range(1, len(data)):
        j = i
        while j > 1 and data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1
    return data


def test(n_tests=100):
    from random import randint
    for _ in range(n_tests):
        data_size = randint(2, 10**2)
        data = [randint(0, 10**3) for _ in range(data_size)]
        sorted_data = insertion_sort(data)
        data.sort()
        assert sorted_data == data


def main():
    data = list(map(float, sys.stdin.readline().split()))
    print(*insertion_sort(data))


if __name__ == '__main__':
    test()
