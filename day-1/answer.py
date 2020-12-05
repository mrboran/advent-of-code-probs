def find_two(content):
    a = 0
    b = 0
    found = 0
    for i in range(len(content)):
        a = content[i]
        for j in range(len(content)):
            b = content[j]
            if (int(a) + int(b)) == 2020:
                found = 1
                break
        if found == 1:
            break

    print("Numbers:", a, b)
    print("Answer:", int(a)*int(b))

def find_three(content):
    a = 0
    b = 0
    c = 0
    found = 0

    for i in range(len(content)):
        a = content[i]
        for j in range(len(content)):
            b = content[j]
            for k in range(len(content)):
                c = content[k]
                if (int(a) + int(b) + int(c)) == 2020:
                    found = 1
                    break
            if found == 1:
                break
        if found == 1:
            break

    print("Numbers:", a, b, c)
    print("Answer:", int(a)*int(b)*int(c))

if __name__ == "__main__":
    # input
    f = open('input.txt')

    content = f.read()
    content = content.split('\n')
    find_two(content)
    find_three(content)