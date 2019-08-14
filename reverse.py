m=int(input())
rev=0
while(m>0):
    dig=m%10
    rev=rev*10+dig
    m=m//10
print(rev)
