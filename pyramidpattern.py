n = int(input())
for i in range(1, n + 1): #i=row
    # spaces
    for j in range(n - i): #j=column
        print(" ", end="")
    # stars
    for j in range(i):
        print("* ", end="")
    print()
#output:
#4
#   * 
#  * * 
# * * * 
#* * * * 
