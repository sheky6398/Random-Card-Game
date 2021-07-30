import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="[]{}()*:;/_-"
all=lower+upper+numbers+symbols
length=int(input("Enter the Lenght: "))
password="".join(random.sample(all,length))
print('Hello, Welcome to Password generator! ')
print("The Password is- ",password)