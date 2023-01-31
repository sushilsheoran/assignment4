import random
i = 0
while i<10:
    a = random.randint(1,10)
    b = random.randint(1,10)
    print("The multiplication of",a, "x",b)
    z=int(input("Your Answer:"))

    if z==a*b:
        print("Correct Answer\n")
    else:
        print("Wrong Answer\n")
    i+=1
print("The game has ended")