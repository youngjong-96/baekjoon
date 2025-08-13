# 너의 평점은,,,

# 기준
standard = {'A+':4.5,
         'A0':4.0,
         'B+':3.5,
         'B0':3.0,
         'C+':2.5,
         'C0':2.0,
         'D+':1.5,
         'D0':1.0,
         'F':0.0,
         }

# 입력 받기
data = [list(map(str, input().split())) for _ in range(20)]

grades = []  # 등급 (A, B 등)
scores = []  # 학점 (3.0, 4.0 등)
cal = []  # 학점 x 등급

for i in range(20):
    if data[i][2] != 'P':
        scores.append(float(data[i][1]))

for i in range(20):
    if data[i][2] != 'P':
        grades.append(float(standard[data[i][2]]))

for i in range(len(grades)):
    cal.append(grades[i] * scores[i])

print(sum(cal)/sum(scores))