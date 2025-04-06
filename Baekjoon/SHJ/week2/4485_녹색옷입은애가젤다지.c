/* input
// 여러 테스트 케이스로 구성
    // 첫 줄: 동굴의 크기 N (2 ≤ N ≤ 125), 0 입력 시 종료
    // 이후 N줄: 각 줄마다 N개의 정수 (도둑루피 비용 0~9)
*/

/* output
    // 각 테스트 케이스마다
    // "Problem i: 최소 손실 루피" 형태로 출력
*/

/* process
    // 그래프 생성: N x N 격자 형태
    // 다익스트라 알고리즘 이용
        - 우선순위 큐(최소힙) 사용
        - 시작점 [0][0], 도착점 [N-1][N-1]
        - 상하좌우 4방향 이동
    // 최소 비용 누적 경로 찾기
*/


#include <stdio.h>
#include <stdlib.h>

#define MAX_N 125
#define INF 987654321

typedef struct{
    int x, y;
    int cost;
} Node;

Node heap[MAX_N * MAX_N];
int heapSize = 0;

int dx[5] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

void push(Node node) {
    int i = ++heapSize;
    while (i != 1 && node.cost < heap[i / 2].cost) {
        heap[i] = heap[i / 2];
        i /= 2;
    }
    heap[i] = node;
}

Node pop() {

    int parent = 1, child = 2;
    Node minNode = heap[parent];
    Node temp = heap[heapSize--];

    while (child <= heapSize) {
        if (child < heapSize && heap[child].cost > heap[child + 1].cost)
            child++;
        if (temp.cost <= heap[child].cost)
            break;
        heap[parent] = heap[child];
        parent = child;
        child *= 2;
    }
    heap[parent] = temp;
    return minNode;
}

int isInRange(int x, int y, int N){
    return (x >= 0 && y >= 0 && x < N && y < N);
}


void initDist(int N, int dist[MAX_N][MAX_N]) {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            dist[i][j] = INF;
}


void dijkstra(int N, int cave[MAX_N][MAX_N], int problemNum) {
    int dist[MAX_N][MAX_N];
    initDist(N, dist);

    heapSize = 0;
    dist[0][0] = cave[0][0];
    push((Node){0, 0, cave[0][0]});

    while (heapSize > 0) {
        Node now = pop();

        if (now.cost > dist[now.x][now.y])
            continue;

        for (int i = 0; i < 4; i++) {
            int nx = now.x + dx[i];
            int ny = now.y + dy[i];

            if (isInRange(nx, ny, N)) {
                int newCost = now.cost + cave[nx][ny];
                if (newCost < dist[nx][ny]) {
                    dist[nx][ny] = newCost;
                    push((Node){nx, ny, newCost});
                }
            }
        }
    }

    printf("Problem %d: %d\n", problemNum, dist[N - 1][N - 1]);
}

int main() {
    int N;
    int cave[MAX_N][MAX_N];
    int problemNum = 1;

    while (1) {
        scanf("%d", &N);
        if (N == 0)
            break;

        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                scanf("%d", &cave[i][j]);

        dijkstra(N, cave, problemNum++);
    }

    return 0;
}
