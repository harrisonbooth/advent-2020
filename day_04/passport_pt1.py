# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) [OPTIONAL]
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passports = [passport_string.split() for passport_string in open('input.txt', 'r').read().split('\n\n')]
passport_dicts = [{key: value for [key, value] in [field.split(":") for field in passport] if key != "cid"} for passport in passports]

total = 0
for passport_dict in passport_dicts:
    if sorted(list(passport_dict.keys())) == sorted(required_fields):
        total += 1

print(total)
