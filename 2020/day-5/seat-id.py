input = open("input.txt", "r")

seats = []

def upper_lower(char, min, max, last):
  middle = ((max - min) // 2) + 1
  if char == "F" or char == "L":
    if last:
      return min
    max -= middle
  elif char == "B" or char == "R":
    if last:
      return max
    min += middle
  return min, max

for seat in input:
  min_row = 0
  max_row = 127
  row = 0
  min_column = 0
  max_column = 7
  column = 0
  for char in seat[0:6]:
    min_row, max_row = upper_lower(char, min_row, max_row, False)
  row = upper_lower(seat[6], min_row, max_row, True)

  for char in seat[7:9]:
    min_column, max_column = upper_lower(char, min_column, max_column, False)
  column = upper_lower(seat[9], min_column, max_column, True)

  seats.append(row * 8 + column)


seats = sorted(seats)
print(f"Answer 1: {max(seats)}")

count = seats[0]

for seat in seats:
  if seat == count:
    count += 1
    continue
  my_seat = count
  break

print(f"Answer 2: {my_seat}")