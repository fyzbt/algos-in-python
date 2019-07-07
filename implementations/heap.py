"""
implement a heap data structure with insertion and max extraction
"""


class MaxHeap(object):
    def __init__(self):
        self.data = [0]
        self.data_size = 0

    def insert(self, val):
        """
        inserts a value into heap (sifts it up)
        """
        assert isinstance(val, int)
        self.data.append(val)
        self.data_size += 1
        val_id = self.data_size
        self.sift_up(val_id)

    def sift_up(self, i):
        """
        sifts up an element with id i
        """
        i_par = i // 2

        while i_par > 0:
            if self.data[i] > self.data[i_par]:
                self.data[i], self.data[i_par] = self.data[i_par], self.data[i]
            i = i // 2
            i_par = i // 2

    def get_max_child(self, i):
        child_left = i * 2
        child_right = child_left + 1

        if child_right > self.data_size:
            return child_left

        else:
            if self.data[child_left] > self.data[child_right]:
                return child_left

            else:
                return child_right

    def sift_down(self, i):
        while (i * 2) <= self.data_size:
            i_child = self.get_max_child(i)

            if self.data[i] < self.data[i_child]:
                self.data[i], self.data[i_child] = self.data[i_child], self.data[i]
            i = i_child

    def extract_max(self):
        if self.data_size > 0:
            max_val = self.data[1]
            self.data[1] = self.data[self.data_size]
            self.data.pop()
            self.data_size -= 1
            self.sift_down(1)
            print(max_val)


def main():
    heap = MaxHeap()
    n_oper = int(input())

    for _ in range(n_oper):
        x = input()
        if x.startswith("Insert "):
            heap.insert(int(x.split()[1]))
        elif x.startswith("ExtractMax"):
            heap.extract_max()


if __name__ == '__main__':
    main()
