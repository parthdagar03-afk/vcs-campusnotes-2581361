#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#define MAXV 600
#define MAXE 20000
#define INF (LLONG_MAX / 4)
typedef long long LL;
typedef struct { int u, v; LL w; } Edge;
typedef struct { int to, next; LL w; } Arc;
static int V, E, head[MAXV], tail[MAXV], arcCount;
static Edge edges[MAXE];
static Arc arcs[2 * MAXE];
static void fail(const char *s) {
    fprintf(stderr, "%s\n", s); exit(EXIT_FAILURE);
}
static void addArc(int u, int v, LL w) {
    int k = arcCount++;
    arcs[k] = (Arc){v, -1, w};
    if (head[u] == -1) head[u] = k;
    else arcs[tail[u]].next = k;
    tail[u] = k;
}
/* weighted=1: read u v w; weighted=0: read u v. */
static void readGraph(int directed, int weighted) {
    if (scanf("%d%d", &V, &E) != 2 || V < 1 ||
        V > MAXV || E < 0 || E > MAXE) fail("Invalid V/E");
    for (int i = 0; i < V; ++i) head[i] = tail[i] = -1;
    arcCount = 0;
    for (int i = 0; i < E; ++i) {
        int u, v; LL w = 1;
        if (scanf("%d%d", &u, &v) != 2) fail("Invalid edge");
        if (weighted && scanf("%lld", &w) != 1)
            fail("Invalid weight");
        if (u < 0 || u >= V || v < 0 || v >= V || u == v ||
            w < -1000000000LL || w > 1000000000LL)
            fail("Invalid endpoint/weight or self-loop");
        edges[i] = (Edge){u, v, w};
        addArc(u, v, w);
        if (!directed) addArc(v, u, w);
    }
}
static void showTime(clock_t a, clock_t b) {
    printf("Time (seconds): %.9f\n", (double)(b-a)/CLOCKS_PER_SEC);
}

static int parent[MAXV], rankDSU[MAXV], used;
static Edge selected[MAXV], temp[MAXE];
static LL cost;
static int find(int x) {
    if (parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
}
static int unite(int a, int b) {
    a = find(a); b = find(b);
    if (a == b) return 0;
    if (rankDSU[a] < rankDSU[b]) { int t=a; a=b; b=t; }
    parent[b] = a;
    if (rankDSU[a] == rankDSU[b]) ++rankDSU[a];
    return 1;
}
static int before(Edge a, Edge b) {
    if (a.w != b.w) return a.w < b.w;
    if (a.u != b.u) return a.u < b.u;
    return a.v <= b.v;
}
static void sortEdges(int l, int r) {
    if (r-l <= 1) return;
    int m=l+(r-l)/2;
    sortEdges(l,m); sortEdges(m,r);
    int i=l, j=m, k=l;
    while (i<m && j<r)
        temp[k++] = before(edges[i],edges[j]) ? edges[i++] : edges[j++];
    while (i<m) temp[k++] = edges[i++];
    while (j<r) temp[k++] = edges[j++];
    for (i=l; i<r; ++i) edges[i] = temp[i];
}
static void kruskal(void) {
    used=0; cost=0;
    for (int i=0; i<V; ++i) { parent[i]=i; rankDSU[i]=0; }
    sortEdges(0,E);
    for (int i=0; i<E && used<V-1; ++i)
        if (unite(edges[i].u,edges[i].v)) {
            selected[used++] = edges[i]; cost += edges[i].w;
        }
}
int main(void) {
    readGraph(0,1);
    clock_t a=clock(); kruskal(); clock_t b=clock();
    if (used != V-1) puts("Disconnected graph: no spanning tree");
    else {
        puts("MST edges (u v weight):");
        for (int i=0; i<used; ++i)
            printf("%d %d %lld\n",selected[i].u,selected[i].v,selected[i].w);
        printf("MST cost: %lld\n",cost);
    }
    showTime(a,b); return 0;
}
