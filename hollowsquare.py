n=int(input())
for row in range(n): #i=row
    for col in range(n): #j=column
        if(row==0 or col==0 or row==n-1 or col==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#output:
#4
#* * * * 
#*     * 
#*     * 
#* * * * 
