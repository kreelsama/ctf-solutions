#include<unistd.h>
#include<stdio.h>

int main(void){
    close(1);
    dup2(1, 2);
    printf("123");
}