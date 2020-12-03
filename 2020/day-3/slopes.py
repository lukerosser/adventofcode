routes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
trees_total = 1

for route in routes:
  right = 0
  line_number = 0
  trees = 0
  right_increment = route[0]
  down = route[1]
  input = open("input.txt", "r")
  for line in input:
    if (line_number % down) == 0:
      if right >= len(line) - 1:
        right = (right % (len(line) - 1))

      if line[right] == "#":
        trees += 1
      right += right_increment
    else:
      pass
    line_number += 1

  trees_total = trees_total * trees

print(trees_total)