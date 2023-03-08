
To perform the -A power, we perform an inverse mod q function:

elementA = inverse_of(pow(PE,A),q)
elementB = inverse_of(pow(PE,B),q)
In the confirm phase we then use the long-term key to generate a unique session key. An attacker cannot determine the password used or the long-term master key (PMK). The cracking of one session key will not reveal the rest of the keys which have been used. Which is not the case for WPA-2.

Here is a simple implementation of the Dragon method:

import hashlib
import random
import sys
import libnum




q=131
text="hello"

a=random.randint(1,1000)
b=random.randint(1,1000)
A=random.randint(1,1000)
B=random.randint(1,1000)


sA= a + A
sB = b + B



PE = int(hashlib.md5(text.encode()).hexdigest()[:8], 16)

elementA = libnum.invmod(pow(PE,A),q)
elementB = libnum.invmod(pow(PE,B),q)

PEsA = pow(PE,sA,q)
PEsB = pow(PE,sB,q)

print("Password:",text)
print("Alice generates two random values")
print("a:\t",a)
print("A:\t",A)
print("\nBob generates two random values")
print("b:\t",b)
print("B:\t",B)

print("\nAlice calculates elementA")
print("Element A:",elementA)
print("\nBob calculates elementA")
print("Element B:",elementB)


ss1 = pow(PEsA * elementA,b,q)
ss2 = pow(PEsB * elementB,a,q)

print("\nThey exchange values and calculate a secret share")
print("\nAlice share:\t",ss1)
print("Bob share:\t",ss2)
