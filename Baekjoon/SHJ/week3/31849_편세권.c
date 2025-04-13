/* input
    // 첫 줄: 지도 크기 (N x M), 방의 개수 R, 편의점 개수 C
    // 다음 R줄: 각 방의 위치 (a, b)와 월세 p
    // 다음 C줄: 각 편의점의 위치 (c, d)
*/

/* output
    // 가장 낮은 편세권 점수를 출력
    // 편세권 점수 = (방에서 가장 가까운 편의점까지의 거리) × (월세)
*/

/* process
    // 1. 모든 편의점 위치를 큐에 넣고 BFS 수행
        // - 각 좌표에서 가장 가까운 편의점까지의 거리 계산
    // 2. 모든 방의 위치에서 거리 배열을 참조하여 점수 계산
    // 3. 그 중 최소값을 출력
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1001
#define INF 1000000000


typedef struct {
    int x, y;
} Point;

typedef struct {
    int x, y, dist;
} QueueNode;

int N, M, R, C;
int dist[MAX][MAX];
int dx[] = {1, -1, 0, 0}; 
int dy[] = {0, 0, 1, -1};
QueueNode queue[MAX * MAX];
int front = 0, rear = 0;

void bfs(Point* convenience) {
    while (front < rear) {
        QueueNode node = queue[front++];
        for (int i = 0; i < 4; ++i) {
            int nx = node.x + dx[i];
            int ny = node.y + dy[i];
            if (nx >= 1 && nx <= N && ny >= 1 && ny <= M) {
                if (dist[nx][ny] > node.dist + 1) {
                    dist[nx][ny] = node.dist + 1;
                    queue[rear++] = (QueueNode){nx, ny, node.dist + 1};
                }
            }
        }
    }
}

int main(int argc, char* argv[]) {
    FILE* input = stdin;

    if (argc == 3 && strcmp(argv[1], "-f") == 0) {
        FILE* file = fopen(argv[2], "r");
        if (file) input = file;
    }

    fscanf(input, "%d %d %d %d", &N, &M, &R, &C);

    Point rooms[R];
    int rent[R];
    for (int i = 0; i < R; ++i) {
        int x, y, p;
        fscanf(input, "%d %d %d", &x, &y, &p);
        rooms[i] = (Point){x, y};
        rent[i] = p;
    }

    for (int i = 0; i <= N; ++i)
        for (int j = 0; j <= M; ++j)
            dist[i][j] = INF;

    for (int i = 0; i < C; ++i) {
        int x, y;
        fscanf(input, "%d %d", &x, &y);
        dist[x][y] = 0;
        queue[rear++] = (QueueNode){x, y, 0};
    }

    // 편의점으로부터 최단 거리 계산
    bfs(NULL);

    // 최소 편세권 점수 계산
    int min_score = INF;
    for (int i = 0; i < R; ++i) {
        int x = rooms[i].x;
        int y = rooms[i].y;
        int score = dist[x][y] * rent[i];
        if (score < min_score) min_score = score;
    }

    printf("%d\n", min_score);

    if (input != stdin) fclose(input);
    return 0;
}

