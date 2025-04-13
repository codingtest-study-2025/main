/* input
 // 첫 줄: 노드의 수 N (1 ≤ N ≤ 10,000)
 // 다음 N-1줄: 간선 정보 (부모, 자식, 가중치)
 // 노드는 1번부터 시작하며, 루트는 항상 1번
*/


/* output
 // 트리의 지름 (가장 긴 경로의 길이) 출력
*/


/* process
1. 트리 구성: 인접 리스트로 각 노드와 연결된 노드 및 가중치 저장
2. DFS를 두 번 수행:
    - 임의의 노드(보통 루트 1번)에서 가장 먼 노드 A를 찾기
    - A에서 다시 DFS하여 가장 먼 노드 B를 찾고, 이때 거리 = 지름
*/



#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 10001

typedef struct Node {
    int vertex;
    int weight;
    struct Node* next;
} Node;

Node* adj[MAX];
int visited[MAX];
int maxDist = 0;
int farthestNode = 0;

void add_edge(int from, int to, int weight) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = to;
    newNode->weight = weight;
    newNode->next = adj[from];
    adj[from] = newNode;
}

void dfs(int node, int dist) {
    visited[node] = 1;

    if (dist > maxDist) {
        maxDist = dist;
        farthestNode = node;
    }

    Node* curr = adj[node];
    while (curr) {
        if (!visited[curr->vertex]) {
            dfs(curr->vertex, dist + curr->weight);
        }
        curr = curr->next;
    }
}

int main(int argc, char * argv[]) {
    FILE * input = stdin;

    if(argc == 3 && strcmp(argv[1], "-f") == 0) {
      FILE * file = fopen(argv[2], "r");

      if(file){
        input = file;
      }
    }

    int n;
    fscanf(input, "%d", &n);

    for (int i = 0; i < n - 1; ++i) {
        int from, to, weight;
        fscanf(input, "%d %d %d", &from, &to, &weight);
        add_edge(from, to, weight);
        add_edge(to, from, weight);  // 무방향 그래프
    }

    // 첫 번째 DFS: 루트(1번)에서 가장 먼 노드 A 찾기
    memset(visited, 0, sizeof(visited));
    dfs(1, 0);

    // 두 번째 DFS: A에서 가장 먼 노드까지 거리 계산
    memset(visited, 0, sizeof(visited));
    maxDist = 0;
    dfs(farthestNode, 0);

    printf("%d\n", maxDist);

    if(input != stdin) fclose(input); 
    return 0;
}

