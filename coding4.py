for i,j in zip(range(1,6), range(5,0,-1)):
    if i ==3 and j==3:
        continue
    print(i," ",j)

i = 1
while i <=5:
    print(i)
    i = i+1
username = ''
password = ''
while username != "admin" and password != "hello":
    username = input("Enter username :")
    password = input("Enter password :")

    
n = int(input("Enter number:")) 
sum = 0
i = 1
while i <= n:
    sum = sum+i
    i=i+1
print("The sum of first", n , "numbers is:", sum )

name = "prashant"
newname = " "
for i in name:
    if i not in newname:
        newname += i
       
        print(newname)

name = "prashant"
print(name[::-1]) 

mycart=[10,20,200,300,800,60,700]
for i in mycart:
    if i > 400:
        print("This is my purchased cart item ")
        continue
    print(i)

name = input("Enter a string: ")
reverse = name[::-1]
if name == reverse:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")
    
    
for i in range(1, 4):    #Loop => Rows
    for j in range(1,4):  #Loop => Columns
          print(i , end=" ")
    print()

n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
        print()