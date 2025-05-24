# [input]
# 첫째 줄: N, H, T (거인 수, 신티의 키, 망치 횟수)
# N개 줄: h (거인의 키)

# [output]
# 횟수 안에 거인의 키를 모두 센티보다 작게 만든 경우 (YES, 사용횟수)
# 그렇지 않은 경우 (NO, 가장 큰 거인의 키)

# [조건]
# 1 ≤ N ≤ 10^5
# 1 ≤ Hcenti ≤ 2 × 10^9
# 1 ≤ T ≤ 10^5
# 거인의 키가 1인 경우 반으로 줄일 수 없음

# [풀이방법]
# 완전 탐색으로 풀 시 O(T*N) => 10^10이므로 시간 초과
# 최댓값을 효율적으로 찾고 넣는 방식 => 우선순위큐
# 파이썬의 최소 힙을 이용해 값을 [음수]로 저장하여 최대 힙처럼 사용

import sys
import heapq

# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

max_heap = []
use = 0
N, H, T = map(int, input().split())

for _ in range(N):
    h = int(input())
    heapq.heappush(max_heap, -h)

for _ in range(T):
    val = -heapq.heappop(max_heap)
    if H > val:
        heapq.heappush(max_heap, -val)
        break
    if val == 1:
        heapq.heappush(max_heap, -val)
    else:
        use += 1
        heapq.heappush(max_heap, -(val // 2))

max_h = -heapq.heappop(max_heap)

if (H > max_h):
    print('YES')
    print(use)
else:
    print('NO')
    print(max_h)
