#include <stdio.h>

int main()
{
    int n;
    printf("enter no");
    scanf("%d",&n);

    int reverseno=0;
    int a=n;
    int remainder;

    while(a!=0)
    {
        remainder= a%10;
        reverseno=reverseno*10+remainder;
        a/=10;
    }
    printf("%d \n",reverseno); 

    if (reverseno==n)
        {
            printf("Palindrome Number");
        }
    else
    {
        printf("not Palindrome Number");
    }

}