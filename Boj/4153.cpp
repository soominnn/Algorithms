#include <iostream>

using namespace std;

int main()
{
    int arr[3];
    int tmp=0;
    while(1)
    {
        for(int i=0; i<3;i++)
        {
            cin >> arr[i];
        }
        
        if(arr[0]==0 && arr[1]==0 && arr[2]==0)
            break;
        
        for(int i=0; i<3; i++)
        {
            if(arr[i] >= arr[i+1])
            {
                tmp = arr[i+1];
                arr[i+1] = arr[i];
                arr[i] = tmp;
            }
        }
        if (arr[0]*arr[0] + arr[1]*arr[1] == arr[2] * arr[2])
            cout << "right\n";
        else
            cout << "wrong\n";
    }
}