# 10분
# 도움&참조 : X

# 1. 입력받은 배열에서 최댓값과 최솟값의 위치를 찾는다.
# 2. 평탄화 횟수만큼 작업을 한다. 최댓값 -= 1, 최솟값 += 1
# 3. 평탄화가 끝나면 결과값을 출력한다.


for tc in range(1, 11):
    n = int(input())  # 평균화 횟수
    arr = list(map(int, input().split()))

    while n:
        # 1
        maxIdx = arr.index(max(arr))
        minIdx = arr.index(min(arr))

        # 2
        arr[maxIdx] -= 1
        arr[minIdx] += 1

        n -= 1

    # 3
    if n == 0:
        print("#{0} {1}".format(tc, max(arr) - min(arr)))
