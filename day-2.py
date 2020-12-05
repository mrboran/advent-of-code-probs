import numpy as np
from numpy.core.defchararray import array
from numpy.testing._private.utils import break_cycles

# read the file
f = open("input-example.txt", "r")
file = f.read()

list_of_rows = file.split('\n')
print(len(list_of_rows))

print(list_of_rows)

tree = 0

arr = np.empty(shape=(0, 0))

for i in range(len(list_of_rows)):
    print(list_of_rows[i])
    row = []
    for ch in list(list_of_rows[i]):
        if ch == '1':
            row.append(1)
        else:
            row.append(2)
    row = row * 7
    my_array = np.asarray(row)
    # print(len(row))
    # print(row)
    # print(type(row))

    # print(len(my_array))
    # print(my_array)
    # print(type(my_array))
    arr = np.append(arr, my_array, axis=0)
    print(arr)
    break