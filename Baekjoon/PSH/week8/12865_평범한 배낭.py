""" 
input
    여행에 필요한 물건 N개
        물건의 무게 W, 가치 V
        배낭에 넣을 수 있는 물건들의 가치의 최댓값

    // 첫째 줄: 
        물건의 수 N (1 ≤ N ≤ 100)
        버틸 수 있는 무게 K (1 ≤ K ≤ 100,000)      
    // 둘째 줄 ~ N+1번째 줄: 
        물건의 무게 W (1 ≤ W ≤ 100,000)
        가치 V (1 ≤ V ≤ 1,000)

output
    배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

process
    시간 제한 2 초, 메모리 제한 512 MB 고려

    완전 탐색으로 진행하는 경우, '시간 제한 2초'에 문제 발생
    해결: DP 사용
    K 최대 무게부터 내려오는 방식으로 검사를 진행하여야 함
        같은 물건을 여러 번 넣는 것을 방지하기 위함
"""

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

#import heapq
#from collections import deque
#sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
# 물건 개수, 최대 무게 할당
items = [list(map(int, input().split())) for _ in range(N)]
# (무게, 가치) 배열 생성

dp = [0] * (K + 1)
# dp 배열 초기화

for weight, value in items:
    # 각 물건의 무게와 가치 확인인
    for w in range(K, weight - 1, -1):
        # 최대 무게 K부터 현재 물건 무게까지 거꾸로 검사
        # 같은 물건을 여러 번 넣는 걸 방지

        dp[w] = max(dp[w], dp[w - weight] + value)
        # 현재 무게에서의 최대 가치를 갱신 (안 넣는 경우 vs 넣는 경우)

print(dp[K])