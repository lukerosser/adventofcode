import re

input = open("input.txt", "r")

valid_passports1 = 0
valid_passports2 = 0
passport = []

def check_passport(passport, validate):
  required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
  passport = dict(passport)
  valid = 0
  if all(key in passport for key in required):
    if validate:
      if 1920 <= int(passport["byr"]) <= 2002:
        if 2010 <= int(passport["iyr"]) <= 2020:
          if 2020 <= int(passport["eyr"]) <= 2030:
            if re.match("^1[5-8][0-9]cm|19[0-3]cm$", passport["hgt"]) or re.match("^59in|[6][0-9]in|7[0-6]in$", passport["hgt"]):
              if re.match("^#[0-9a-f]{6}$", passport["hcl"]):
                if passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                  if re.match("^[0-9]{9}$", passport["pid"]):
                    valid = 1
    else:
      valid = 1
  return valid

for line in input:
  if line != "\n":
    for key_value in line.split(" "):
      k, v = key_value.split(":")
      passport.append([k, v.strip("\n")])
  else:
    valid_passports1 += check_passport(passport, False)
    valid_passports2 += check_passport(passport, True)
    passport = []

valid_passports1 += check_passport(passport, False)
valid_passports2 += check_passport(passport, True)
print(f"Answer 1: {valid_passports1}")
print(f"Answer 2: {valid_passports2}")