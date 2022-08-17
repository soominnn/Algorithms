#include <iostream>

using namespace std;

int M_origin(int M, int sum)
{
    sum = M;
    for(int i=0; i<7; i++)
    {
        sum += M%10;
        M=(M-(M%10))/10;
    }
    return sum;
}

int main()
{
    int M,N,sum,key;
    M=0;
    cin >> N; 
    while(1)
    {
        sum = 0;
        key = M_origin(M,sum);
        if(key == N)
        {
            cout<< M;
            break;
        }
        else if(M > N)
        {
            cout << 0;
            break;
        }
        M++;
    }
}