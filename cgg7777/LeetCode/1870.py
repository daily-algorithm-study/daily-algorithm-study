import random

num_students = 100

# 학생 점수 생성
arr = [100] * 95
arr.append(1)
arr.append(1)
arr.append(1)
arr.append(1)
arr.append(1)

stra = ""
for entry in arr:
    stra += str(entry) + " "

print(stra)