#include <stdio.h>

void subset(int n, int m, int nss, int (*ss)[m]);

int main(int argc, char *argv[]) {
	int buffer[3];
	fread(buffer, sizeof(int), 3, stdin);
	
	int n = buffer[0];
	int m = buffer[1];
	int nss = buffer[2];
	int ss[nss][m];
	subset(n, m, nss, ss);
	
	fwrite(ss, sizeof(int), nss*m, stdout);

	return 0;
}
