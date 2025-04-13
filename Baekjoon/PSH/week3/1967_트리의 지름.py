""" 
input
    // 첫 번째 줄줄: 노드의 개수 n (1 ≤ n ≤ 10,000)
    // 둘째 줄 ~ n-1 개의 줄: 각 간선에 대한 정보
        // 첫 번째 정수: 부모 노드의 번호
        // 두 번째 정수: 자식 노드의 번호
        // 세 번째 정수: 간선의 가중치
    // 루트 노드의 번호: 항상 1
    // 간선의 가중치: 0 < n < 100

output
    // 트리의 지름 출력

process
    // 트리 구성: 양방향 연결이 가능한 인접 리스트트 
    // DFS 1
        // 지름의 한 쪽 끝을 찾기 위한 DFS
    // DFS 2
        // 지름의 다른 쪽 끝을 찾기 위한 DFS
"""

from collections import defaultdict
import sys

# 백준 입출력 관련 recursion 제한 해제
sys.setrecursionlimit(10**6) 
#sys.stdin = open('input.txt', 'r')

# 트리 입력 받기
n = int(input())
tree = defaultdict(list)

# 트리 구성: 양방향 연결이 가능한 인접 리스트
# 각 노드에 대해 부모 노드와 자식 노드, 가중치를 입력받아 트리 구성
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# DFS 함수
def dfs(node, distance):
    visited[node] = True # 무한루프 방지용
    global diameter, farthest_node 
    # 전역변수 사용을 위한 선언
    # 지름과 가장 먼 노드 저장을 위함

    if distance > diameter: # 현재 지름보다 길면 갱신
        diameter = distance # 지름 갱신
        farthest_node = node # 가장 먼 노드 갱신

    for neighbor, weight in tree[node]: # 탐색
        if not visited[neighbor]:
            dfs(neighbor, distance + weight) 
            # 재귀 호출
            # 현재까지 누적 거리 + 지금 가려는 거리

# 1차 DFS: 1번 노드에서 시작
visited = [False] * (n + 1) # 방문 여부 체크용
diameter = 0 # 초기화
farthest_node = 0 # 초기화
dfs(1, 0)

# 2차 DFS: farthest_node에서 다시 시작
visited = [False] * (n + 1) # 방문 여부 체크용
diameter = 0 # 초기화
dfs(farthest_node, 0)

# 출력: 트리의 지름
print(diameter)