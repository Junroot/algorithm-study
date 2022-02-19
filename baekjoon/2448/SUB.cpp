#include "stdio.h"

int arr[6200][3100];

void draw_tri(int size, int xpos, int ypos) {
	if (size == 3) {
		arr[xpos][ypos] = 1;
		arr[xpos - 1][ypos + 1] = 1;
		arr[xpos + 1][ypos + 1] = 1;
		arr[xpos - 2][ypos + 2] = 1;
		arr[xpos - 1][ypos + 2] = 1;
		arr[xpos][ypos + 2] = 1;
		arr[xpos + 1][ypos + 2] = 1;
		arr[xpos + 2][ypos + 2] = 1;
	}
	else {
		draw_tri(size / 2, xpos, ypos);
		draw_tri(size / 2, xpos - (size/2), ypos + size / 2);
		draw_tri(size / 2, xpos + (size/2), ypos + size / 2);
	}
}


int main()
{
	int n;
	scanf("%d", &n);

	draw_tri(n, n, 1);
	int i, j;
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n * 2 - 1; j++) {
			if (arr[j][i] == 1) {
				printf("*");
			}
			else {
				printf(" ");
			}
		}
		printf("\n");
	}
    return 0;
}