#include<stdio.h>
#include<stdlib.h>
int main()
{
	int c, i, n, k, sum, up;
	int* arr;
	double avg;
	scanf("%d", &c);
	for(i=0; i<c; i++)
	{
		scanf("%d", &n);
		arr=(int*)malloc(sizeof(int)*n);
		sum=up=0;
		for(k=0; k<n; k++)
		{
			scanf("%d", &arr[k]);
			sum+=arr[k];
		}
		avg=(double)sum/(double)n;//ЦђБе
		for(k=0; k<n; k++)
		{
			if(arr[k]>avg)
				up++;
		}
		avg=(double)up*100/n;
		printf("%.3lf%%\n", avg);
		free(arr);
	}
}