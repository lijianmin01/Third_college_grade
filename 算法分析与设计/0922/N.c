#include<stdio.h>
#include<math.h>
//判断质数
int f(int n){
	int flag=1;
    int i;
	for(i=2;i<=sqrt(n);i++){
		if(n%i==0){
			flag=0;
			return 0;
		}
	}
	if(flag==1)
    {
        return 1;
    }
		
}

int main(){
	int n,i,k;
	scanf("%d",&n);
	int a[100]={0};
	int j=0;

	for(i=2;i<=n/2;i++){
		if(n%i==0 && f(i))
			a[j++]=i;
	}
	a[j]='\0';
	for(k=0;k<j;k++){
		printf("%d ",a[k]);
	}

	return 0;
}