"""
implementation of the rucksack without repetitions bottom-up algorithm
modification: cost of a bar == bar's weight
inputs maximum sack weight, number of bars, bars' weights
outputs
total optimal rucksack weight with bars
"""
import sys
import numpy as np


def rucksack_bu(max_sack_wt, sticks_num, sticks_wt):
    weights_table = np.empty([max_sack_wt + 1, sticks_num + 1])

    for w in range(max_sack_wt):
        weights_table[w, 0] = 0
    for i in range(sticks_num):
        weights_table[0, i] = 0

    for i in range(1, sticks_num+1):
        for w in range(1, max_sack_wt+1):
            weights_table[w, i] = weights_table[w, i - 1]
            if sticks_wt[i-1] <= w:
                weights_table[w, i] = max(weights_table[w, i], weights_table[w - sticks_wt[i-1], i-1]+sticks_wt[i-1])

    return int(weights_table[max_sack_wt, sticks_num])


def main():
    max_wt, num_sticks = map(int, sys.stdin.readline().split())
    sticks_wt = [int(i) for i in sys.stdin.readline().split()]
    print(rucksack_bu(max_wt, num_sticks, sticks_wt))


def test_man():
    max_wt, num_sticks = 10, 3
    sticks_wt = [1, 4, 8]
    assert rucksack_bu(max_wt, num_sticks, sticks_wt) == 9


if __name__ == '__main__':
    test_man()
