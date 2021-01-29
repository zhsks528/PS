# 35분
# 도움&참조 : O

# 1. 입력값을 이용하여 그래프를 생성한다
# 2. 시작 노드를 다르게 하여 DFS로 노드를 탐색한다.


def dfs(node, count):
    global result

    if result < count:
        result = count

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, count+1)
            visited[next_node] = False


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = {node: [] for node in range(1, n+1)}
    visited = [False] * (n+1)
    result = 0

    # 1
    for i in range(m):
        node_a, node_b = map(int, input().split())
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    # 2
    for node in range(1, n+1):
        visited[node] = True
        dfs(node, 1)
        visited[node] = False

    print("#{0} {1}".format(tc, result))
