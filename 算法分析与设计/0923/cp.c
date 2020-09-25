#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
#include<cmath>
#include<string>
#include<map>
#include<queue>
using namespace std;
typedef long long ll;
ll a[30];
 
void dfs(ll num,ll len,ll n,ll m){
	if(len==m){//选全m个数 
			for(ll i=1;i<=m-1;i++){
				cout<<a[i]<<" ";
			}
			cout<<a[m]<<endl;
			return ; 
	}
	if(num==n){//没有选全m个数，但是数已经超过n，return； 
		return ;
	}
	for(ll i=num+1;i<=n;i++){//寻找num后面的数字 
		a[++len]=i;//选进 
		dfs(i,len,n,m);
		len--;//踢出 
	}
	return ;
}
 
int main(){
	ll n,m;
	cin>>n>>m;
	dfs(0,0,n,m);
return 0;
}