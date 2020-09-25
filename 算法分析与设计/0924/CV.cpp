#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#define MAX 16
using namespace std;
#include<stdio.h>

char ori[16];
int total,length;

//判断是否有元音字母
inline bool isValid(char *a){
    int i;
    for ( i = 0; i < length; i++)
    {
        if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'){
            return true;
        }
    }
    return false; 
}

//depth 判断是第几位
void perm(int depth, int start) { 
    //"depth" <- 1, "start" <- 0. 
    static bool isOccupied[MAX]={false};//判断每个字符是否被使用
    static char put[MAX];
    //长度符合，并且有元音字母
    if (depth == length+1 && isValid(put) == true) {
        for (int i=0; i<length; i++) {
            printf("%c",put[i]);
        }
        printf("\n");
    }else{
        for (i=start; i<total; i++) {
         if(isOccupied[i]==false) {
            put[depth-1]=ori[i]; //Attention! "depth" <- 1. 
            isOccupied[i]=true;
            perm(depth+1, i);//递归生成
            isOccupied[i]=false;
         }
      }
    }
}

int main () {
   scanf("%d %d", &length, &total);
   scanf("%s",&ori);
   
   //对字符串进行排序
   for (int i=0; i<total-1; i++){
       for (int j=i+1; j<total; j++){
           if (ori[i]>ori[j]){
               swap (ori[i], ori[j]);  
           }  
       }
   }
      
   perm(1, 0);
   return 0;
}
