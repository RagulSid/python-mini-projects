import random
otp = random.randrange (100000, 1000000)
print(otp)

user = int(input('Enter the OTP: '))
if otp == user:
    print('Access granted!!!')
else:
    print("Access Denied!!! ")