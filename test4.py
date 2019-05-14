# this is a test python program

def numcheck(number1):
    if number1%2 == 0:
        value=(number1)/2
        print('number is even and value is',value)
    else:
        value= (number1)*3+1
        print('number is odd and value is',value)

while True:
    print('enter the number')
    number = int(input())
    numcheck(number)



