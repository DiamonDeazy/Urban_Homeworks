first = int(input('Type first number: '))
second = int(input('Type second number: '))
third =  int(input('Type third number: '))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)