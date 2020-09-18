#include<stdio.h>
#include<string.h>

char * int_to_string(int num)
{
    if(num==0){
        return '0';
    }

	int i=0,j=0;
	char temp[10],str[10];

	while(num)
	{
        //1000
    	temp[i++]=num%10+'0';  //将数字加字符0就变成相应字符
    	num/=10;               //此时的字符串为逆序
	}
    temp[i]='\0';
 	i=i-1;
 	while(i>=0)
    str[j++]=temp[i--];   //将逆序的字符串转为正序
	str[j]='\0';               //字符串结束标志

	return str;
} 

int main(){
    int n,i,j;
    scanf("%d",&n);
    int nums[10];
    for ( i = 0; i < 10; i++)
    {
        nums[i]=0;
    }
    if(n==0){
        printf("1\n");
        return 0;
    }

    for ( i = 0; i <= n; i++)
    {
        char *num;
        num = int_to_string(i);
        for ( j = 0; num[j]!='\0'; j++)
        {
            if(num[j]=='0'){
                nums[0]++;
            }else if(num[j]=='1'){
                nums[1]++;
            }else if(num[j]=='2'){
                nums[2]++;
            }else if(num[j]=='3'){
                nums[3]++;
            }else if(num[j]=='4'){
                nums[4]++;
            }else if(num[j]=='5'){
                nums[5]++;
            }else if(num[j]=='6'){
                nums[6]++;
            }else if(num[j]=='7'){
                nums[7]++;
            }else if(num[j]=='8'){
                nums[8]++;
            }else if(num[j]=='9'){
                nums[9]++;
            } 
        }  
    }
    
    for ( i = 0; i < 10; i++)
    {
        printf("%d\n",nums[i]);
    }
    
    return 0;
}