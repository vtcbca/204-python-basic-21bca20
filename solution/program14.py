#WAS to enter any number and print pattern
n=int(input("Enter any number:"))
for a in range(1,n+1):
    print(" "*(n-a)+"* "*a)
