n=int(input())
for i in range(1,n+1): #i=row
    for j in range(n-i): #j=column
        print(" ",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()
#output:
#4
#      * * * * 
#    * * * * 
#  * * * * 
#* * * * 
