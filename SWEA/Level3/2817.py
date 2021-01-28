# 20분
# 도움&참조 : O

# 1. 재귀를 이용하여 K 와 같은 값을 찾는다.


def dfs(idx, result):

    global count

    if idx >= n:
        return

    temp = result + arr[idx]

    if temp == k:
        count += 1

    dfs(idx+1, result)
    dfs(idx+1, temp)


t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0

    # 1
    dfs(0, 0)

    print("#{0} {1}".format(tc, count))
