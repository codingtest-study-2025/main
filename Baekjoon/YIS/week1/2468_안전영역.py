import sys
input = sys.stdin.readline  # 일반 input보다 훨씬 빠름
sys.setrecursionlimit(10**6)  # 백준 recursion 제한 해제

# sys.stdin = open('input.txt', 'r')

# 기본 변수
n = int(input().strip())
max_rain_level = 101
answer = 0
graph = []

# 방향 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# graph 생성
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)


def can_visit_dfs(nx, ny, h):
    return (0 <= nx < n) and (0 <= ny < n) and (graph[nx][ny] > h) and not visited[nx][ny]


def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if can_visit_dfs(nx, ny, h):
            visited[nx][ny] = True
            dfs(nx, ny, h)


def init_visited():
    return [[False] * n for _ in range(n)]


for rain_level in range(max_rain_level):
    # visited 초기화
    visited = init_visited()
    count = 0

    # 모든 좌표에 대한 dfs 실행
    for i in range(n):
        for j in range(n):
            if (graph[i][j] > rain_level) and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dfs(i, j, rain_level)

    answer = max(answer, count)

print(answer)
