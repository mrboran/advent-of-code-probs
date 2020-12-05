import re
# checker with out 'cid'
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passport = 0

# file read
file_name = "input.txt"
f = open(file_name)

# get file content
file_lines = f.readlines()

file_content = ""
i = 0

for line in file_lines:
    if line == '\n':
        file_content = file_content + '\n'
        i += 1
    elif '\n' in line:
        file_content = file_content + line.split('\n')[0] + ' '
    else:
        file_content = file_content + line

passports = file_content.split('\n')

for passport in passports:
    valid = 1
    for passport_field in passport_fields:
        if passport_field in passport:
            valid = 1
        else:
            valid = 0
            break
        # break
    if valid == 1:
        valid_passport += 1

print("Total Number of valid passports =", valid_passport)

# --------Second part -----

for passport in passports:
    s_valid = True
    # for birth year
    birth = passport.split('byr:')[-1].split(' ')[0]
    bir = re.compile(r'\d\d\d\d')
    if bir.match(birth):
        if not (int(birth) >= 1920 and int(birth) <= 2002):
            print('birth not valid')
            s_valid = False
    else:
        s_valid = False
    
    # for issue year
    iyr = passport.split('iyr:')[-1].split(' ')[0]
    iss = re.compile(r'\d\d\d\d')
    if iss.match(iyr):
        if not (int(iyr) >= 2010 and int(iyr) <= 2020):
            print('issue year not valid')
            s_valid = False
    else:
        s_valid = False
    
    # for expiration year
    eyr = passport.split('eyr:')[-1].split(' ')[0]
    exp = re.compile(r'\d\d\d\d')
    if exp.match(eyr):
        if not (int(eyr) >= 2010 and int(eyr) <= 2020):
            print('issue year not valid')
            s_valid = False
    else:
        s_valid = False
    
    # for height 
    hgt = passport.split('eyr:')[-1].split(' ')[0]
    height = re.compile(r'cm|in')