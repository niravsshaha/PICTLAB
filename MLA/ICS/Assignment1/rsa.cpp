/*Name:-Nimisha Phadke
Roll No:-4064
Batch:- S10
Problem statement:-Write a program in C++ or Java to implement RSA algorithm for key generationand cipher verification

------------------------------------------------------------------------------------------------------------------------*/

﻿#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

class RSA
{
	public:
		long int p, q, n,t,flag, e[100], d[100], temp[100], j,i;
		char msg[100],en[100],m[100];
		int prime(long int);
		void ce();
		long int cd(long int);
		void encrypt();
		void decrypt();
};

int RSA :: prime(long int pr)
{
    int i;
    j = sqrt(pr);
    for(i=2;i<=j;i++)
    {
        if(pr % i == 0)
            return 0;
    }
    return 1;
}

void RSA :: ce()
{
    int k=0;
    
    for(i=2;i<t;i++)
    {
        if(t%i == 0)
            continue;

        flag = prime(i);

        if(flag==1 && i!=p && i!=q)
        {
            e[k]=i;
            flag=cd(e[k]);

            if(flag > 0)
            {
                d[k]=flag;
                k++;
            }

            if(k==99)
                break;
        }
    }
}

long int RSA :: cd(long int x)
{
    long int k=1;
    while(1)
    {
        k=k+t;
        if(k%x == 0)
            return (k/x);
    }
}

void RSA :: encrypt()
{
    long int pt,ct,key=e[0],k,len;
    i=0;
    len=strlen(msg);
   
    while(i!=len)
    {
        pt=m[i];
        pt=pt-96;
        k=1;

        for(j=0;j<key; j++)
        {
            k=k*pt;
            k=k%n;
        }

        temp[i]=k;
        ct=k+96;
        en[i]=ct;
        i++;
    }

    en[i] = -1;
    cout<<endl<<"The encrypted message is: ";
    
    for(i=0;en[i]!=-1;i++)
        cout<<en[i];

}

void RSA :: decrypt()
{
    long int pt,ct,key=d[0],k;
    i=0;
   
    while(en[i]!=-1)
    {
        ct=temp[i];
        k=1;

        for(j=0;j<key;j++)
        {
            k=k*ct;
            k=k%n;
        }

        pt=k+96;
        m[i]=pt;
        i++;
    }

    m[i]=-1;
    cout<<endl<<"The decrypted message is: ";

    for (i=0;m[i]!=-1;i++)
        cout<<m[i];
        
    cout<<endl;
}

int main()
{
   
    RSA a;

    cout<<endl<<"Please enter first prime number: ";
    cin>>a.p;
    
    a.flag=a.prime(a.p);

    if(a.flag==0)
    {
        cout<<endl<<"Wrong Input !!!"<<endl;
        exit(1);
    }

    cout<<endl<<"Please enter another prime number: ";
    cin>>a.q;
    a.flag = a.prime(a.q);

    if(a.flag==0 || a.p==a.q)
    {
        cout<<endl<<"Wrong Input !!!"<<endl;
        exit(1);
    }

    cout<<endl<<"Please enter message: ";
    fflush(stdin);
    cin>>a.msg;

    for(int i=0;a.msg[i]!='\0';i++)
        a.m[i]=a.msg[i];

    a.n=a.p*a.q;
    a.t=(a.p-1)*(a.q-1);
    a.ce();

    a.encrypt();
    a.decrypt();

    return 0;
}

/*
Output:


a3-402-13@a340213-OptiPlex-5060:~/ICS$ g++ rsa.cpp
a3-402-13@a340213-OptiPlex-5060:~/ICS$ ./a.out

Please enter first prime number: 13

Please enter another prime number: 11

Please enter message:Nimisha

The encrypted message is: ]�mis��a
The decrypted message is: Nimisha

*/

