/* Matrix QR factorization */

#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

void printmatrix(int m, int n, int na, double(*a)[na])
{
	unsigned max = 10;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			printf("%*f ", max, a[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

char * mgsR(int m, int n, int nq, double(*q)[nq], int nr, double(*r)[nr])
{
	r[0][0] = 0.f;
	for (int i = 0; i < m; ++i) r[0][0] += q[i][0] * q[i][0];
	r[0][0] = sqrt(r[0][0]);

	if (r[0][0] + 1000000.f == 0.f + 1000000.f) return "linearly dependent";

	for (int i = m - 1; i >= 0; --i) q[i][0] /= r[0][0];

	if (n > 1)
	{
		for (int i = 1; i < n; ++i) r[i][0] = 0.f;

		for (int j = 1; j < n; ++j) {
			r[0][j] = 0.;
			for (int k = 0; k < m; ++k)
				r[0][j] += q[k][0] * q[k][j];
		}

		for (int i = 0; i < m; ++i)
			for (int j = 1; j < n; ++j)
				q[i][j] -= q[i][0] * r[0][j];

		return mgsR(m, n - 1, nq, (double(*)[nq])&q[0][1], nr, (double(*)[nr])&r[1][1]);
	}
	return NULL;
}

char * mgsNR(int m, int n, int nq, double(*q)[nq], int nr, double(*r)[nr], double(*qq)[nq], double(*rr)[nr])
{
	int c = 0; //counter
	while (n - c >= 1)
	{
		r[c][c] = 0.f;
		for (int i = 0; i < m; ++i) r[c][c] += q[i][c] * q[i][c];
		r[c][c] = sqrt(r[c][c]);

		if (r[c][c] + 1000000.f == 0.f + 1000000.f) return "linearly dependent";

		for (int i = m - 1; i >= 0; --i) q[i][c] /= r[c][c];

		for (int i = c + 1; i < n; ++i) r[i][c] = 0.f;

		for (int j = c + 1; j < n; ++j) {
			r[c][j] = 0.f;
			for (int k = 0; k < m; ++k)
				r[c][j] += q[k][c] * q[k][j];
		}

		for (int i = 0; i < m; ++i)
			for (int j = c + 1; j < n; ++j)
				q[i][j] -= q[i][c] * r[c][j];
		c++;
	}
	return NULL;
}
