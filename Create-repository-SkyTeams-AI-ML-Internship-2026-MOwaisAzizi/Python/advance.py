

def counter():
    for num in range(5):
      yield num

for value in counter():
  print(value)

# fibonoch
# def fib():
#     a, b = 0, 1
#     for num in range(10):
#         print(a)
#         a,b = b,a+b
# fib()
        
        # using yeil
def fib():
    a,b = 0, 1
    for num in range(10):
        yield(a)
        a,b = b,a+b

for number in fib():
  print(number)

word = 'this is the a great city in af'
words = word.split()
array_word_length = []

# for w in words:
#   if w != 'the':
#     array_word_length.append(len(w))

# print(words)
# print(array_word_length)

# comperhension way
array_word_length = [len(w) for w in words if w != 'the']
print(array_word_length)

# lamda function
sumLam = lambda x,y: x+y
sumnumber = sumLam(2,3);
print(sumnumber)


def callNumbers(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

callNumbers(1,2,3,4,5)

def operaton(first, second, third, **options):
    if options.get('action') == 'sum':
        print(first + second + third)
    if options.get('number') == 'first':
        print(first)
operaton(3,4,5, action = 'sum', number = 'first')

print(set('my name is owias and I am here with name and my'.split()))

print(set(['ali', 'ahmad', 'kdarim']))
print(set(['ali', 'karim']))

a = set(['one', 'tow', 'tree'])
b = set(['three', 'tow', 'five'])
print(a.intersection(b))
print(b.intersection(a))
print(a.symmetric_difference(b))
print(a.difference(b))
print(a.union(b))

import json
data = [1, 2, 3, "a", "b", "c"]
# encode obj json to string
json_string = json.dumps(data)
print(json_string)
print(len(json_string))
# decode string json to obj
print(json.loads(json_string))

import pickle
# encode to binary data
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickled_string)
# decode back data
print(pickle.loads(pickled_string))

from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print(p(8))

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))
print(type(Vehicle))
print(id(Vehicle))
# print(isinstance(Vehicle))
print(callable(Vehicle))

fruits = ['apple', 'banaban', 'orieng']
new_Fuits = []
for x in fruits:
    if 'a' in x:
        new_Fuits.append(x)
print(new_Fuits) 

arr = [3,2,3,4]
arr.sort(reverse = True)
print(arr)

string = 'this is string'
print('hello' not in string)

arr2 = [3,'hello',5,6]
arr2.append(66)
arr2.insert(2,55)
newArr = [56,5,5]
newArr.extend(arr2)
newArr.remove("hello")
newArr.pop(2)
del newArr[1]


print(newArr)
newArr.clear()
print(newArr)
del newArr
# print(newArr)

plays = ['foot', 'wall']
for p in range(len(plays)):
    print(plays[p])

i = 0
while ( i != len(plays)):
    print(plays[i])
    i += 1


new_Fuits = [x for x in plays if 'f' in x ]
print(new_Fuits)

mylist = [3,4,5]
copyList = mylist.copy()
copyList = list(mylist)

myTouple = ('apple',)
notTouple = ('apple')
print(type(myTouple))
print(type(notTouple))

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

sets  = {'ali', 'karim'}
sets2  = {'ali', 'karim'}
combine = sets.update(sets2)
print(combine)

# dictionary key value
# .values, .keys. items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

dictionary = {'name': 'ali', 'age': 4}
newDic = dictionary.copy()
for x,y in newDic.items():
    print(x,y)

myFruits = ['apple', 'orange']
iterator = iter(myFruits)
print(next(iterator))
print(next(iterator))

import myModule
myModule.greetAll()
print(myModule.person['name'])

import myModule as x
from myModule import person
# build in modules
import platform 
print(platform.system())
print(dir(platform))

import datetime
print(datetime.datetime.now())

print(datetime.datetime.now().year)
x = datetime.datetime(2020,4,5)
# print(datetime)

if not type(y) is int: 
    raise TypeError('y is not defined')

mytext = "this is {} car which is very {} and costs {:.2f}"
print(mytext.format('lamborgini', 'fast', 30000))