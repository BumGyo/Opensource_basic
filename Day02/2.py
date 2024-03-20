
for a in range(2, 10):
    print("#  %d단  #" %a,  end = "   ")
print("")

for i in range(1, 10) :
    for j in range (2, 10) :
        print("%d X %d = %2d" %(j, i, i*j), end = "  ")
    print("")