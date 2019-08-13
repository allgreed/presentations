#include <stdlib.h>
#include <stdio.h>

int main()
{
    const int numbers[] = { 1, -5, -2147483648 };
    
    for (int i = 0; i < (sizeof numbers / sizeof (int)) ; ++i)
    {
        int num = numbers[i];

        printf("Raw value: %d\n", num);
        printf("Absolute value: %d\n", abs(num));
    }

}

