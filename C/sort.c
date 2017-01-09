/*
The problem is inspired by a fast N-body method that reduces the
problem to a lattice.) Given a nonnegative integer argument n, create a text file listing all
integer triples (i, j, k), 0 ≤ i ≤ j ≤ k ≤ n, ordering them based on the distance squared
i^2 + j^2 + k^2 from the origin. For triples at the same distance, order them lexicographically. 
*/

#include <stdio.h>
#include <stdlib.h>
//#include <time.h>

int compare(const void *a, const void *b)
{
	const int * aa = (int*)a; 
	const int * bb = (int*)b;
	int d;
	d = aa[0] - bb[0];
	if (d != 0) return d;
	d = aa[1] - bb[1];
	if (d != 0) return d;
	d = aa[2] - bb[2];
	if (d != 0) return d;
	d = aa[3] - bb[3];
	return d;
}

int main(int argc, char *argv[])
{
	//clock_t start = clock(), diff;
	if (argc != 2 || atoi(argv[1]) < 0)
	{
		//printf("Usage: ./sort.exe N\nN: a nonnegative integer\n");
		return(-1);
	}

	int i, j, k, counter = 0;
	int n = atoi(argv[1]);
	int size = (n + 1)*(n + 2)*(n + 3) / 6;
	int * items = (int *)malloc(sizeof(int)*4*size);
	if (!items) return -1;

	for (i = 0; i <= n; ++i)
	{
		for (j = i; j <= n; ++j)
		{
			for (k = j; k <= n; ++k)
			{
				items[4 * counter] = i*i + j*j + k*k;
				items[4 * counter + 1] = i;
				items[4 * counter + 2] = j;
				items[4 * counter + 3] = k;
				++counter;
			}
		}
	}

	qsort(items, size, sizeof(int) *4, compare);

	for (i = 0; i < size; ++i)
		printf("%d %d %d %d\n", items[4*i], items[4*i+1], items[4*i+2], items[4*i+3]);

	free(items);
	
	//diff = clock() - start;
	//int msec = diff * 1000 / CLOCKS_PER_SEC;
	//printf("Time taken %d seconds %d milliseconds\n", msec / 1000, msec % 1000);

	return 0;
}

