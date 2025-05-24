# [input]
# 첫째 줄: N, K (물건 개수, 배낭 무게 한도)
# N개 줄: W, V (무게, 가치)

# [output]
# K 한도 안에서 가장 높은 가치

# [조건]
# 1 ≤ N ≤ 100
# 1 ≤ K ≤ 10^5
# 1 ≤ W ≤ 10^5

# [풀이방법]
# 모든 물건의 조합을 시도하면 O(N * 2^N) => 2^100 시간초과
# dp를 사용하여 한 번씩만 계산하면서 최적의 해를 찾기
# dp[w] = max(dp[w], dp[w-(물건 무게)] + 물건 가치)
# K부터 물건의 무게까지 거꾸로 내려오면서 계산 => 앞에서부터 올라가면 지금 넣은 물건이 다음 칸에 반영되어 중복 계산되는 상황 발생

import sys

# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
items = []
dp = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())

    for w in range(K, W - 1, -1):
        dp[w] = max(dp[w], dp[w-W] + V)

print(dp[K])
