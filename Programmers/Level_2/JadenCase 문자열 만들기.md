---
title: "프로그래머스 - JadenCase 문자열 만들기"
date: "2020-09-04T20:20:33.112"
category: "ps"
emoji: "📶"
---

## 프로그래머스 - JadenCase 문자열 만들기

- 관련된 알고리즘 : 문자열

### 문제 설명

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한 조건

- s는 길이 1 이상인 문자열입니다.
- s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

### 입출력 예

| s                     |        return         |
| --------------------- | :-------------------: |
| 3people unFollowed me | 3people Unfollowed Me |
| for the last week     |   For The Last Week   |

### 해결

```python
def solution(s):

    s = list(s.split(' '))
 	
    # 첫 문자 대문자로 바꾸기
    res = [i.capitalize() for i in s]

    return ' '.join(res)
```

### 설명

1. 문자열의 첫 문자를 대문자로 바꾸기 (capitalize()를 이용하면 쉽게 해결)

### 출처

- https://programmers.co.kr/learn/courses/30/lessons/12951