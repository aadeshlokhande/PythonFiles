// function

// returntype functionName(arguments)
// {
//     code;
//     return value;
// }



// #include<stdio.h>
// float areaOfCircle(int rad)
// {
//     float area;
//     area = 3.14 * rad * rad;
//     return area;
// }

// int main()
// {
//     float ans;
//     int num;
//     printf("Enter a number = ");
//     scanf("%d",&num);

//     ans = areaOfCircle(num);

//     printf("ans = %f",ans);
//     return 0;
// }


// =<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=


// recursion



// #include<stdio.h>
// // a = 5
// void abc(int a)
// {
//     if (a>0)
//     {
//         printf("this is ABC function...\n");
//         abc(a-1);
//     }
// }


// int main()
// {
//     abc(10);
//     return 0;
// }


// =<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=<:>=


// 5! - 5x4x3x2x1
// 4! = 4x3x2x1

// 5! = 5 x 4! 
// n! = n * (n-1)!


// 1! = 1 
// 0! = 1 


// #include<stdio.h>

// int fact(int a)
// {
//     if(a==0 || a==1)
//     {
//         return 1;
//     }
//     else 
//     {
//         return a * fact(a-1);
//     }
// }



// int main()
// {
//     int num;
//     int ans;

//     printf("Enter a number = ");
//     scanf("%d",&num);

//     ans = fact(num);
//     printf("ans= %d",ans);
//     return 0;
// }