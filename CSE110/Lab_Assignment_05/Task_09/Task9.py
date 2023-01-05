exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
new_dict = {}
num_input = int(input())

for i in exam_marks:
  if exam_marks[i] >= num_input:
    new_dict[i] = exam_marks[i]

print(new_dict)