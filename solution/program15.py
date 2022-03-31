#WAS to enter any number and print pattern
i=int(input("Enter any number:"))
n=1
for a in range(1,i+1):
    for b in range(1,a+1):
        print(n,end=' ')
        n=n+1
    print()

