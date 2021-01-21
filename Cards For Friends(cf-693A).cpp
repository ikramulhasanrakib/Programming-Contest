#include<stdio.h>
int main(){
    int T,w,h,n,count;
    scanf("%d",&T);
    while (T--){
        scanf("%d %d %d",&w,&h,&n);
        count=1;
        while(w%2==0){
            count = count*2;
            w=w/2;
            
        }
        while(h%2==0){
            count = count*2;
            h=h/2;
            
        }
        if(count>=n){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}