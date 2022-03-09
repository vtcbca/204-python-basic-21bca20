#write a script to enter any number and print it sum of digit
a=int(input("Enter number:"))
sum=0
temp=a
while(a>0):
    x=a%10
    sum=sum*10+x
    a=a//10
if(temp==sum):
    print("{}is a palidrome number".format(temp))

else:
    print("{} is not a palidrome number".format(temp))
    


 
