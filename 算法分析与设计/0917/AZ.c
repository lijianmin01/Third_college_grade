#include<stdio.h>
#include<stdlib.h> 
void  josephus(int * p, const int n, const int m);
int main(void)
{
    int * arr;
    int n, m;
    // printf("请输入人的总数：");
    scanf("%d", &n);
    //printf("请输入报数值：");
    m=3;
    arr = (int *)calloc(n, sizeof(int));
    josephus(arr, n, m);
    free(arr);
    return 0;
}
void  josephus(int * p, const int n, const int m)
{

	int i=0,out=n,cnt=0,t;
	int nums[2];
	int cnt1=0;
	while(out!=1)
	{
		if(p[i]==0)
		{
			cnt++;
		}
		if(cnt==m)
		{
			p[i]=1;
			out--;
			cnt=0;
		}
		i++;
		if(i==n)
		{
			i=0;
		}
		
	}
	for(i=0;i<n;i++)
	{
		if(p[i]==0)
		{
			nums[cnt1++]=i+1;
		}
	}
	printf("%d",nums[0]);
}