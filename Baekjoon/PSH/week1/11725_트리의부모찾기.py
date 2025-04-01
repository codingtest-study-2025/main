#import sys
#sys.stdin = open('input.txt')

from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [False] * (N + 1)
    parents = [0] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                parents[neighbor] = current
                visited[neighbor] = True
                queue.append(neighbor)

    return parents

result = bfs(1)

for i in range(2, N + 1):
    print(result[i])