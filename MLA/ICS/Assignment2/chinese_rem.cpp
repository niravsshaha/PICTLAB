


#include<bits/stdc++.h>
using namespace std;

int power(int x,int y,int m)
{
	if(y==0)
		return 1;
	
	int temp=1;
	
	for(int i=1;i<=y;i++)
	{
		temp*=x%m;	
	
	}
	
	return temp;
}


int main()
{
	int m[100],r[100],t[100],n,ans;
	cout<<"Enter no of equations: ";
	cin>>n;
	
	for(int i=0;i<n;i++)
	{
		cout<<"Enter a"<<i+1<<" and m"<<i+1<<": ";
		cin>>r[i]>>m[i];
	}
	
	cout<<"The equations entered by you are:\n";
	
	for(int i=0;i<n;i++)
	{
		cout<<r[i]<< " (mod "<<m[i]<<")\n";
	}
	
	int M=1;
	
	for(int i=0;i<n;i++)
	{	
		M*=m[i];
	}		
	
	for(int i=0;i<n;i++)
	{
		t[i]=power(M/m[i],m[i]-2,m[i])%(m[i]);
	}
	
	ans=0;
	
	for(int i=0;i<n;i++)
	{
		ans+=(M/m[i])*r[i]*t[i];
	}
	
	ans=ans%M;
	
	cout<<"Answer of Chinese remainder theorem is "<<ans<<endl;
	
	return 0;
}




/*
Output:
a3-402-09@a3-402-09:~/ICS$ g++ chinese_rem.cpp 
a3-402-09@a3-402-09:~/ICS$ ./a.out
Enter no of equations: 4
Enter a1 and m1: 1 2
Enter a2 and m2: 1 3
Enter a3 and m3: 3 5
Enter a4 and m4: 1 7
The equations entered by you are:
1 (mod 2)
1 (mod 3)
3 (mod 5)
1 (mod 7)
Answer of Chinese remainder theorem is 43
*/
