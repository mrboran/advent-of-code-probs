def preprocess():
    # number of rows
    rows = 128
    columns = 8

    row_array = []
    column_array = []

    # make input row array
    for i in range(rows):
        row_array.append(i)

    # make input column array
    for i in range(columns):
        column_array.append(i)
    
    return row_array, column_array

def sol(row_array, column_array, file):
    # read file content
    f = open(file)
    tickets = f.read()
    tickets = tickets.split('\n')

    row_upper = row_array[-1]
    row_lower = row_array[0]

    column_lower = column_array[0]
    column_upper = column_array[-1]

    print(row_lower, row_upper, column_lower,column_upper )

    for ticket in tickets:
        for char in ticket:
            if char == 'B':
                row_lower = row_upper / 2
            elif char == 'F':
                row_upper = row_upper / 2
            elif char == 'R':

            elif char == 'L':

if __name__ == '__main__':
    FILE = 'input.txt'
    row_array, column_array = preprocess()
    sol(row_array, column_array, FILE)
