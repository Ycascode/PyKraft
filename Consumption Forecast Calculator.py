import time
print("Hello")
time.sleep(2)
print("Welcome to the Consumption Forecast Calculator")
time.sleep(2)
n1=int(input("Type the first month: "))
n2=int(input("Type the second month: "))
n3=int(input("Type the third month: "))
n4=int(input("Type the fourth month: "))
n5=int(input("Type the fifth month: "))
n6=int(input("Type the sixth month: "))
s=n1+n2+n3+n4+n5+n6
d=s/6
phrase='The expect demand is: '
mensage='%s %i' %(phrase,d)
print(mensage)
