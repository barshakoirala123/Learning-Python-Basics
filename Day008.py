#loops 

numbers = [1, 2, 3, 4, 5] #list
n = len(numbers)
print(n)
for digits in numbers:
    print(digits)

for digits in numbers:
    print(numbers)

# 1 2 3 4 5 
# 1 2 3 4 5 

names = ['puntu', 'dodo', 'subububu', 'bunu']

for nicknames in names:
    print(f"nickname detected! The nickname is {nicknames}.")







days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
for day in range(len(days)):
    print(f"{days[day] } is day {day + 1} of the week")

for index, day in enumerate(days, start=1):
    print(index, day)
    print(f"{day} is the day {index}  of week")

# mean nikalne






# function declaration
def mean(nums):
    total = sum(nums)
    n = len(nums)
    mean = total/n
    print(mean)

mean([1, 2, 3 ,4 ,5])









































# numbers = [1, 2, 3, 4, 5]

# for items in numbers:
#     print(items)

# names = ['bobo', 'dudu', 'meri-baccha', 'mayalu']

#----------------------------------------------
#code here:


#----------------------------------------------



