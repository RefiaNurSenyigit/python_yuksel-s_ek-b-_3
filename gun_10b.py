n = int(input())
student_marks = {}
sum=0
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    for a in student_marks[name]:
        sum=sum+a
    print(sum/3)