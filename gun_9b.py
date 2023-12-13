python_students=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    python_students.append([name,score])
print("Listeniz->",python_students)
print(sorted("Sondan ikinci öğrenci ve notu->",python_students)[-2])