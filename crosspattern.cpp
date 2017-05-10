
#include<iostream>
using namespace std;

void printPattern(string str)
{
    int len = str.length();
 
    for (int i=0,j=len-1; i<=len,j>=0; i++,j--)
    {
        if (i<j)
        {
            // Print i spaces
            for (int x=0; x<i; x++)
                cout << " ";
 
            // Print i'th character
            cout << str[i];
 
            // Print j-i-1 spaces
            for (int x=0; x<j-i-1; x++)
                cout << " ";
 
            // Print j'th character
            cout << str[j] << endl;
        }
 
        // To print center point
        if (i==j)
        {
            // Print i spaces
            for (int x=0; x<i; x++)
                cout << " ";
 
            // Print middle character
            cout << str[i] << endl;
        }
 
        // To print lower part
        else if (i>j)
        {
            // Print j spances
            for (int x = j-1; x>=0; x--)
                cout << " ";
 
            // Print j'th character
            cout << str[j];
 
            // Print i-j-1 spaces
            for (int x=0; x<i-j-1; x++)
                cout << " ";
 
            // Print i'h character
            cout << str[i] << endl;
        }
    }
}
 

int main()
{
    printPattern("12345");
    return 0;
}
