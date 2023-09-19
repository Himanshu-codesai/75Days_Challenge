#include <stdio.h>

int main()
{
    int a,b;
    printf("Enter two numbers\n");
    scanf("%d",&a);
    scanf("%d",&b);
    if (a>b)
    {
        printf("Greater");
    }
    else if (a<b)
    {
        printf("Smaller");
    }
    else 
    {
        printf("Equal");
    }
    return 0;
}