input = open("input.txt", "r")

answer_counts = []
same_answer_counts = []
answers1 = ""
answers2 = ""
group_members = 0

def declarations(group_answers, count):
  if count == 0:
    return len(set(group_answers))
  else:
    common_answers = []
    unique_answers = set(group_answers)
    for answer in unique_answers:
      if group_answers.count(answer) == count:
        common_answers.append(answer)
    return len(common_answers)

for line in input:
  if line != "\n":
    answers1 = answers1 + line.strip("\n")
    answers2 = answers2 + line.strip("\n")
    group_members += 1
  else:
    answer_counts.append(declarations(answers1, 0))
    same_answer_counts.append(declarations(answers2, group_members))
    answers1 = ""
    answers2 = ""
    group_members = 0

answer_counts.append(declarations(answers1, 0))
same_answer_counts.append(declarations(answers2, group_members))

print(f"Answer 1: {sum(answer_counts)}")
print(f"Answer 2 :{sum(same_answer_counts)}")