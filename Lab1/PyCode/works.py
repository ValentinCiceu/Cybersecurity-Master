# ## Cybersec Lab 1

# %%
print(53431 % 453)

# %%
print(0x43 | 0x21 )

# %%
print(0x43 & 0x21 )

# %%
print(0x43 ^ 0x21  )

# %%
val1=93 
print("Dec:\t",val1 )

# %%
print("Bin:\t",bin(val1))

# %%
print("Hex:\t",hex(val1))

# %%
print("Oct:\t",oct(val1))

# %%
print("Char:\t",chr(val1))

# %%
import base64 

# %%
s = "crypto"
encoded_bytes = base64.b64encode(s.encode("utf-8"))
encoded_string = encoded_bytes.decode("utf-8")

encoded_string

# %%
s = "crypto1"
encoded_bytes = base64.b64encode(s.encode("utf-8"))
encoded_string = encoded_bytes.decode("utf-8")

encoded_string

# %%
print("Bin:\t",bin(41))

# %%
import math

# Given numbers
num1 = 4539 
num2 = 6

# Compute the GCD
gcd_result = math.gcd(num1, num2)

gcd_result

# %%
pow(8,13)%271

# %%
pow(12,23)%973

# %%
pow(8,5)%269

# %%
def cipher(message , e , p):
    print(int(message) ** int(e) % int(p))

# %%
cipher(5,5,53)

# %%
cipher(4,11,79)

# %%
cipher(101,7,293)

# %%
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_up_to(target):
    primes = []
    for num in range(2, target + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# %%
primes_up_to(100)

# %%
primes_up_to(1000)

# %%
primes_up_to(5000)

# %%
primes_up_to(10000)[-1]

# %%
def randSeqCheck(a,seed,c,mod):
    print((a*seed+c)%mod)

# %%
randSeqCheck(21,79,31,100)

# %%
randSeqCheck(2175143,934700,10653,1000000)