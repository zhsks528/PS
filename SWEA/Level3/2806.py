# 15분
# 도움&참조 : X

# 1. DFS를 이용하여 퀸이 들어갈 수 있는 자리를 찾는다.
# 1-1. 퀸이 들어갈 수 있는지 확인한다.


def isAvailable(col, candiate):
    current_row = len(candiate)

    for queen_row in range(current_row):
        if candiate[queen_row] == col or abs(candiate[queen_row] - col) == current_row - queen_row:
            return

    return True


def dfs(n, current_row, current_candiate, result):
    if n == current_row:
        result.append(current_candiate[:])
        return

    for col in range(n):
        # 1-1
        if isAvailable(col, current_candiate):
            current_candiate.append(col)
            dfs(n, current_row + 1, current_candiate, result)
            current_candiate.pop()


t = int(input())

for tc in range(t):
    n = int(input())

    result = []

    # 1
    dfs(n, 0, [], result)

    print('#{0} {1}'.format(tc, len(result)))
