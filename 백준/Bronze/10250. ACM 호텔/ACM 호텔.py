# https://www.acmicpc.net/problem/10250
# ACM 호텔

"""
1. h x w 크기의 2차원 배열
2. 1열부터 아래에서 위로 채우고 2열을 채우는 순서
3. 방 번호는 YXX 혹은 YYXX 형태로 주어짐
4. N 번째로 도착한 손님에게 배정될 방 번호는?
"""

T = int(input())
for t in range(T):
    # h = 행, w = 열, n = 손님 순서
    h, w, n = map(int, input().split())

    result = ''
    room_number = str((n // h) + 1)
    floor_nunber = str(n % h)

    if n % h == 0:
        room_number = str(n // h)
        floor_nunber = str(h)

    if len(room_number) < 2:
        room_number = '0' + room_number

    result = floor_nunber + room_number

    print(result)