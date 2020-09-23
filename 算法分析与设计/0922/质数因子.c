//链接：https://www.nowcoder.com/questionTerminal/196534628ca6490ebce2e336b47b3607
//来源：牛客网

#include <stdio.h>

int main(void)
{
    long int a;
    int i;
    //printf("Input a positive number:a\n");
    scanf("%d",&a);
    
    for (i=2;i<=a;i++)
    {    
     	while (a != i){
	        if (a%i == 0)
            {
                printf("%d ",i);
                a = a/i;
            }else{
            	break;
			}
        }
    }
    printf("%d ",a);
    printf("\n");
    return 0;    
}