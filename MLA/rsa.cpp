#include<bits/stdc++.h>


using namespace std;


long long int gcd(long long int e,long long int phi)
{
	
	long long int temp;
	
	while(1)
	{
		temp = e%phi;
		
		if(temp==0)
		  return phi;
		e = phi;
		phi = temp;
	}
	
	return phi;
}


long long int fpow(long long int msg,long long int pow,long long int m )
{
	long long int res = 1;
	msg = msg%m;
	
	while(pow)
			      {																																																																																																																																																																																																																																																		
		if(pow & 1)
			res = (res*msg)%m;
		pow=pow/2;
		msg = (msg*msg)%m;
	}
	
	return res;
	
}


int main()
{
	
	//map<int,char> m1;


	
	long long int q,p,n,m,d,k,e,phi;
	long long msg,ery,dry;
	
	p = 101;
	q = 103;
	
	n = p*q;
	
	phi = (p-1)*(q-1);
	
	
	e = 2;
	
	while(e<phi)
	{
		if(gcd(e,phi)==1)
		   break;
		e++;
	}
	
	k=1;																																																																																																																																																																																																																																																																																																																																																																																																																																																											
	
	while(((1+k*phi)%e)!=0)
	        k++;
	        
	d = (1+(k*phi))/e;
	
	cout<<"\nEnter your msg:";
	cin>>msg ;
	
	ery = fpow(msg,e,n);
	
	cout<<"Encrypted msg:"<<ery;
	
    dry = fpow(ery,d,n);
    
    
    cout<<"Decrypted msg:"<<dry;
    
	
}










