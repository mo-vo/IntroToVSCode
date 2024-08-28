# problem #1: infinite loop
# What is mising in the while loop? The value of x is not incrementing
# use a breakpoint in line 6 to debug
x = 1
while x < 10:
    print(x)
    x += 1 #incrementing x


# problem #2
# use a breakpoint in line 14 to debug
mylist = list(range(5))

for x in range(1,5):
    print(f"Run No.:{mylist[x]}")

