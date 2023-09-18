#include <stdio.h>
#include <string.h> 
int main()
{
    char entered[10];
    scanf("%s",&entered);
    int length = strlen(entered);
    printf("%d \n",length);
    if (strcmp(entered, "Long") == 0)
    {
        printf("8 Bytes\n");
    }
    else 
    {
        printf("error");
    }  
}
 // if (entered=='Long')
    // {
    //     printf("8 Bytes");
    // }