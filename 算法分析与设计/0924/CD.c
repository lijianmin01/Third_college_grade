// 从第一个坑开始放，开始dfs，每个坑都有两种可能，放或者不放，
// dfs（i,j）i第i个坑，j前i个坑最后j个坑都填了物质，
// 若j达到m,则次方案不行，若没有m,继续


#include<stdio.h>

int m=3,ans=0;

int dfs(int i,int j,int n){
    if(j==m) return 0;//如果有连续的m坑都有物质，此方案不行 
    if(i==n) {
       ans++;//能到n,说明之前没有连续的m坑都有物质，此方案可以
       return 1;
    } 
    int ans=0;
    dfs(i+1,0,n);//第i+1个坑里没有物质，之后的坑里是否放物质与前面没有联系了 
    dfs(i+1,j+1,n);//前i+1个坑中最后连续j+1个坑里都有物质， 
}
int main(){
    int res;
    int n;
    while(scanf("%d",&n)!=EOF){
        dfs(0,0,n);//从第0个坑里开始放 
        printf("%d\n",ans);
        ans=0; 
    }
    
} 