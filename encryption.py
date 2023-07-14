#https://www.hackerrank.com/challenges/encryption/problem
import math
s="haveaniceday"
s1=""
c=0
n=0
m=int(math.sqrt(len(s)))
if m==math.sqrt(len(s)):
    n=m
else:
    n=int(math.sqrt(len(s)))+1
if m*n>=len(s):
    i=0
else:
    m+=1
    i=0
def f(s1,i,c):
    while True:
        s1=s1+s[i]
        i+=n
        if i>=len(s):
            c+=1
            i=c
            if i<n:
                s1+=" "
                f(s1,i,c)
            else:
                return s1
y=f(s1,i,c)
print(y)