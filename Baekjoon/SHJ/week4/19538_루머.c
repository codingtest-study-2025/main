/* input
   // 첫 줄: 사람 수 N (1 ≤ N ≤ 200,000)
   // 다음 N줄: 주변인의 번호와 입력의 마지막(0)
   // N+1 줄 : 루머를 퍼뜨리는 최소 유포자의 수 : M 
   // N+2 줄 : 최초 유포자의 번호 (공백으로 구분)
*/

/* output
   // N개의 정수 시간단위로 출력 (tn 시간이 지나도 루머를 믿지 않을 경우 -1) 
*/

/* process
   1. 인접 리스트 생성
   2. 최초 유포자 정보 저장 (루머 시간 = 0, BFS 큐에 추가)
   3. BFS 시작
    1) 현재 사람의 모든 이웃에게 루머 전파
    2) 각 이웃은 주변인의 절반 이상이 믿으면, 믿기 시작함
    3) 믿게 되는 순간 루머 시간 기록 + 큐에 추가
   4. 모든 사람의 루머 시간 출력
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 200001
FILE *input = NULL;

typedef struct node {
    int val;
    struct node *next;
} Adj;

Adj *adj[MAX];  // 인접 리스트
int rumorTime[MAX]; // 루머 믿기 시작한 시간
int believeCount[MAX]; // 주변인 중 루머 믿는 사람 수
int totalNeighbor[MAX]; // 주변인 수

int queue[MAX];
int front = 0, rear = 0;

void enqueue(int x) { queue[rear++] = x; }
int dequeue() { return queue[front++]; }
int isEmpty() { return front == rear; }

void addEdge(int u, int v) {
    Adj *newNode = malloc(sizeof(Adj));
    newNode->val = v;
    newNode->next = adj[u];
    adj[u] = newNode;

    totalNeighbor[u]++;
}
    

void makeGraph(FILE *input, int N) {
    for (int i = 1; i <= N; i++) {
        int v;
        while (1) {
            fscanf(input, "%d", &v);
            if (v == 0) break;

            addEdge(i, v);
            addEdge(v, i); 
        }
    }
}

void bfs() {
    while (!isEmpty()) {
        int curr = dequeue();

        for (Adj *p = adj[curr]; p; p = p->next) {
            int next = p->val;
            if (rumorTime[next] != -1) continue;

            believeCount[next]++;
            if (believeCount[next] >= (totalNeighbor[next] + 1) / 2) {
                rumorTime[next] = rumorTime[curr] + 1;
                enqueue(next);
            }
        }
    }
}

int main(int argc, char *argv[]) {
    input = stdin;

    if (argc == 3 && strcmp(argv[1], "-f") == 0) {
        FILE* file = fopen(argv[2], "r");
        if (!file) {
            fprintf(stderr, "파일 열기 실패: %s\n", argv[2]);
            return 1;
        }
        input = file;
    }
    int N;
    fscanf(input, "%d", &N);
    makeGraph(input, N);

    for (int i = 1; i <= N; i++) rumorTime[i] = -1;

    int M;
    fscanf(input, "%d", &M);

    for (int i = 0; i < M; i++) {
        int x;
        fscanf(input, "%d", &x);
        rumorTime[x] = 0;
        enqueue(x);
    }

    bfs();

    for (int i = 1; i <= N; i++) {
        printf("%d ", rumorTime[i]);
    }

    if (input != stdin) fclose(input);
    return 0;
}

