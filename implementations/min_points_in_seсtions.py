"""
you have N sections (e.g., [[1, 5], [4, 5]])
and you need to find a set of int
so that each section has at least one int from the set that is included in the section
"""


def main():
    """
    input: number of sections, each section in next string
    :return: len of set, set as a string with each value separated by a whitespace
    """
    n_secs = int(input())
    secs = [[int(i) for i in input().split()] for _ in range(n_secs)]
    secs = sorted(secs, key=lambda x: x[1])

    points = []
    point = secs[0][1]
    points.append(point)

    for i in range(n_secs):
        if point not in range(secs[i][0], secs[i][1] + 1):
            point = secs[i][1]
            points.append(point)

    print(len(points))
    print(*points)


if __name__ == '__main__':
    main()
