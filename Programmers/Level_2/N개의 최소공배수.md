---
title: "프로그래머스 - N개의 최소공배수"
date: "2020-09-02T18:20:33.612"
category: "ps"
emoji: "📶"
---

## 프로그래머스 - N개의 최소공배수

- 관련된 알고리즘 : .

### 문제 설명

두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

### 제한 사항

- arr은 길이 1이상, 15이하인 배열입니다.
- arr의 원소는 100 이하인 자연수입니다.

### 입출력 예

| arr        | result |
| ---------- | ------ |
| [2,6,8,14] | 168    |
| [1,2,3]    | 6      |

### 해결

```python
# 최대공약수
def gcd(x, y):
    
    while y:
        x, y = y, x%y
        
    return x

# 최소공배수
def lcm(x, y):
    
    return x*y // gcd(x,y)

def solution(arr):
   
    while True:
        if len(arr) == 1:
            break
            
        a = arr.pop(0)
        b = arr.pop(0)
        c = lcm(a,b)
        arr.append(c)

    return arr[0]
```

### 설명

1. 전체 원소의 최소공배수를 구하기위해 2개의 원소에 대한 최소공배수를 구한다음 다시 배열에 넣어준다.

### 출처

- https://programmers.co.kr/learn/courses/30/lessons/12953