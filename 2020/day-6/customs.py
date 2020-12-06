input = open("input.txt", "r")

answer_counts = []
same_answer_counts = []
group_answers = ""
group_members = 0

def declarations(group_answers: str, number_of_people: int = None) -> int:
  if not number_of_people:
    return len(set(group_answers))
  else:
    common_answers = []
    unique_answers = set(group_answers)
    for answer in unique_answers:
      if group_answers.count(answer) == number_of_people:
        common_answers.append(answer)
    return len(common_answers)

for line in input:
  if line != "\n":
    group_answers = group_answers + line.strip("\n")
    group_members += 1
  else:
    answer_counts.append(declarations(group_answers))
    same_answer_counts.append(declarations(group_answers, group_members))
    group_answers = ""
    group_members = 0

answer_counts.append(declarations(group_answers))
same_answer_counts.append(declarations(group_answers, group_members))

print(f"Answer 1: {sum(answer_counts)}")
print(f"Answer 2 :{sum(same_answer_counts)}")