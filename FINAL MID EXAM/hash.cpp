#include <iostream>
using namespace std;

#define size 10
#define I 1000
int i = -1;
int array[size]={I};

float H1(int x)
{
    return x % 7;
}


float H2(int x)
{
    return x % 3;
}

main()
{

   mainfunction(5);
   mainfunction(0);
   mainfunction(65);
   mainfunction(28);
   mainfunction(9);
   for(int j =0;j<10;j++)
   {
    cout<<array[j]<<endl;
   }

}

float HASHFunction(int x)
{
    i++;
    float result= (H1(x)+ (i*x*H2(x)));
    return result;
}

void mainfunction(int x)
{
    while(true)
    {
        if(HASHFunction(x)!=I)
        {
        array[x]=x;
        break;
        }
        else
        {
            x++;
        }
    }


}