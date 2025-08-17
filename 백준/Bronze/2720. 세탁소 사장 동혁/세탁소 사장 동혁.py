# 세탁소 사장 동혁

"""
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수,
니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.
거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다.
"""

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
T = int(input())
for t in range(1, T+1):
    # 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나로 이루어져 있다. C의 단위는 센트이다
    c = int(input())

    quarter, dime, nickel, penny = 0,0,0,0

    quarter = c//25
    c = c - (25 * quarter)

    dime = c//10
    c = c - (10 * dime)

    nickel = c//5
    c = c - (5 * nickel)

    penny = c/1

    print(int(quarter), int(dime), int(nickel), int(penny))