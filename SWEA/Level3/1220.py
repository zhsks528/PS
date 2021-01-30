# 35분
# 도움&참조 : O
# 참조 : https://mungto.tistory.com/152


for tc in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    for j in range(n):
        temp_stack = []
        check = False

        # 아래부터 위로 진행하면서 찾는다.
        for i in range(n):
            if board[i][j] == 1:
                temp_stack.append(1)
            if board[i][j] == 2 and temp_stack:
                temp_stack.clear()
                count += 1

    print("#{0} {1}".format(tc, count))
