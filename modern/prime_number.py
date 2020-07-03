import math
import random
def basic(n):
    def is_prime(n):
        steps=1
        if n==1:
            return False
        steps+=1
        if n==2:
            return True
        steps+=1
        if n>2 and n%2==0:
            return False
        else:
            for j in range(3,math.floor(math.sqrt(n))+1,2):
                steps+=1
                if(n%j==0):
                    return False
            return True
    return is_prime(n)
    
        
    
    
def fermat(n):
    def gcd(x,y):
        while(y!=0):
            z=x%y
            x=y
            y=z
        return x
    def is_prime(n):
        steps=1
        if n==1 or n%2==0:
            return False
        steps+=1
        if n==2 or n==3:
            return True
        
        for i in range(128):
            a=random.randint(2,n-2)
            steps+=1
            if math.gcd(a,n)!=1:
                return False
            steps+=1
            if pow(a,n-1,n)!=1:
                return False
        
        return True
    return is_prime(n)
    
    
def miller_rabbin(n):
    def is_prime(n, k=128):
    
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        # find r and s
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        # do k tests
        for _ in range(k):
            a = random.randrange(2, n - 2)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                for j  in range(s-1):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    if x == n-1:
                        break
                else:
                    return False
        return True
    return is_prime(n)

if __name__ == "__main__":
    print(basic(36))
    print(fermat(36))
    print(miller_rabbin(36))

    
