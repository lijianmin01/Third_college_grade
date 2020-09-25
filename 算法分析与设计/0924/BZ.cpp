//https://blog.csdn.net/qq_40511169/article/details/80656318
#include<iostream>
#include<stdio.h>
using namespace std;
int abc[10006];
int solve(int n)
{
    if(abc[n]){
    	return abc[n];
	}
    if(n==0){
    	return abc[n]=1;	
	} 
    //注意：不可省略
    if(n==1){
    	return abc[n]=0; 
	}
    //因为后面调用solve(n-1)时，n-1可能等于0；
    if(n==2){
    	return abc[n]=1;
	} 
    abc[n]=(solve(n-1)+solve(n-2))%7654321;
    return abc[n];
}
int main()
{
    int n;
    scanf("%d",&n);
    printf("%d\n",(solve(n)+solve(n-1))%7654321);
    return 0;                                  
}