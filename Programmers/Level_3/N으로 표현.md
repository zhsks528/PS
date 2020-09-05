---
title: "프로그래머스 - N으로 표현"
date: "2020-09-05T16:59:33.112"
category: "ps"
emoji: "📶"
---

## 프로그래머스 - N으로 표현

- 관련된 알고리즘 : 다이나믹 프로그래밍

### 문제 설명

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

### 제한사항

- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

### 입출력 예

| N    | number | return |
| ---- | ------ | ------ |
| 5    | 12     | 4      |
| 2    | 11     | 3      |

##### 입출력 예 설명

예제 #1
문제에 나온 예와 같습니다.

예제 #2
`11 = 22 / 2`와 같이 2를 3번만 사용하여 표현할 수 있습니다.

### 해결

```python
def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        num_set = { int(str(N) * i) }

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    num_set.add(x + y)
                    num_set.add(x - y)
                    num_set.add(x * y)

                    if y != 0:
                        num_set.add(x // y)

        if number in num_set:
            return i

        DP.append(num_set)

    return answer
```

### 설명

1. 주어진 숫자 N으로 각 횟수당 만들수 있는 숫자 조합을 만든다.
2. 만들어진 숫자 조합에 number로 주어진 숫자가 있는지 확인한다.
3. 만약 있다면 그 시점에서의 횟수를 답으로 리턴한다.
4. 없다면 횟수를 하나 늘리고 가능한 숫자 조합을 만들고 1~3을 반복한다.

### 출처

- https://programmers.co.kr/learn/courses/30/lessons/42895

