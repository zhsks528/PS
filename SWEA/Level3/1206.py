# 15분
# 도움&참조 : X

# 1. 현재 빌딩에서 왼쪽 전망 - 오른쪽 전망 가장 큰 빌딩을 찾는다.
# 1-1. 현재 빌딩과 가장 큰 빌딩의 높이를 비교한다.

for tc in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))
    count = 0

    # 1
    for i in range(2, n-2):
        around = max([data[i - 2], data[i - 1], data[i + 1], data[i + 2]])

        # 1-1
        if data[i] > around:
            count += data[i] - around

    print("#{0} {1}".format(tc, count))
