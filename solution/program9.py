#write a script to enter any number and print the sum of digit
a=int(input("enter number:"))
sum =0
while(a!=0):
    sum=sum+a%10
    a=a//10
print("sum of it:",sum)    
