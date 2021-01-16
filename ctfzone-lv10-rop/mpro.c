#include <unistd.h>
#include <sys/mman.h>

int main(void){
    char *p;
    p =(char*)0x8048000;
    mprotect(p, 0x1000, 7);
    if (0>read(0, p+500, 10))
        printf("?");
    return 0;
}