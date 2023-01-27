# assignment-4 
import random
n=1
while(n<=10):
    a = (random.randrange(0, 10))
    b = (random.randrange(0, 10))
    print("a is", a)
    print("b is", b)

    print('QUESTION n:a*b is')
    answer = int(input())

    if (answer == a * b):
        print('correct answer')

    else:
        print('incorrect answer correct answer is ', a*b)

n = n + 1
