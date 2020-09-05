---
title: "프로그래머스 - 2xn 타일링"
date: "2020-09-05T16:33:11.665"
category: "ps"
emoji: "📶"
---

## 프로그래머스 - 압축

- 관련된 알고리즘 : 다이나믹 프로그래밍

### 문제 설명

가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

- 타일을 가로로 배치 하는 경우
- 타일을 세로로 배치 하는 경우

예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

![Imgur](https://i.imgur.com/29ANX0f.png)

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

### 제한사항

- 가로의 길이 n은 60,000이하의 자연수 입니다.
- 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

### 입출력 예

| n    | result |
| ---- | ------ |
| 4    | 5      |

##### 입출력 예 설명

입출력 예 #1
다음과 같이 5가지 방법이 있다.

![Imgur](https://i.imgur.com/keiKrD3.png)

![Imgur](https://i.imgur.com/O9GdTE0.png)

![Imgur](https://i.imgur.com/IZBmc6M.png)

![Imgur](https://i.imgur.com/29LWVzK.png)

![Imgur](https://i.imgur.com/z64JbNf.png)

### 해결 1

```python
def solution(n):
    
    dp = [0,1,2]
    
    for i in range(3, n+1):
        dp.append((dp[i-2] + dp[i-1])% 1000000007) 

    return dp[n]
```

### 설명

없음.

### 해결 2

```python
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    
    for i in range(3, n+1):
        a, b = b, a+b 

    return b % 1000000007
```

### 설명

없음.

### 출처

- https://programmers.co.kr/learn/courses/30/lessons/12900

