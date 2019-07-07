"""
count number of inversions in list
inversion: for a pair of indices in list 1 <= i < j <= n if A[i] > A[j]
in a sorted array number of inversions is 0
input:
list size
list elements as string separated by whitespace
"""
import sys

num_inversions = 0


def recursive_merge_sort(data):
    """
    recursively merge sort array
    takes list of numerical elements as input
    """
    if len(data) <= 1:
        return data

    mean_el = len(data) // 2
    left_data = recursive_merge_sort(data[:mean_el])
    right_data = recursive_merge_sort(data[mean_el:])

    return merge(left_data, right_data)


def merge(left_data, right_data):
    i_left, i_right = 0, 0

    merged_data = []
    global num_inversions

    while i_left < len(left_data) and i_right < len(right_data):
        if left_data[i_left] <= right_data[i_right]:
            merged_data.append(left_data[i_left])
            i_left += 1

        else:
            merged_data.append(right_data[i_right])
            # upfating global counter variable
            num_inversions += len(left_data) - i_left
            i_right += 1

    merged_data += left_data[i_left:]
    merged_data += right_data[i_right:]
    return merged_data


def main():
    data_size = int(sys.stdin.readline())
    data = list(map(float, sys.stdin.readline().split()))
    recursive_merge_sort(data)
    print(num_inversions)


def test(n_iter=100):
    from random import randint
    for _ in range(n_iter):
        # to drop global counter variable for each test iteration
        global num_inversions
        num_inversions -= num_inversions

        n = randint(1, 3)
        data = [randint(0, 5) for _ in range(n)]
        recursive_merge_sort(data)
        print(data)
        print(num_inversions)


def test_man():
    data = [7, 6, 5, 4, 3, 2, 1]
    data = [1, 2, 3, 5, 4]
    data = [6, 4, 5, 0, 0, 2]
    data = [2, 3, 9, 2, 9]
    data = [10, 8, 6, 2, 4, 5]
    data = [10, 9, 3, 8, 3, 10]
    recursive_merge_sort(data)
    print(num_inversions)


if __name__ == '__main__':
    main()
