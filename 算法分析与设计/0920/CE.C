
#include<stdio.h>

int qiu(int n){
	if(n<4){
		return 1;
	}else{
		return qiu(n-1)+qiu(n-3);
	}
}
int main(void){
	int n;
	scanf("%d",&n);
	int nums = qiu(n);
	printf("%d\n",nums);
	return 0;
}

