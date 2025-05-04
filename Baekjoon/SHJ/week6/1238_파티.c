/* input
 // 첫 줄: 정수 N (마을 수), M (도로 수), X (파티 마을 번호)
 // 다음 M줄: A B T (A번 마을에서 B번 마을까지 가는 데 T 시간)
*/

/* output
 // 모든 학생들이 X번 마을까지 갔다가 집으로 돌아오는 데 걸리는 시간 중 가장 긴 시간 출력
*/

/* process
 - 모든 마을 i에서 X로 가는 최단 시간
 - X에서 모든 마을 i로 돌아오는 최단 시간
 - i 마을 학생의 왕복 시간 = i->X 최단거리 + X->i 최단거리
 - 그 중 최댓값

 - Dijkstra 2번 실행
   1. 정방향: X->모든 마을 거리 (X 기준)
   2. 역방향: 모든 마을->X 거리 (역방향 그래프에서 X 기준)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 1001
#define INF 1000000000

typedef struct Edge {
    int to;
    int cost;
    struct Edge* next;
} Edge;

Edge* forwardGraph[MAX_N];
Edge* reverseGraph[MAX_N];

int distToX[MAX_N];   // i->X
int distFromX[MAX_N]; // X->i
int n, m, x;

void addEdge(Edge* graph[], int from, int to, int cost) {
    Edge* newEdge = (Edge*)malloc(sizeof(Edge));
    newEdge->to = to;
    newEdge->cost = cost;
    newEdge->next = graph[from];
    graph[from] = newEdge;
}

int getMinIndex(int* dist, int* visited) {
    int min = INF, idx = -1;
    for (int i = 1; i <= n; i++) {
        if (!visited[i] && dist[i] < min) {
            min = dist[i];
            idx = i;
        }
    }
    return idx;
}

void dijkstra(Edge* graph[], int start, int* dist) {
    int visited[MAX_N] = {0};
    for (int i = 1; i <= n; i++) dist[i] = INF;
    dist[start] = 0;

    for (int i = 1; i <= n; i++) {
        int u = getMinIndex(dist, visited);
        if (u == -1) break;
        visited[u] = 1;

        for (Edge* e = graph[u]; e != NULL; e = e->next) {
            int v = e->to;
            int w = e->cost;
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
            }
        }
    }
}

void freeGraph(Edge* graph[]) {
    for (int i = 1; i <= n; i++) {
        Edge* cur = graph[i];
        while (cur) {
            Edge* temp = cur;
            cur = cur->next;
            free(temp);
        }
    }
}

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

    fscanf(input, "%d %d %d", &n, &m, &x);
    for (int i = 0; i < m; i++) {
        int from, to, time;
        fscanf(input, "%d %d %d", &from, &to, &time);
        addEdge(forwardGraph, from, to, time);   // X->i용
        addEdge(reverseGraph, to, from, time);   // i->X용 (역방향)
    }

    dijkstra(forwardGraph, x, distFromX);   // X->i
    dijkstra(reverseGraph, x, distToX);     // i->X

    int maxTime = 0;
    for (int i = 1; i <= n; i++) {
        int roundTrip = distFromX[i] + distToX[i]; // i->X + X->i
        if (roundTrip > maxTime) maxTime = roundTrip;
    }

    printf("%d\n", maxTime);

    freeGraph(forwardGraph);
    freeGraph(reverseGraph);

    return 0;
}
