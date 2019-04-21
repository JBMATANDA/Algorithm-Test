from Algorithm import BubbleSort

data = [5, 8, 3, 9, 0, 3, 6, 7]
print(data)

n_ops = BubbleSort.sort(data)

print(data)
print("n_ops: %d" % n_ops)
