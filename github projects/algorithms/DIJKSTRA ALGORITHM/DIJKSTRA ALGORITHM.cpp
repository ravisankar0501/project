#include<stdio.h>
#include<string.h>
#include<stdbool.h> 
#define INFINITY 6698898
#define MAX 10

void Dijkstra(int G[MAX][MAX], int n, int begin);

void Dijkstra(int G[MAX][MAX], int n, int begin) {
    int mincost[MAX][MAX], dist[MAX], pred[MAX];
    int visit[MAX], count, minimumdist, next_node, i, j;

    // Creating cost matrix
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            if (G[i][j] == 0)
                mincost[i][j] = INFINITY;
            else
                mincost[i][j] = G[i][j];

    for (i = 0; i < n; i++) {
        dist[i] = mincost[begin][i];
        pred[i] = begin;
        visit[i] = 0;
    }

    dist[begin] = 0;
    visit[begin] = 1;
    count = 1;

    while (count < n - 1) {
        minimumdist = INFINITY;

        for (i = 0; i < n; i++)
            if (dist[i] < minimumdist && !visit[i]) {
                minimumdist = dist[i];
                next_node = i;
            }

        visit[next_node] = 1;
        for (i = 0; i < n; i++)
            if (!visit[i])
                if (minimumdist + mincost[next_node][i] < dist[i]) {
                    dist[i] = minimumdist + mincost[next_node][i];
                    pred[i] = next_node;
                }
        count++;
    }

    // TO print the distance
    for (i = 0; i < n; i++)
        if (i != begin) {
            printf("\nDistance from a to %c: %d", i + 97, dist[i]);
        }
}
int main() {
    int G[MAX][MAX], i, j, n, u;
    n = 6;

    G[0][0] = 0;
    G[0][1] = 10;
    G[0][2] = 15;
    G[0][3] = 0;
    G[0][4] = 0;
    G[0][5] = 0;

    G[1][0] = 0;
    G[1][1] = 0;
    G[1][2] = 0;
    G[1][3] = 12;
    G[1][4] = 0;
    G[1][5] = 15;

    G[2][0] = 0;
    G[2][1] = 0;
    G[2][2] = 0;
    G[2][3] = 0;
    G[2][4] = 10;
    G[2][5] = 0;

    G[3][0] = 0;
    G[3][1] = 0;
    G[3][2] = 0;
    G[3][3] = 0;
    G[3][4] = 2;
    G[3][5] = 1;

    G[4][0] = 0;
    G[4][1] = 0;
    G[4][2] = 0;
    G[4][3] = 0;
    G[4][4] = 0;
    G[4][5] = 5;

    G[5][0] = 0;
    G[5][1] = 0;
    G[5][2] = 0;
    G[5][3] = 0;
    G[5][4] = 0;
    G[5][5] = 0;


    u = 0;
    Dijkstra(G, n, u);

    return 0;
}