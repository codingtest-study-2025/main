from sys import stdin as s

# sys.stdin = open('input.txt', 'r')
input = s.readline

# 문제명: 트리 (골드 4)

testcase = 1
result = ''
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    visited = [False for _ in range(n + 1)]

    def dfs(v, prev):
        visited[v] = True

        for next in graph[v]:
            # 방문 안 한 노드에 대해 dfs
            if not visited[next]:
                # dfs 결과가 사이클이면 return True
                if dfs(next, v):
                    return True
            # 방문했던 노드가 직전 노드가 아니면 사이클
            elif next != prev:
                return True
        # 사이클이 없으면 return False
        return False

    cnt = 0
    # 모든 노드에 대해 dfs
    for i in range(1, n + 1):
        if not dfs(i, 0):
            cnt += 1

    if cnt == 0:
        result += f'Case {testcase}: No trees.\n'
    elif cnt == 1:
        result += f'Case {testcase}: There is one tree.\n'
    else:
        result += f'Case {testcase}: A forest of {cnt} trees.\n'

    testcase += 1

print(result)
