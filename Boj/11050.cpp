#include <iostream>

using namespace std;

int main()
{
    int N,K,result,sub,tmp;
    cin >> N >> K;
    if((N/2) < K)
    {
        K = N-K;
    }
    result = 1;
    sub = 1;
    for(int i=K; i > 0; i--)
    {
        result *= N;
        sub *= K;
        N--;
        K--;
    }
    cout << result/sub;
}