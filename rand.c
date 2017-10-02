#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<sys/time.h>
int main(){
	struct timeval tpstart;
	int n,i;
	for(i=0;i<100;i++){
	gettimeofday(&tpstart,NULL);
	srand(tpstart.tv_usec);
	n=(0+(int)(5.0*rand()/(RAND_MAX+1.0)));
	printf("%d\n",n);
	}
}
