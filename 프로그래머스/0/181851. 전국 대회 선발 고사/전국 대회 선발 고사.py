def solution(rank, attendance):
    l = len(rank)
    students = []
    
    for i in range(l):
        if attendance[i]:
            students.append((rank[i], i))
    
    selected = sorted(students)[:3]
    a, b, c = selected[0][1], selected[1][1], selected[2][1]
    answer = 10000 * a + 100 * b + c
        
    return answer