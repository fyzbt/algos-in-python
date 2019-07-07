"""
you have a rucksack with W max weight. you have N products with C price and A amounts.
find an optimal amounts of products to fill your whole sack and maximize the cumulative
cost of the products in your sack
"""


from decimal import *


def main():
    """
    :return: cumulative price of products in the rucksack
    """
    n_prod, w_ruck = map(int, input().split())
    prods = [[int(i) for i in input().split()] for _ in range(n_prod)]
    prods = sorted(prods, key=lambda x: x[0] / x[1], reverse=True)
    cum_price = Decimal(0)
    for prod in prods:
        if prod[1] < w_ruck:
            w_ruck -= prod[1]
            cum_price += Decimal(prod[0])
        else:
            cum_price += Decimal(prod[0]) / Decimal(prod[1] * w_ruck)
            w_ruck -= prod[1]
        if w_ruck < 0:
            break
    cum_price = max(0, cum_price)
    print(format(cum_price, ".3f"))


if __name__ == '__main__':
    main()
