#include <stdio.h>

long long power(long long a,long long b,long long p){
    long long result=1;
    a%=p;
    while(b>0){
        if(b%2==1)
            result=(result*a)%p;
        a=(a*a)%p;
        b/=2;
    }
    return result;
}

long long modInverse(long long a,long long m){
    for(long long i=1;i<m;i++)
        if((a*i)%m==1)
            return i;
    return -1;
}

int main(){
    long long p,q,g,x,k,h,y,r,s,w,u1,u2,v;

    printf("DSA Digital Signature Algorithm\n");
    printf("-------------------------------\n");

    printf("Enter prime number p: ");
    if(scanf("%lld",&p)!=1) return 1;

    printf("Enter prime divisor q: ");
    if(scanf("%lld",&q)!=1) return 1;

    printf("Enter generator g: ");
    if(scanf("%lld",&g)!=1) return 1;

    printf("Enter private key x: ");
    if(scanf("%lld",&x)!=1) return 1;

    printf("Enter message hash h: ");
    if(scanf("%lld",&h)!=1) return 1;

    printf("Enter random number k: ");
    if(scanf("%lld",&k)!=1) return 1;

    if(p<=2||q<=1||(p-1)%q!=0||g<=1||g>=p||
       x<=0||x>=q||k<=0||k>=q||h<0){
        printf("Invalid input parameters\n");
        return 1;
    }

    if(power(g,q,p)!=1){
        printf("Invalid generator: g must have order q\n");
        return 1;
    }

    y=power(g,x,p);
    r=power(g,k,p)%q;

    if(r==0){
        printf("Invalid signature: r is zero\n");
        return 1;
    }

    long long kinv=modInverse(k,q);

    if(kinv==-1){
        printf("Inverse of k does not exist\n");
        return 1;
    }

    s=(kinv*((h%q+x*r%q)%q))%q;

    if(s==0){
        printf("Invalid signature: s is zero. Choose another k or h\n");
        return 1;
    }

    printf("\n--- Signature Generation ---\n");
    printf("Public key y = %lld\n",y);
    printf("Signature r = %lld\n",r);
    printf("Signature s = %lld\n",s);

    w=modInverse(s,q);

    if(w==-1){
        printf("Signature verification failed\n");
        return 1;
    }

    u1=((h%q)*w)%q;
    u2=(r*w)%q;

    v=((power(g,u1,p)*power(y,u2,p))%p)%q;

    printf("\n--- Signature Verification ---\n");
    printf("u1 = %lld\n",u1);
    printf("u2 = %lld\n",u2);
    printf("Verification value v = %lld\n",v);

    if(v==r)
        printf("Digital Signature is VALID\n");
    else
        printf("Digital Signature is INVALID\n");

    return 0;
}