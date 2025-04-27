# [input]
# 첫 번째 줄: N
# N개 줄: 대나무 숲 정보 (ex. 1 14 3 5)

# [output]
# 이동할 수 있는 칸의 수의 최댓값

# [참고]
# 판다는 상하좌우로 이동
# 대나무가 더 많은 곳으로만 이동 가능

# [제한]
# 1 <= N <= 500
# 1 <= 대나무 <= 1,000,000

# [풀이방법]
# 모든 좌표마다 DFS 실행
# 단, 이미 계산된 값이 있으면 해당 값 사용하고 DFS 진행 X
#   - 가지치기 하지 않으면 최악의 경우 6.25 * 10^10
# 이동 칸수 최댓값 갱신

import sys
sys.setrecursionlimit(10**7)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dist = [[0] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def checkGraphSize(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def checkBamboo(prev, cur):
    x, y = prev
    nx, ny = cur
    return graph[nx][ny] > graph[x][y]

def dfs(x, y):
    if dist[x][y] != 0:
        return dist[x][y]

    dist[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if checkGraphSize(nx, ny) and checkBamboo((x, y), (nx, ny)):
            dist[x][y] = max(dist[x][y], dfs(nx, ny) + 1)

    return dist[x][y]

max_moves = 0
for i in range(N):
    for j in range(N):
        max_moves = max(max_moves, dfs(i, j))

print(max_moves)
