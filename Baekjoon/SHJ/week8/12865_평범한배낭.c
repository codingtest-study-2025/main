/* input
 // 첫 줄: 물건 개수, 버틸 수 있는 최대 무게
 // 다음 N줄: 각 줄에 물건의 무게 W, 가치 V (정수)
*/

/* output
 // 배낭에 넣을 수 있는 물건들의 가치 합의 최댓값 출력
*/

/* process
 - 각 물건은 한 번만 선택 가능
 - dp[i]: 무게 i를 채울 수 있을 때의 최대 가치
 - 점화식 (뒤에서부터 갱신): dp[i] = max(dp[i], dp[i - weight] + value)
 - dp 배열 크기: K+1
 - N개의 물건에 대해 위 연산 반복
 - 최종 결과: dp[K] (무게 K 이하로 담았을 때 최대 가치)
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_K 100001
#define MAX_N 101

int dp[MAX_K]; 
int weight[MAX_N], value[MAX_N];

int main(int argc, char* argv[]) {
    FILE* input = stdin;

    if (argc == 3 && strcmp(argv[1], "-f") == 0) {
        FILE* file = fopen(argv[2], "r");
        if (!file) {
            fprintf(stderr, "파일 열기 실패: %s\n", argv[2]);
            return 1;
        }
        input = file;
    }

    int N, K;
    fscanf(input, "%d %d", &N, &K);

    for (int i = 0; i < N; i++) {
        fscanf(input, "%d %d", &weight[i], &value[i]);
    }

    for (int i = 0; i < N; i++) {
        for (int j = K; j >= weight[i]; j--) {
            if (dp[j] < dp[j - weight[i]] + value[i]) {
                dp[j] = dp[j - weight[i]] + value[i];
            }
        }
    }

    printf("%d\n", dp[K]);

    if (input != stdin) fclose(input);

    return 0;
}

