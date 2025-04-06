/* input
// 전위 순회로 주어진 이진 검색 트리
    // 각 줄마다 노드 키 (1 ≤ 키 < 1,000,000)
    // 입력 끝은 EOF
*/

/* output
    // 후위 순회 결과를 한 줄에 하나씩 출력
*/

/* process
    // 전위 순회 첫 번째 값이 루트
    // 왼쪽은 루트보다 작은 값, 오른쪽은 큰 값
    // 전위 순회 기반으로 BST 재귀적으로 구성
    // 구성된 트리를 후위 순회 (왼 → 오 → 루트) 하면서 출력
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 10000

int preorder[MAX];
int size = 0;

typedef struct Node {
    int key;
    struct Node* left;
    struct Node* right;
} Node;

Node* newNode(int key) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// 전위 순회를 기반으로 Binary Search Tree 구성
Node* buildBST(int start, int end) {
    if (start > end) return NULL;

    Node* root = newNode(preorder[start]);

    int idx = start + 1;
    while (idx <= end && preorder[idx] < root->key) {
        idx++;
    }
    root->left = buildBST(start + 1, idx - 1);
    root->right = buildBST(idx, end);
    return root;
}

// 후위 순회 (왼 → 오 → 루트)
void postorder(Node* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d\n", root->key);
}

int main() {
    while (scanf("%d", &preorder[size]) != EOF) {
        size++;
    }

    Node* root = buildBST(0, size - 1);
    postorder(root);
    return 0;
}
