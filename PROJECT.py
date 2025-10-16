def onsquaretime(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
            iteration += 1
        print("")
    print("when n is ",n,"iteration =",iteration)
onsquaretime(6)
onsquaretime(7)
print("with every n the time takened is = n^2")