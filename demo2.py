# # list = ["prashant","Ashish","komal", "ankush","77","sandip",60.52,"prashant"]
# # print(list)
# # print(type(list))
# # print(list[0])
# # print(list[2])
# # print(list[-1])
# # print(list[2:5])
# # list.append("harsh")
# # list.append("Trump")
# # print(list)
# # newlist = list.copy()
# # list.remove("Trump")
# # print(newlist)
# # multilist = [['prashant','jha'],['85.56'],['25252','yyy']]
# # print(multilist[0][0])
# # print(multilist[0][1])
# # print(multilist[1][0])
# # print(multilist[2][0])
# # print(multilist[2][1])

# # list1 = ["prashant","jha"]
# # print(list1*2)
# # list2 = [4325,5325]
# # print(list1+list2)

# # list3 = [50,25,50,'prashant']
# # list3.clear()
# # print(list3)

# # list = [44,22,77,0,98]
# # list.sort() 
# # print(list)
# # print(id(list))  

# for i in range(1, 11):
#     for j in range(2, 11):
#         print(i * j, end="\t")
#     print()
# date_input = input("Enter date (YYYY-MM-DD): ")
# date_obj = datetime.strptime(date_input, "%Y-%m-%d")
# day = date_obj.strftime("%A")
# print(f"Day: {day}")

# days = int(input("Enter name of days: "))
# if days == "SATURDAY" or days == "SUNDAY" or days == "saturday" or days == "sunday":
#     print("It's a weekend!")
# else:
#     print("It's a weekday.")

# # Accept 3 paper marks
# mark1 = float(input("Enter mark 1: "))
# mark2 = float(input("Enter mark 2: "))
# mark3 = float(input("Enter mark 3: "))

# # Calculate total and percentage
# total = mark1 + mark2 + mark3
# percentage = (total / 300) * 100

# # Check eligibility for placement
# print(f"Total: {total}")
# print(f"Percentage: {percentage:.2f}%")

# if percentage >= 85:
#     print("Eligible for placement!")
# else:
#     print("Not eligible for placement.")

v1 = float(input("Enter value 1: "))
v2 = float(input("Enter value 2: "))
v3 = float(input("Enter value 3: "))
v4 = float(input("Enter value 4: "))
v5 = float(input("Enter value 5: "))

max_val = v1
if v2 > max_val:
    max_val = v2
if v3 > max_val:
    max_val = v3
if v4 > max_val:
    max_val = v4
if v5 > max_val: 
    max_val = v5 
print("Maximum value is:", max_val)