#include<stdio.h>
#include<memory.h>
int OneCount, ZeroCount;
int cach[41];
int P(int n)
{
	if(n <= 1) // ������ ���� 0�Ǵ� 1�ΰ��
	{
		return cach[n];
	}
	if(0 < cach[n]) // ĳ�þȿ� ���� ����ִ� ��� (�ѹ� ������ ������ ���)
	{
		return cach[n];
	}
	else
		return cach[n] = P(n-1) + P(n-2); //���� ������� �ʴ°��, ���� �־��ش�
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