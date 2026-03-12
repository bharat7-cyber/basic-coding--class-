#wap a program for simple intrest
priciple = 1000
rate = 5
time = 2
simple_interest = (priciple * rate * time) / 100
print("Simple Interest:", simple_interest)



#write a program except a centigrade temperature and convert it to fahrenheit
centigrade = float(input("Enter temperature in Centigrade: "))
fahrenheit = (centigrade * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#swap two numbers without using a third variable
a = 5
b = 10
print("Before swapping: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

#take value from user and swwp them
x = input("Enter first value: ")
y = input("Enter second value: ")
print("Before swapping: x =", x, "y =", y)
x, y = y, x
print("After swapping: x =", x, "y =", y)

#wap to enter height of the user in feet and convert it into inches and centimeters
height_feet = float(input("Enter height in feet: "))
height_inches = height_feet * 12
height_centimeters = height_inches * 2.54
print("Height in inches:", height_inches)
print("Height in centimeters:", height_centimeters)

#take num 123 and print 321
num = 123
reversed_num = int(str(num)[::-1])
print("Reversed number:", reversed_num)

#w
num =123
a = num %10
print(a)
num = num // 10
b = num % 10
print(b)
num = num // 10
c = num % 10
print(c)
print("Reversed number:", a * 100 + b * 10 + c)

#do same for 1234567 using while loop 
num = 1234567
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print("Reversed number:", reversed_num)
