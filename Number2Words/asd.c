#include <stdio.h>

void printNumber(int num) 
{
    char ones[10][20] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    char teens[10][20] = {"", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    char tens[10][20] = {"", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    int thousands, hundreds, tens_place, ones_place;

    if (num == 0) 
    {
        printf("zero\n");
        return;
    }

    thousands = num / 1000;
    num = num % 1000;
    hundreds = num / 100;
    num = num % 100;
    tens_place = num / 10;
    ones_place = num % 10;

    if (thousands > 0) 
    {
        printf("%s thousand ", ones[thousands]);
    }

    if (hundreds > 0) 
    {
        printf("%s hundred ", ones[hundreds]);
    }

    if (tens_place == 1 && ones_place > 0) 
    {
        printf("%s", teens[ones_place]);
    } 
    else 
    {
        if (tens_place > 0) 
        {
            printf("%s ", tens[tens_place]);
        }
        if (ones_place > 0) 
        {
            printf("%s\n", ones[ones_place]);
        }
    }
}

int main() 
{
    int num;
    
    printf("Enter a number = ");
    scanf("%d", &num);

    if (num < 0 || num > 9999) 
    {
        printf("Please enter a number between 0 and 9999.\n");
    }
    else
    {
        printNumber(num);
    }

    return 0;
}