#include<stdio.h>

int main()
{
 int samples[5] = {12,20,30,40,50};
 int *pointer = samples;
 int i = 0;

 while( i < 5 )
	{ printf("using samples[i] : %d\n",samples[i]);
	  printf("using (*pointer + i) : %d\n",*(pointer + i));
          printf("address using (void *)&samples[i] : %p \n",(void *)&samples[i]);
	  printf("addressusing (void *)(pointer + i) : %p\n",(void *)(pointer + i));
	  i++;
	}
 return 0;
}
