# [input]
# 첫째 줄: W H (맵 크기)
# H개 줄: 지도 정보

# [output]
# 최소 거울 설치 개수

# [조건]
# 1 <= W, H <= 100
# c는 항상 두 칸
# 거울의 종류는 두 개

# [풀이방법]
# 거울 사용 개수를 비용으로 생각하면 최단 거리 문제로 확장할 수 있으므로 다익스트라 사용
# 노드에는 '방향 정보'도 필요함 => 꺾을 때 거울을 추가해야 하므로
# 우선순위 큐에 시작점으로부터 네 방향을 넣어주고 시작

import sys
import math
import heapq

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

W, H = map(int, input().split())

# 그래프 생성
graph = []
for _ in range(H):
    line = list(input().rstrip())
    graph.append(line)

# c좌표 찾기
c_pos = []
for y in range(H):
    for x in range(W):
        if graph[y][x] == 'C':
            c_pos.append((y, x))
(sy, sx) = c_pos[0]
(ey, ex) = c_pos[1]


# 상하좌우
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = math.inf

# dist 초기화
# dist[y][x][d]: (y,x)에 방향 d 로 진입했을 때 최소 거울 수
dist = [[[INF]*4 for _ in range(W)] for __ in range(H)]
pq = []

# 시작점에서는 네 방향 모두 거울 0개로 진입 가능
for d in range(4):
    dist[sy][sx][d] = 0
    heapq.heappush(pq, (0, sy, sx, d))

# 다익스트라
while pq:
    mirror_cnt, y, x, d = heapq.heappop(pq)
    # 이미 최소이면 건너뛰기
    if mirror_cnt > dist[y][x][d]:
        continue
    for nd, (dy, dx) in enumerate(dirs):
        ny, nx = y + dy, x + dx
        # 맵을 벗어나거나 벽에 부딪히면 건너뛰기
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if graph[ny][nx] == '*':
            continue
        # 방향이 다르면 거울 추가
        new_cnt = mirror_cnt
        if nd != d:
            new_cnt += 1
        # 새로 계산한 거울 수가 최소이면 우선순위큐에 넣기
        if new_cnt < dist[ny][nx][nd]:
            dist[ny][nx][nd] = new_cnt
            heapq.heappush(pq, (new_cnt, ny, nx, nd))

# 도착점 네 방향 중 최솟값 출력
answer = min(dist[ey][ex])
print(answer)
