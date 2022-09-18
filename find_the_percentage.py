n = int(input())
each_students_pair = input()
query_name = input()
student_marks = {}
for _ in range(n):
    name, *line = each_students_pair.split() # this say that the fist element of the input(after have been splitted into a list) belongs to the name and all others eleme belongs to the *args variable
    scores = list(map(float, line))   # this pass every single eleme of the list(line) into the function called float() => become float

for key, val in student_marks.items():
    if key == query_name:
        avg = sum(list(student_marks[key])) / len(list(student_marks[key]))
        avg = '%.2f' % avg    # this is the way to show 2 decimal places which can't be achieved through round()
print(avg)