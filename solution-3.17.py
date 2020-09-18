print("(a)")
for i in range(0,10):
    for j in range(1,1-i):
        print(" ", end = "")
    for k in range (0, i+1):
        print("*", end = "")
    print("")
print()
    
print("(b)")
for a in range(1,11):
    for b in range(0,1-a):
        print(" ", end = "")
    for c in range (0, 11-a):
        print("*", end = "")
    print("")
print()
print("(c)")
for a in range(0,10):
    for b in range(0,1+a):
        print(" ", end = "")
    for c in range (0, 10-a):
        print("*", end = "")
    print("")
print()
print("(d)")

for i in range(0,10):
    for j in range(0,10-i):
        print(" ", end = "")
    for k in range (0, i+1):
        print("*", end = "")
    print("")
print()