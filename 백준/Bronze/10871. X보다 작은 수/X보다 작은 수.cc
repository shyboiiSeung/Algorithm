#include <stdio.h>

int main(void) {
    int N, X, a;
    scanf("%d %d", &N, &X);
    for (int i = 0; i < N; i++) {
        scanf("%d", &a);
        if (a < X) printf("%d ", a);
    }
}