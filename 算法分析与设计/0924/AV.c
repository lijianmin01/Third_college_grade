#include<stdio.h>

int main(){
    char strs[100];
    char str2[100];
    int cnt=0;
    char c;
    gets(str2);
    while(str2[cnt]!='\0'){
    	c=str2[cnt];
    	if(c==32){
    		
		}else{
			if(c=='z'){
            strs[cnt++]='a';
	        }else if(c=='Z'){
	            strs[cnt++]='A';
	        }else{
	            strs[cnt++]=(c+1);
	        }	
		}
    }
    int i;
    for ( i = 0; i < cnt; i++)
    {
        printf("%c ",strs[i]);
    }
    printf("\n");
    
    return 0;
}