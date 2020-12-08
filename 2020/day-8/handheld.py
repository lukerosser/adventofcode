input = open("input.txt", "r")

code = []
bug_located = False
bug_fixed_accumulator = 0

def run_code(accumulator: int, current_location: int, executed: list, fix_bug: bool = False, iterate: bool = False) -> int:
  global bug_located
  global bug_fixed_accumulator
  # reassign to avoid recursion issues with object
  executed = [item for item in executed]
  while current_location not in executed:
    executed.append(current_location)
    if code[current_location][0] == "acc":
      accumulator = add_subtract(accumulator, code[current_location][1], code[current_location][2])
      current_location += 1
    elif code[current_location][0] == "jmp":
      if not bug_located and iterate:
        run_code(accumulator, current_location + 1, executed, True, False)
      current_location = add_subtract(current_location, code[current_location][1], code[current_location][2])
    elif code[current_location][0] == "nop":
      if not bug_located and iterate:
        run_code(accumulator, add_subtract(current_location, code[current_location][1], code[current_location][2]), executed, True, False)
      current_location += 1
    else:
      print("error, unknown operation")
    if fix_bug:
      if not bug_located:
        if current_location >= len(code):
          bug_fixed_accumulator = accumulator
          bug_located = True
          break
  return accumulator

def add_subtract(start: int, pos_neg: str, value: str) -> int:
  if pos_neg == "+":
    start += int(value)
  elif pos_neg == "-":
    start -= int(value)
  return start  

for line in input:
  operation, argument = line.strip("\n").split(" ")
  pos_neg = argument[0]
  value = argument[1:]
  code.append([operation, pos_neg, value])

print(f"Answer 1: {run_code(0, 0, [])}")
run_code(0, 0, [], True, True)
print(f"Answer 2: {bug_fixed_accumulator}")