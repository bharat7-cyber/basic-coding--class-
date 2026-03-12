# #wap to accept three paper marks and check maximum marks using nested if else 

n1 = int(input('Enter the value of paper1:'))
n2 = int(input('Enter the value of paper2:'))
n3 = int(input('Enter the value of paper3:'))
if n1>n2:
        if n1>n3:
                 print("n1 is greater")
        else:
              print("n3 is greater")
else:
      if n2>n3:
                print("n2 is greater")
      else:
            print("n3 is greater")
            

# # #wap to accept three paper marks and check minimum  marks using nested if else           
n1 = int(input('Enter the value of paper1:'))
n2 = int(input('Enter the value of paper2:'))
n3 = int(input('Enter the value of paper3:'))
if n1<n2:
        if n1<n3:
                 print("n1 is smaller")
        else:
              print("n3 is smaller")
else:
      if n2<n3:
                print("n2 is smaller")
      else:
            print("n3 is smaller")
            
            
# #wap to accept percentage and if per 
# #per > 90 ==> 'A'
# #per > 80 ==> 'B'
# #per > 60 ==> 'C'
# #per < 60 ==> 'FAIL'
# #else if ladder 

per = int(input('Enter your percentage:'))
if per >= 90:
            print("A")
elif per >=80 and per < 90:
        print ("B")
elif per >=60 and per < 80:
          print("C")
else:
    print("FAIL")
    
    
# #dictionary 

mydict = {
    "name": "prashant",
    "professional": "developer",
    "enpid":1001
    }
print(mydict)
print(type(mydict))

mydict= {
    101:"prashant",
    102:"ashish",
    "103":"mohini",
    "104":"trivani",
    101:"ashish",
    104:"ashish",
}
print(mydict)

# # #with the help of key we have to print the values
a = mydict[102]
print(a)

mydict[102]="peter"
print(mydict)

for x in mydict:
    print(x)

for x in mydict.values():
    print(x)

for x,y in mydict.items():
    print(x,y)

mydict["mobile_no"]= 9874561230
print(mydict)

mydict= {
    101: "prashant",
    "professional": "developer",
    "enpid":1001
}
mydict.pop(101)
print(mydict)

name = "prashantjha"
print(name[0])
print(name[1])
print(name[-1])

print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])
print(name[1:8:2])
print(name[::-1])


s ="help4code is a best platform for practicing programming"
print(s.find("help4code"))
print(s.find("python"))
print(s.find("programming"))


s = "prashant","ashish","sandip"
m = '|'.join(s)
print(m)

s = "python is a high level programming language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())


print('Subject Marks:')
phy = 50
chem = 60
math = 70
print("physic ={} chemistry={} Math={}".format(phy,chem,math))
print("physic ={0} chemistry={1} Math={2}".format(phy,chem,math))
print("physic ={x} chemistry={y} Math={z}".format(phy,chem,math))\

total = phy+chem+math
print("Total Marks", f"{total}")
print("Roll No=", "7".zfill(4))


print('prashantjha777'.isalnum())
print('prashantjha'.isalpha())
print('777f'.isdigit())
print('sdsdsdsd'.islower())
print(''.islower())
print('PRASHANTj'.isupper())
print('My Name is Prashant'.istitle())
print(''.istitle())
print(''.isspace())
print('Hello'.startswith("He"))
print('Hello'.endswith("lo"))


a = 50
b = 30
c = 20
d = 10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)

x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x!=z)

name = "prashant"
data = ['a','e','i','o','u']
vowels = 0
con = 0
for i in name:
    if i in data:
        vowels += 1
    else:
        con += 1
        print("vowels=" , vowels)
        print("consonent=", con)