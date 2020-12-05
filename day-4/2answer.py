# checker with out 'cid'
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passport = 0

# file read
file_name = "example-input.txt"
f = open(file_name)

content = f.read()

lines = content.split('\n\n')
isValid = 0

for line in lines:
    valid = 1
    for passport_field in passport_fields:
        if passport_field in line:
            valid = 1
        else:
            valid = 0
            break
    if valid == 1:
        isValid = isValid + 1

print(isValid)







print(lines)
