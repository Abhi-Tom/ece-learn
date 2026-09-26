#include <stdio.h>

int main(void)
{
	float celsius;
	float fahrenheit;

	printf("Enter temperature in C: ");

	if(scanf("%f" , &celsius) != 1)
		{

		printf("Inavlid input \n");
		return 1;

		}

	fahrenheit = (celsius * 9.0f/5.0f) + 32.0f;

	printf("%.2f C = %.2f F\n",celsius , fahrenheit);

	return 0;
}
