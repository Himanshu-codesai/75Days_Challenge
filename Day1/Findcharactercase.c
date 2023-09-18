#include <stdio.h>
#include <ctype.h>

int Findcharactercase(char a)
{
    if(isupper(a))
    {
        return 1;
    }
    else if (islower(a))
    {
        return 0;
    }
    else
    {
        return -1;
    }
}

int main()
{
    char charinput;
    printf("Enter the character \t");
    scanf("%c",&charinput);
    // printf("Entered character is -> %c \n ",charinput);

    int result = Findcharactercase(charinput);
    printf("%d",result);    
}
    













// int main()
// {
// char inp;
// scanf("%c",&inp);
// if (isupper(inp)) {
//     printf("f");
// }

// }