
#include<stdio.h>
/*弃九法，,一个数, 对9取余, 就相当于 其所有为 数和对九 ,取余*/
int main()
{
	int n,i,r;
	scanf("%d",&n);
	while(n--)
	{
		char strs[1000105];
		gets(strs);
		r=0;
		for(i=0;strs[i]!='\0';i++)
		{
			r+=s[i]-'0';
		}
		printf("%d\n",r%9);
	}
}  



// #include<stdio.h>

// int main(){
//     int n;
//     scanf("%d",&n);
//     while(n--){
//         long long int cnt,s;
//         scanf("%d",&cnt);
//         s = cnt/9;
//         printf("%d\n",s);
//     }

//     return 0;
// }