#include<stdio.h>
#include<string.h>
#include<stdbool.h> 
#define INF 7977880
#define V 6

int Graph[V][V] = {
  {0, 4, 0, 0, 0, 2},
  {4, 0, 6, 0, 0, 3},
  {0, 6, 0, 3, 0, 1},
  {0, 0, 3, 0, 2, 0},
  {0, 0, 0, 2, 0, 4},
    {2, 3, 1, 0, 4, 0}
};

int main() {
    int no_edges;
    int select[V];
    memset(select, false, sizeof(select));
    no_edges = 0;
    select[0] = true;
    int e;
    int A = 0;
    int f;
    printf("Edges : Weight\n");
    while (no_edges < V - 1) {

        int minimum = INF;
        e = 0;
        f = 0;

        for (int i = 0; i < V; i++) {
            if (select[i]) {
                for (int j = 0; j < V; j++) {
                    if (!select[j] && Graph[i][j]) {
                        if (minimum > Graph[i][j]) {
                            minimum = Graph[i][j];
                            e = i;
                            f = j;
                        }
                    }
                }
            }
        }
        printf("%c - %c : %d\n", (e + 97), (f + 97), Graph[e][f]);
        A += Graph[e][f];
        select[f] = true;
        no_edges++;
    }
    printf("MINIMUM SPANNING TREE COST: %d ", A);
    return 0;
}