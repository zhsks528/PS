# 30분
# 도움&참조 : X

# 1. 임의의 위치에서 시작한다.
# 2. dfs를 이용하여 7자리의 숫자를 만든다
# 3. 중복되지 않은 7자리 숫자의 갯수를 출력한다.

# 동서남북
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, result):
    global answer

    if len(result) == 7:
        answer.add(result)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, result + board[nx][ny])


t = int(input())

for tc in range(1, t+1):
    board = [list(input().split()) for _ in range(4)]
    answer = set()

    # 1
    for i in range(4):
        for j in range(4):
            # 2
            dfs(i, j, board[i][j])

    # 3
    print('#{0} {1}'.format(tc, len(answer)))
