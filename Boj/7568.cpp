#include <iostream>

using namespace std;

int main()
{
    int N,count;
    int x[50], y[50], cnt[50];
    cin >> N;
    
    for(int i=0; i<N; i++)
    {
        cin >> x[i] >> y[i];
    }
    for(int i=0; i<N; i++)
    {
        count = 1;
        for(int j=0; j<N; j++)
        {
            if(x[j] > x[i] && y[j] > y[i])
            { 
                count++;
            }
        }
        cnt[i] = count;
    }
    for(int i=0; i<N; i++)
    {
        cout << cnt[i] << " ";
    }
}
