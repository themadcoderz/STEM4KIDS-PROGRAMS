#question1
def factorial():
    fact = 1
    number = int(input("Enter a number:  "))
    for i in range(1, number + 1):
        fact = fact * i
        print(fact)

factorial()



#question 3
def star():
    star = "*"
    num = 0
    base = int(input("Enter a base size:  "))
    while num < base:
        print(star)
        star = star + "*"
        num = num + 1
#star()

def addall():
    result = 0
    number = input("Enter a number:  ")
    for i in range(0, len(number)):
        result = result + int(number[i])
    print(result)
#addall()


def firstlast():
    number = input("Enter a number:  ")
    debug = int(len(number))
    print(debug)
    print(int(number[0]) - int(number[debug - 1]))

#firstlast()


def poweroftwo():
    number = int(input("Enter a number:  "))
    exponent = 1
    power = 0
    while power < number:
        power = 2 ** exponent
        exponent = exponent + 1
    exponent = exponent - 2
    print (2 ** exponent)

#poweroftwo()
