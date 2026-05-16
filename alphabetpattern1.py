n=int(input())
ch=65
for i in range(1,n+1): #i=row
    for j in range(1,i+1): #j=column
        print(chr(ch),end=" ")
        ch=ch+1
    print()
#output:
# 4
#A 
#B C 
#D E F 
#G H I J 
