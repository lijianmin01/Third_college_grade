#include<stdio.h>

public static ListNode fun(ListNode h1,ListNode h2){
    ListNode A=h1;
    ListNode B=h2;
    while(A!=B){
        A = A!=NULL ? A.next:h2;
        B = B!=NULL ? B.next:h1;
    }
    return A;
}

int main(){

    return 0;
}