a=int(input("Enter a value="))
sum=0
temp=a
while(a>0):
    x=a%10
    y=x*x*x
    sum=sum+y
    a=a//10

if(temp==sum):
    print("{}is armstrong number".format(temp))
else:
    print("{} is not armstrong number".format(temp))
