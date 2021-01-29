# 25분
# 도움&참조 : X

# 1. 왼쪽 대각선과 오른쪽 대각선의 합을 구한다.
# 2. 각 행과 열의 합 중 최댓값을 구한다

for _ in range(1, 11):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    max_row = 0  # 각 행의 합 중 최댓값
    max_col = 0  # 각 열의 합 중 최댓값

    value_left_cross = 0  # 왼쪽 대각선의 합
    value_right_cross = 0  # 오른쪽 대각선의 합

    for i in range(100):
        value_row_sum = 0
        value_col_sum = 0

        # 1
        value_left_cross += board[i][i]
        value_right_cross += board[i][100-i-1]

        # 2
        for j in range(100):
            value_row_sum += board[i][j]
            value_col_sum += board[j][i]

        max_row = max(max_row, value_row_sum)
        max_col = max(max_col, value_col_sum)

    result = max(max_row, max_col, value_left_cross, value_right_cross)

    print("#{0} {1}".format(tc, result))
