#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n, length;
    string database , l ,r;
    cin >> n;
    for (int _=0; _<n; _++)
    {
        cin >> database;
        cin >> length;
        cin >> l;
        cin >> r;
        cout << database << length << l << r;
    }
    
}