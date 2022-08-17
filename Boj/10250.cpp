#include <iostream>

using namespace std;

int main()
{
    int T,H,W,N,pos;
    cin >> T;
    for(int i=0; i<T; i++)
    {
        H,W,N = 0;
        pos = 1;
        cin >> H >> W >> N;
        for(int j=1; j<=W; j++)
        {
            for(int k=1; k<=H; k++)
            {
                
                if(N == pos)
                {
                    if(j >= 0 && j <= 9)
                        cout<< k << 0 << j << "\n";
                    else
                        cout << k << j << "\n";
                }
                pos++;   
            } 
        }
    }
}