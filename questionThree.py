#lets take x as 0 which will help in swapping
# x=0
# a=10
# b=20

# print('Before swapping the value of a and b is:', a,b)
# x=a
# a=b
# b=x
# print('After Swapping')
# print(a,'value of a')
# print(b, 'value of b')


#INeuron Solution
numberOne = int(input('Enter the number:'))
numberTwo = int(input('Ener the number:'))

numberOne, numberTwo = numberTwo, numberOne
print(numberOne)
print(numberTwo)