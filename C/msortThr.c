/* msortThr.c */
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

typedef struct Point {int d2, i, j, k;} Point;
int compar (Point ptA, Point ptB);
void merge(int r1, int r2, int *N, Point **ls);
int main(int argc, char **argv) {
   int M = atoi(argv[1]);
   int p = 0;
#pragma omp parallel
   {
	   if (omp_get_thread_num() == 0) p = omp_get_num_threads();
   }
   //printf("Num of threads: %d\n", p);
   double begin = omp_get_wtime();
   int Ntot = (M+1)*(M+2)*(M+3)/6;  // length of list
   // partition the list among p sublists and sort each one
   Point *ls[p];
   int N[p];
#pragma omp parallel
   {
	   int r = omp_get_thread_num();
	   // construct r-th sublist
	   N[r] = Ntot / p;
	   if (r < Ntot % p) N[r]++;
	   Point *lsr = ls[r] = (Point *)malloc(N[r] * sizeof(Point));
	   int n = 0;
	   for (int k = 0; k <= M; k++)
		   for (int j = 0; j <= k; j++)
			   for (int i = 0; i <= j; i++) {
		          if (n % p == r) {
			         Point lsrnbyp = { i*i + j*j + k*k, i, j, k };
			         lsr[n / p] = lsrnbyp;
		          }
		          n++;
			   }
	   // do an insertion sort
	   for (int n = 0; n < N[r]; n++)
		   for (int m = n; m > 0 && compar(lsr[m], lsr[m - 1]) < 0; m--) {
		      Point lsrm = lsr[m]; lsr[m] = lsr[m - 1]; lsr[m - 1] = lsrm;
		   }
	   int p0 = p;  // number of sublists
	   int p1 = 1;
	   while (2 * p1 < p0) p1 *= 2;  // p1 = next value of p0
	   while (p0 > 1) {
#pragma omp barrier
		   if (r < p0 - p1) merge(r, p1 + r, N, ls);
		   p0 = p1; p1 /= 2;
	   }
   }
   double end = omp_get_wtime();
   printf("nthreads = %2d, nparts = %2d, time = %.3lf\n", p, p, end - begin);
   FILE *sorted = fopen("sorted.txt", "w");
   for (int n = 0; n < Ntot; n++) {
      Point pt = ls[0][n];
      fprintf(sorted,"%d %d %d %d\n", pt.d2, pt.i, pt.j, pt.k);
   }
   fclose(sorted);
}
int compar (Point ptA, Point ptB) {
   if (ptA.d2 < ptB.d2) return -1;
   else if (ptA.d2 > ptB.d2) return 1;
   else if (ptA.i < ptB.i) return -1;
   else if (ptA.i > ptB.i) return 1;
   else if (ptA.j < ptB.j) return -1;
   else if (ptA.j > ptB.j) return 1;
   else if (ptA.k < ptB.k) return -1;
   else if (ptA.k > ptB.k) return 1;
   else return 0;}
void merge(int r1, int r2, int *N, Point **ls) {
   int N3 = N[r1] + N[r2];
   Point *ls1 = ls[r1], *ls2 = ls[r2];
   Point *ls3 = (Point *)malloc(N3*sizeof(Point));
   for (int n1 = 0, n2 = 0, n = 0; n < N3; n++)
      if (n2 == N[r2] || n1 < N[r1] && compar(ls1[n1], ls2[n2]) < 0) {
         ls3[n] = ls1[n1]; n1++;}
      else {
         ls3[n] = ls2[n2]; n2++;}
   free(ls1); free(ls2);
   ls[r1] = ls3;  N[r1] = N3;
   //printf("r1=%d r2=%d ", r1, r2);
   //printf("Merged\n");
}
