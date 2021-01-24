# 10분
# 도움&참조 : X

# 1. 입력값이 범위에 만족하는 지 확인한다.

t = int(input())

for test_case in range(1, t+1):
    l, u, x = map(int, input().split())

    # 1
    if l <= x <= u:
        print('#{0} {1}'.format(test_case, 0))
    elif u <= x:
        print('#{0} {1}'.format(test_case, -1))
    else:
        print('#{0} {1}'.format(test_case, l-x))
