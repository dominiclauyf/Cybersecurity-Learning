import math,random
def random_prime(k=20):
    # miller rabbin
    def check_prime(n):
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


    p=random.getrandbits(k)
    p |= (1 << k - 1) | 1

    while not check_prime(p):
        p=random.getrandbits(k)
        p |= (1 << k - 1) | 1
    return p

# reference https://gist.github.com/JonCooperWorks/5314103
class RSA:
    def __init__(self,p,q):
        self.n=p*q
        self.p=p
        self.q=q
        self.phi=(p-1)*(q-1)
        self.e = random.randrange(2, self.phi)
        g = self.gcd(self.e, self.phi)
        while g != 1:
            self.e = random.randrange(2, self.phi)
            g = self.gcd(self.e, self.phi)
        self.multiplicative_inverse()

    def encrypt(self,plain_text):
        return pow(plain_text,self.e,self.n)
    
    
    def decrypt(self,cipher_text):
        return pow(cipher_text,self.d,self.n)
    
    
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a

    def multiplicative_inverse(self):
        x1=self.phi
        x2=self.e
        x3=None
        y1=self.phi
        y2=1
        y3=None
        while x1>0:
            multiply=x1//x2
            x3=x1-multiply*x2
            y3=y1-multiply*y2
            if y3<0:
                y3%=self.phi
            if x3==1:
                self.d=y3
                break
            x1=x2
            x2=x3
            y1=y2
            y2=y3

if __name__ == "__main__":
    _RSA=RSA(random_prime(128),random_prime(128))
    cipher=_RSA.encrypt(42)
    print(cipher)
    print(_RSA.decrypt(cipher))


