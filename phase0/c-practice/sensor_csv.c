
#include<stdio.h>

int main()
{
	int samples[20];

	for( int i = 0 ; i < 20 ; i++ )
	{
		int position = i % 10;
		int val = ( position <= 5 ) ? position : 10 - position;
		samples[i] = val;
	}
        
        printf("Sample,Value \n");

        for( int i = 0 ; i < 20 ; i++)
        {
                printf("%d,%d\n" , samples[i] , i);
        }
	
	return 0;

}
