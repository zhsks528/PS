# 23분
# 도움&참조 : O

# 1. 결과값에 0을 넣어준다.
# 2. 입력된 배점만큼 반복하여 결과값을 구한다.
# 2-1. 결과에 속한 값과 배점을 더하여 새로운 결과값을 만든다.
# 2-2. 새로운 결과값을 저장한다.

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    # 1
    result = set()
    result.add(0)

    # 2
    for i in range(n):
        temp = []

        # 2-1
        for num in result:
            temp.append(arr[i] + num)

        # 2-2
        for t in temp:
            result.add(t)

    print('#{} {}'.format(tc, len(result)))
