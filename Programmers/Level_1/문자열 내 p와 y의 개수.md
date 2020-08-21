---
title: "프로그래머스 - 문자열 내 p와 y의 개수"
date: "2020-08-21T13:00:22.412Z"
category: "ps"
emoji: "⛺"
---

## 프로그래머스 - 문자열 내 p와 y의 개수

- 관련된 알고리즘 : .

### 문제 설명

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

### 제한사항

- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

------

### 입출력 예

| s       | answer |
| ------- | ------ |
| pPoooyY | true   |
| Pyy     | false  |

##### 입출력 예 설명

입출력 예 #1
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

입출력 예 #2
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

### 해결 1

```python
def solution(s):
    p_cnt, y_cnt = 0, 0
    S = s.upper()
    
    for i in range(len(S)):
        if S[i] in ['P', 'Y']:
            if S[i] == 'P':
                p_cnt += 1
            elif S[i] == 'Y':
                y_cnt += 1

    if p_cnt != y_cnt:
        return False
    
    return True
```

### 설명

없음.

### 해결 2

```python
def solution(s):
    p = s.upper().count('P')
    y = s.upper().count('Y')
    
    if p != y:
        return False
    
    return True
```

### 설명

1. count를 사용하면 쉽게 문자열안에 속해있는 문자의 갯수를 파악할 수 있다.

### 출처

- https://programmers.co.kr/learn/courses/30/lessons/12916
