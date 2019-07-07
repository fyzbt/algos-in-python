"""
find partition in which no number occurs more than once and has maximum number of parts
(partition with distinct parts:
https://en.wikipedia.org/wiki/Partition_(number_theory)#Restricted_part_size_or_number_of_parts)
didn't need that but some fun reads:
https://www.mathpages.com/home/kmath556/kmath556.htm
https://math.berkeley.edu/~mhaiman/math172-spring10/partitions.pdf
"""


def main():
    """
    inputs a number for which to find a partition
    :return: outputs max number of elements in a partition and the partition itself
    """
    n = int(input())
    k = 1
    while ((k * (k + 1)) / 2) < n:
        k += 1
    q_n = k - 1
    part_q = list(range(1, q_n))
    part_q.append(n - sum(part_q))
    print(q_n)
    print(*part_q)


if __name__ == '__main__':
    main()
