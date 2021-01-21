#include<stdio.h>
int main(){
    int x,d;
    scanf("%d",&x);
    if(x%5==0){
        d=x/5;
    }else{
        d=x/5+1;
    }
    printf("%d",d);
    return 0;
}