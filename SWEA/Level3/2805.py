# DFS를 이용한 해결법 --> 시간초과
# from collections import deque

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# a = [(1, 2), (3, 2)]

# def dfs(x, y, cnt):
#     global result

#     if cnt == 0:
#         return

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if (nx, ny) not in result:
#             result.append((nx, ny))
#             dfs(nx, ny, cnt-1)

# t = int(input())

# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(map(int, input())) for _ in range(n)]
#     check = [[False] * n for _ in range(n)]
#     mid = len(arr) // 2
#     result = [(mid, mid)]

#     dfs(mid, mid, mid)

#     _sum = 0

#     for x, y in result:
#         _sum += arr[x][y]

#     print("#{0} {1}".format(tc, _sum))

# 55분
# 도움&참조 : O

# 1. 농장의 중앙에서 시작한다.
# 2. 각 좌표에서 농장의 중앙까지의 거리를 비교한다
# 2-1. 중앙까지의 거리안에 들어오는 좌표의 값을 더한다.

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    # 1
    mid = n // 2
    result = 0

    # 2
    for x in range(n):
        for y in range(n):
            # 2-1
            if abs(mid-x) + abs(mid-y) <= mid:
                result += board[x][y]

    print('#{0} {1}'.format(tc, result))
