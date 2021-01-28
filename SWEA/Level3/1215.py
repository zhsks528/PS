# 30분
# 도움&참조 : X

# 1. 범위를 벗어나지 않으며 회문의 길이만큼 문자를 저장한다.
# 1-1. 상, 하로 이동하는 것 = 아래로 이동하는 것으로 통일 가능
# 1-2. 좌, 우로 이동하는 것 = 우로 이동하는 것으로 통일 가능
# 1-3. 지정한 길이가 되었는지 확인한다.
# 2. 회문인지 확인한다.

for tc in range(1, 11):
    k = int(input())
    arr = [list(input()) for _ in range(8)]
    result = []

    # 1
    for i in range(8):
        for j in range(8):
            currentStrRight = arr[i][j]
            currentStrDown = arr[i][j]

            # 1-1
            for y in range(1, k):
                if 0 <= j+y < 8:
                    currentStrRight += arr[i][j+y]

            # 1-2
            for x in range(1, k):
                if 0 <= i+x < 8:
                    currentStrDown += arr[i+x][j]

                    # 1-3
            if len(currentStrRight) == k:
                result.append(currentStrRight)

            if len(currentStrDown) == k:
                result.append(currentStrDown)

        # 2
    count = 0

    for value in result:
        if value == value[::-1]:
            count += 1

    print("#{0} {1}".format(tc, count))
