import re


class Verifier:
    def verify_passport(self, passport):
        for field, value in passport.items():
            if not self.verify_field(field, value):
                return False
        return True

    def verify_field(self, field_name, field_value):
        method_name = 'verify_' + field_name
        verifier_function = getattr(self, method_name)
        return verifier_function(field_value)

    def verify_byr(self, byr):
        return len(byr) == 4 and 1920 <= int(byr) <= 2002

    def verify_iyr(self, iyr):
        return len(iyr) == 4 and 2010 <= int(iyr) <= 2020

    def verify_eyr(self, eyr):
        return len(eyr) == 4 and 2020 <= int(eyr) <= 2030

    def verify_hgt(self, hgt):
        hgt_re = '^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$'
        return re.match(hgt_re, hgt) is not None

    def verify_hcl(self, hcl):
        hcl_re = '^#([a-f0-9]{6})$'
        return re.match(hcl_re, hcl) is not None

    def verify_ecl(self, ecl):
        ecl_re = '^(amb|blu|brn|gry|grn|hzl|oth)$'
        return re.match(ecl_re, ecl) is not None

    def verify_pid(self, pid):
        pid_re = '^[0-9]{9}$'
        return re.match(pid_re, pid) is not None


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passports = [passport_string.split() for passport_string in open('input.txt', 'r').read().split('\n\n')]
passport_dicts = [{key: value for [key, value] in [field.split(":") for field in passport] if key != "cid"} for passport in passports]

total = 0
for passport_dict in passport_dicts:
    if sorted(list(passport_dict.keys())) == sorted(required_fields) and Verifier().verify_passport(passport_dict):
        total += 1

print(total)
