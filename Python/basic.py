# start of practice

x = str(3)
y = float(5)
z = 'hello'
# not corrent
# first-name= "Ali" 
a,b,c = 'ali', 'karim', 'mohammad'
i = j = h = 10

print(x)
print(y)
print(z)
print(type(x))

fruits = ['ali', 'ahmad', 'mahmood']
x, y, z = fruits

print(x+y+z)
print(x, y)

message = 'grete'
def myFunc():
    # it cause to reasign global var value, and also can create a global var if there is no
    global x
    x = 'fantastic'

myFunc();
print(message)



numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings = []
strings.append('hello')
strings.append('world')
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None
second_name = names[1]
print(second_name)

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

myText = "Hello World"
print(myText * 2)
print([1,2,3]*3)

oddList = [1,3,5,7,9]
evenList = [2,4,6,8,10]
print(oddList + evenList)


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

string = 'hellow World and wellcome'
print(string.index('W'))
print(string.count('l'))
print(string[2:10])
print(string[2:10:2])#start/end/ step
print(string[::-1])
print(string[::])
print(string.startswith('H'))
print(string.endswith('H'))
print(string.lower())
print(string.upper())
print(string.split(' '))

name = 'ahmad'
age = 50
if name == 'ahmad':
    print('your name is ahmad')

if name == 'ahmad' and age == 20:
    print('your name is ahmad and your age is 20');

if name == 'ahmad' or name == 'ali':
    print('your name is ahmad or ali');

if name in ['ali', 'ahmad', 'mohammad']:
    print('your name is in the list')

ourarray = [1,2,3,4,5,6,7,8,9,10]
another = [1,2,3,4,5,6,7,8,9,10]
print(ourarray == another)#true
print(ourarray is another)#false
print(not False)#true

#loops
users = ['ali', 'ahmad', 'mohammad']
for user in users:
    print(user)
# for users in range(2):
#     print(user)

for num in range(5):
    print(num)
else:
    print('the loop is finished in 4')

count = 0
while len(users) > 1:
    print(count)
    if(count == 2): break
    count+=1

while count > 1:
    print('this is count:', count)
    count -=1
else:
    'now the count is less then 1'
    count-=1

#dictionary
phones = {'ahmad': 123, 'ali': 456, 'mohammad': 789}
print(phones['ahmad'])
phones['sara'] = 101112
del phones['ali']
phones.pop('ahmad')
for name,number in phones.items():
    print(name, number)
print(phones.items())

# input1=input('enter your name: ')
# print('hello ', input1)

# input2 = int(input('enter a number: '))
# print('your number +5 is: ', input2+5)
# array = input('enter numbers with comma: ')
# print(array.split(','))
# for item in array.split(','):
#     print(int(item))

# Taking the name input using input()
# name = input("Enter your name: ")

# Taking the age input using input() and converting it to integer
# age = int(input("Enter your age: "))

# Taking the country input using input()
# country = input("Enter your country: ")

# Displaying the formatted sentence with name, age, and country
# print("Hello, my name is {}, I am {} years old, and I am from {}.".format(name, age, country))

