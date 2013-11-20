#include <stdio.h>
#include "Crossover.h"

int main(){

	int parent1[4];
	int parent2[4];
	parent1[0] = 1;
	parent2[0] = 2;
	parent1[1] = 1;
	parent2[1] = 2;
	parent1[2] = 1;
	parent2[3] = 2;
	int **ret;
	ret = CrossOver(parent1,parent2,4);

	return 0;
}
