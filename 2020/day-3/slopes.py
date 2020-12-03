routes = [[1,1, False], [3,1, True], [5,1, False], [7,1, False], [1,2, False]]
trees_total = 1

for route in routes:
  right = 0
  line_number = 0
  trees = 0
  right_increment = route[0]
  down = route[1]
  show_route = route[2]
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
  if show_route:
    print(f"First answer: {trees}")
  trees_total = trees_total * trees

print(f"Second answer: {trees_total}")