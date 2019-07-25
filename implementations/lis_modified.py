"""
given a sequence, output size of the largest non-increasing subsequence
where every element can be divided by a previous element without the remainder
basically, a modified lis algorithm
"""
import sys


def lis_mod(sequence):
    D = [1] * len(sequence)
    ans = 0

    for i in range(len(sequence)):
        for j in range(i):
            if sequence[j] <= sequence[i] and D[j] + 1 > D[i] and sequence[i] % sequence[j] == 0:
                D[i] = D[j] + 1
        ans = max(ans, D[i])
    return ans


def main():
    data_size = sys.stdin.readline()
    data = list(map(int, sys.stdin.readline().split()))
    print(lis_mod(data))


def test_man():
    data = [3, 6, 7, 12]
    assert lis_mod(data) == 3
    assert lis_mod([4, 4, 4, 4]) == 4


if __name__ == '__main__':
    test_man()
