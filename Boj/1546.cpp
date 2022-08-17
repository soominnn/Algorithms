#include <iostream>

using namespace std;

int main()
{
    int n;
    int max=0;
    float result;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++)
    {
        cin >> arr[i];
        if(arr[i] > max)
            max = arr[i];
    }

    for(int i=0; i<n; i++)
    {
        result += (float)arr[i]/max*100;
    }
    cout << result/n;
}