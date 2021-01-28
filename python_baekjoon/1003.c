#include<stdio.h>
#include<memory.h>
int OneCount, ZeroCount;
int cach[41];
int P(int n)
{
	if(n <= 1) // 들어오는 값이 0또는 1인경우
	{
		return cach[n];
	}
	if(0 < cach[n]) // 캐시안에 값이 들어있는 경우 (한번 연산을 진행한 경우)
	{
		return cach[n];
	}
	else
		return cach[n] = P(n-1) + P(n-2); //값이 들어있지 않는경우, 값을 넣어준다
}
int main()
{
	int Test, num, i;
	
	scanf("%d", &Test);
	
	cach[0]=0;
	cach[1]=1;
	
	for(i=0; i<Test; i++)
	{
		scanf("%d", &num);
		if(num==0)
			printf("1 0\n");
		else if(num == 1)
			printf("0 1\n");
		else
		{
			P(num);
			printf("%d %d\n", cach[num-1], cach[num]);
		}
	}
}