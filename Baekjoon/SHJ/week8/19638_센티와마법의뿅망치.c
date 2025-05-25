/* input
 // 첫 줄: 거인 수, 센티 키, 뿅망치 사용 제한
 // 다음 N줄: 각 거인의 키 H (1 ≤ H ≤ 2×10^9)
*/

/* output
 // 모든 거인이 센티보다 작아지면
 //    YES
 //    최소 사용한 횟수
 // 남은 횟수를 다 써도 센티보다 크거나 같은 거인이 있으면
 //    NO
 //    가장 큰 거인의 키
*/

/* process
 - 센티보다 큰 거인들을 뿅망치로 줄임
 - 항상 가장 키 큰 거인을 때림 ->  우선순위 큐(최대 힙) 사용

   1. 모든 거인의 키를 최대 힙에 삽입
   2. T번 또는 조건 만족까지 반복:
      - 키 가장 큰 거인을 꺼내서
      - 키 ≥ 센티일 경우 키 반으로 줄임 (키가 1이면 줄이지 x) 
      - 줄인 값을 다시 힙에 삽입
   3. 반복 도중에 모든 거인이 센티보다 작아지면 YES + 사용 횟수 출력
   4. 끝까지 안 되면 NO + 힙에서 가장 큰 값 출력
*/


#include <stdio.h>
#include <stdlib.h>

#define MAX_N 100005

typedef struct {
    int size;
    long long data[MAX_N];
} MaxHeap;

void swap(long long* a, long long* b) {
    long long temp = *a;
    *a = *b;
    *b = temp;
}

void push(MaxHeap* h, long long value) {
    int i = ++(h->size);
    h->data[i] = value;

    while (i > 1 && h->data[i] > h->data[i / 2]) {
        swap(&h->data[i], &h->data[i / 2]);
        i /= 2;
    }
}

long long top(MaxHeap* h) {
    return h->data[1];
}

void pop(MaxHeap* h) {
    h->data[1] = h->data[h->size--];

    int i = 1;
    while (1) {
        int left = i * 2, right = i * 2 + 1;
        int largest = i;

        if (left <= h->size && h->data[left] > h->data[largest]) largest = left;
        if (right <= h->size && h->data[right] > h->data[largest]) largest = right;

        if (largest == i) break;

        swap(&h->data[i], &h->data[largest]);
        i = largest;
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

    int N, T;
    long long Hcenti;
    fscanf(input, "%d %lld %d", &N, &Hcenti, &T);

    MaxHeap heap = {0};

    for (int i = 0; i < N; i++) {
        long long h;
        fscanf(input, "%lld", &h);
        push(&heap, h);
    }

    int used = 0;
    while (T-- > 0) {
        if (top(&heap) < Hcenti) break;

        long long tallest = top(&heap);
        pop(&heap);

        if (tallest == 1) {
            push(&heap, 1); // 더 줄수 x
            break;
        }

        push(&heap, tallest / 2);
        used++;
    }

    if (top(&heap) < Hcenti) {
        printf("YES\n%d\n", used);
    } else {
        printf("NO\n%lld\n", top(&heap));
    }

    if (input != stdin) fclose(input);

    return 0;
}

