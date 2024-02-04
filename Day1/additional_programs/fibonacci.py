#print fibonacci series of a number 
nterm=10
n=0
n2=1
count=0

if nterm<=0:
    print("enter positive integer: ")
elif nterm==1:
    print("nterm:",nterm)
    print(n)
else:
    print(nterm)
    while count<nterm:
        print(n, end=',')
        nth = n+n2
        n=n2
        n=nth
        count+=1
