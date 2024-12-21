def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

while True:
    n = int(input('Enter the number from 3 to 20: '))
    if 3 <= n <= 20:
        break
    else:
        print('Enter the number again.')

result = get_password(n)
print('Password:', result)