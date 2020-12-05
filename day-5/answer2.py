file = 'input.txt'
# file = 'example-2.txt'
f = open(file)
tickets = f.read()
tickets = tickets.split('\n')

max = 0
ids = ' '

for ticket in tickets:
    r_upper = 128
    r_lower = 0

    c_upper = 8
    c_lower = 0
    for char in ticket:
        if char == 'B':
            r_lower = ((r_upper - r_lower) // 2) + r_lower
            # print(r_lower, r_upper)
        elif char == 'F':
            r_upper = ((r_upper - r_lower) // 2 ) + r_lower
            # print(r_lower, r_upper)
        elif char == 'R':
            c_lower = ((c_upper - c_lower) // 2 ) + c_lower
            # print(c_lower, c_upper)
        elif char == 'L':
            c_upper = ((c_upper - c_lower) // 2 ) + c_lower
            # print(c_lower, c_upper)
    
    row = r_upper-1
    column = c_upper - 1

    id = row * 8 + column

    # print("ID:", id)

    ids = ids + str(id) + ' '
    if id >= max:
        max = id

# print('ids: ', ids)
print("Max:",max)
# print(ids)
i = 0 
while i < 1024:
    test = ' ' + str(i) + ' '
    if test in ids:
        pass
    else:
        print(test)
    i = i + 1

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.