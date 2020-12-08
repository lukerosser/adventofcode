input = open("input.txt", "r")

bag_types = {}
search_bag_name = "shiny gold"
contains_search_bag = {search_bag_name}

def look_for_bags():
  for bag in bag_types:
    if any(x in contains_search_bag for x in bag_types[bag]):
      if bag not in contains_search_bag:
        contains_search_bag.add(bag)
        look_for_bags()

def count_bags(bags: dict) -> int:
  count = 0
  for bag in bags:
    recurse_count = count_bags(bag_types[bag])
    count += int(bags[bag]) + (int(bags[bag]) * recurse_count)
  return count

for line in input:
  bag_type, contains = line.split(" contain ")
  bag_type_split = bag_type.split(" bag")
  bag_type = bag_type_split[0]
  contents = {}

  for contains_bag in contains.strip("\n").split(", "):
    if contains_bag != "no other bags.":
      split_contains_bag = contains_bag.split(" ")
      container_bag = split_contains_bag[1] + " " + split_contains_bag[2]
      container_bag_count = split_contains_bag[0]
      contents[container_bag] = container_bag_count

    bag_types[bag_type] = contents

look_for_bags()
print(f"Answer 1: {len(contains_search_bag) - 1}")
print(f"Answer 2: {count_bags(bag_types[search_bag_name])}")