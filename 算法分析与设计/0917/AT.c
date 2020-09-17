#include<stdio.h>

int main() {
    char strs[1000];
    int i;
    gets(strs);
    for(i=0;strs[i]!='\0';i++){
        if (strs[i]==32){

        }else if(strs[i]=='z'){
            printf("a ");
        }else if(strs[i]=='Z')
        {
            printf("A ");
        }else{
            printf("%c ",(strs[i]+1));
        }
    }
    return 0;
}








// #include<stdio.h>
// #include<math.h>
// #define S(a,b,c) (a+b+c)*1.0/2
// #define area(a,b,c,S) sqrt(S*(S-a)*(S-b)*(S-c))

// int main(){
//     int a,b,c;
//     scanf("%d %d %d",&a,&b,&c);
//     double s,area1;
//     s = S(a,b,c);
//     area1 =area(a,b,c,s);
//     printf("%.3lf\n",area1); 
//     return 0;
// }