# Started at 5:48 2-5-2022

list_in_list = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
print(list_in_list[0][1])
print(list_in_list[1][1])
print(list_in_list[2][1])
print(list_in_list[3][1])
print(list_in_list[4][1])

animals = ['cow', 'pig', 'dog', 'sheep', 'cat']
print('cow' in animals)
print('goat' in animals)
print('sheep' in animals)

animals = ['cow', 'pig', 'dog', 'sheep', 'cat']
print(not 'cow' in animals)
print('goat' not in animals)
print(not 'sheep' in animals)
print('cat' not in animals)

animals = ['cow', 'pig', 'dog', 'sheep', 'cat']

if 'cow' in animals:
    print("Cows are animals!")
else:
    print("Cows are not in the list")

# while 'goat' not in animals:
    # print('put goats in the list!')

x = 'YouTube'

if 'Y' in x:
    print("This is going to be printed.")
if 'u' not in x:
    print("This will never be printed.")
# while 'goat' not in animals:
    # print('put goats in the list!')

empty_list = []
empty_list.append(10)

print(empty_list[0])

nums = [10, 20, 30, 40]

nums.append('sixty')
print(nums)

nums.append(50)
print(nums[-1])

nums = [10, 20, 30, 40]
nums2 = list(nums)
array_2D = []
nums.append('sixty')
print(nums)

nums.append(50)
print(nums[-1])

array_2D.append(nums)
array_2D.append(nums2)

print(array_2D)

print(array_2D[0][4])
print(array_2D[1][1])

animals = ['chicken', 'cow', 'penguin', 'tiger']

animals.insert(0, 'goat')
print(animals)

animals.insert(-1, 'donkey')
print(animals)

animals = ['chicken', 'cow', 'penguin', 'tiger', 'koala']
print(len(animals))

animals = ['chicken', 'cow', 'penguin', 'tiger', 'koala']
length = len(animals)
for i in range(length):
    print(animals[i])

letters = ['a', 'c', 'e', 'f', 'g']
print(letters.index('a'))
print(letters.index('e'))
print(letters.index('g'))


nums = [10, 20, 30, 40]

nums.remove(20)
print(nums)

# nums.remove(90)

desserts = ['cookies', 'brownies', 'pies', 'cheesecake']

print('pies' in desserts)
print('cake' in desserts)
print('pies' in desserts)
print('ice cream' in desserts)

random = [32, 10, 29, 40]

random.append(13)
random.insert(1, 67)
random.remove(29)
random.append(98)

print(random)

numbers = [78.3, 27, 41.9, 68.7, 45, 12.2]

print(numbers.index(12.2))
print(numbers.index(78.3))
print(numbers.index(45))
print(len(numbers))

animal_list = []
animal_list.append('Duck')
animal_list.append('Orangatan')
animal_list.append('Kangaroo')
animal_list.append('Tucan')
animal_list.append('Humans')
print(animal_list)
print(animal_list.index('Duck'))
print(animal_list.index('Orangatan'))
print(animal_list.index('Kangaroo'))
print(animal_list.index('Tucan'))
print(animal_list.index('Humans'))

# Ended at 7:02 So for an hour an 1 hour and 13 minutes
# Going to do 47 minutes of Javascript and it wll total up to 2 hours.


# /usr/local/bin/python3 /Volumes/Transcend/wrkst.py
