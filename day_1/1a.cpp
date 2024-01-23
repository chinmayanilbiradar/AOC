#include <bits/stdc++.h>
using namespace std;
int helper(string s)
{
    // cout << "here";
    int n = s.size();
    int val = 0;
    int i = 0;
    while (i < n)
    {
        // cout << "yes" << endl;
        if (isdigit(s[i]) == true)
        {
            val += 10 * (s[i] - '0');
            break;
        }
        else
            i++;
    }
    int j = n - 1;
    // cout << val << endl;
    while (j >= i)
    {
        // cout << "yes2" << endl;
        if (isdigit(s[j]) == true)
        {
            val += s[j] - '0';
            break;
        }
        else
            j--;
    }
    // cout << val << endl;
    return val;
}
int main()
{
    ifstream myfile("C:/Users/birad/Desktop/AOC/input.txt");
    int ans = 0;
    if (myfile.is_open())
    {
        string s;
        while (getline(myfile, s))
        {
            ans += helper(s);
        }
    }
    myfile.close();
    cout << ans;
    return 0;
}