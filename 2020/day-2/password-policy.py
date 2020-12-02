input = open("input.txt", "r")
valid_count1 = 0
valid_count2 = 0

for line in input:
  minmax, character, password = line.split(" ", 2)
  min, max = minmax.split("-")
  character = character[0]
  occurences = password.count(character)
  if int(min) <= occurences <= int(max):
    valid_count1 += 1

  if bool(password[int(min) - 1] == character) ^ bool(password[int(max) - 1] == character):
    valid_count2 += 1

print(f"password policy 1 count: {valid_count1}")
print(f"password policy 2 count: {valid_count2}")