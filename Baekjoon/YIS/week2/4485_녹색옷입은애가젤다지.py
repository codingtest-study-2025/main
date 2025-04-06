import sys
import heapq

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


# 동굴에서 움직일 수 있는지 확인
def canMove(n, x, y):
    return 0 <= x < n and 0 <= y < n


# 다익스트라 (2차원 그리드)
def dijkstra_2d(grid, start, end):
    n = len(grid)
    INF = int(1e9)

    # 초기값 설정
    start_x, start_y = start[0], start[1]

    # distance (n * n) 초기화
    dist = [[INF] * n for _ in range(n)]

    dist[start_x][start_y] = grid[start_x][start_y]

    queue = []
    heapq.heappush(queue, (dist[start_x][start_y], start_x, start_y))

    # 상하좌우 오프셋 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        # 누적 루피가 가장 작은 작업 pop (튜플 첫 번재 요소가 작은 것)
        cost, x, y = heapq.heappop(queue)

        # 도착점이면 조기 종료
        if (x, y) == end:
            return cost

        # 이미 더 짧은 게 있으면 무시
        if dist[x][y] < cost:
            continue

        # 상하좌우로 인접한 칸에 대해 다익스트라 수행
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if canMove(n, nx, ny):
                new_cost = cost + grid[nx][ny]

                # 기존 루피보다 작으면 갱신하고 우선순위큐에 넣기
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(queue, (new_cost, nx, ny))

    return dist[end[0]][end[1]]


count = 1

# 문제마다 동굴 생성 후 답 찾기
while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    for i in range(n):
        line = list(map(int, input().split(' ')))
        graph.append(line)

    start = (0, 0)
    end = (n-1, n-1)

    result = dijkstra_2d(graph, start, end)

    print(f"Problem {count}: {result}")
    count += 1
