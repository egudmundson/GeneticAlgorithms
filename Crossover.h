#include <stdlib.h>
#include <time.h>
#include <stdio.h>
// This function will return the child of the two parents using single point crossover.
//

int ** CrossOver(int *parent1, int *parent2,int const size){
	int location =0;
	int  *retVal[2];

	srand(time(NULL));
	location = rand()%size;

	printf("%d \n",location);

	return retVal;
}
