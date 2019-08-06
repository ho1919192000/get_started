# arr = [1, -10, 10, 31, -100, 56, 982, 102]
#
# def maxInArr(i):
#     if i > 20:
#         return True
#     else:
#         return False
#
# def smInArr(arr):
#     smallNum = None
#     for i in arr:
#         if smallNum is None:
#             smallNum = i
#         elif i < smallNum:
#             smallNum = i
#     return  smallNum

# def smInArr(arr):
#     smallNum = arr[0]
#     for i in arr:
#         if i < smallNum:
#             smallNum = i
#     return  smallNum

# print(smInArr(arr))
#
# print(list(filter(maxInArr, arr)))

# a = 'apple'
# index = 0
# while index < len(a):
#     print( index ,a[index])
#     index +=1

# count = 0
# for i in a:
#     if i == 'p':
#         count += 1
# print(count)
#
# print(a[1:3])
#
# print('s' in a)
#
# print(a[0:1].upper() + a[1:])
#
# print(a.capitalize())
#
# print(a.find('e'))
#
# print(a.find('x'))
#
# print(a.replace('p', 'g'))
#
# print(a.replace('pp', 'g'))
#
# print(a.startswith('a'))
# print(dir(a))
# data = 'howard@gmail.com Sun Mar 11 k12:00:23 2019'
#
# atpos = data.find('@')
# dotpos = data.find('.')
#
# host = data[atpos+1: dotpos].capitalize()
#
# print(host)
#
# x = u'你好'
#
# print(type(x))
#
# text = "X-DSPAM-Confidence:    0.8475"
# print(float(text[text.find(' '):]))

# File

# xfile = open('hello.txt')
# count = 0
#
# for line in xfile:
#     print(line)
#     count = count + 1
# print('Line Count:', count)
# .rstrip() remove newline
# for line in xfile:
#     line = line.rstrip()
#     if not '@toolcase' in line:
#         continue
#     print(line)
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened', fname)
#     quit()
#
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
#         print(line)
# print('There were', count, 'subject lines in', fname)

# Use the file name mbox-short.txt as the file name
# count = 0
# # ans = 0
# # fname = input("Enter file name: ")
# # try:
# #     fh = open(fname)
# # except:
# #     print('File cannot be opened', fname)
# #     quit()
# # for line in fh:
# #     if not line.startswith("X-DSPAM-Confidence:"): continue
# #     line = line[line.find(':') + 1:].strip()
# #     count = count + 1
# #     ans = ans + float(line)
# # print('Average spam confidence:', ans/count)

# import this

# import turtle
#
# turtle.pensize(4)
# turtle.pencolor('red')
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.mainloop()

# import antigravity

# List
# friends = ['a', 'b', 'c']
# for friend in friends:
#     print(friend)
# print('done')
#
# print(friends[2])
#
# print(len(friends))
#
# print(list(range(4)))
#
# for i in range(len(friends)):
#     print(friends[i])
# x = ['d', 'e', 'f']
#
# print(friends + x)
#
# print(friends[:2])

# t = [9, 41, 12, 3, 74, 15]

# t.sort()
# print(t)
#
# print(5 in t)
# print(15 in t)

# print(t[:4])
#
# print(dir(list()))

# stuff = list()
# stuff.append('book')
# stuff.append('99')
# print(stuff)

# numbers = list()
# while True:
#     num = input('A number?')
#     if num == 'done': break
#     numbers.append(float(num))
# average = sum(numbers)/len(numbers)
# print(average)

# abc = 'a b c'
# abc = 'a;b;c'
# stuff = abc.split(';');
# print(stuff)

# fh = open('mbox-short.txt')
# for line in fh:
#     line.rstrip()
#     if line.startswith('From '):
#         world = line.split()
# print(world[1])
# print(world[1][world[1].find('@') + 1:])
#
# email = world[1]
# pieces = email.split('@')
# print(pieces[1])

# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see
# if the word is already in the list and if not
# append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

# fname = input("Enter file name: ")
# fh = open('romeo.txt')
# lst = list()
# for line in fh:
#     words = line.split()
#     for word in words:
#         if not word in lst:
#             lst.append(word)
# lst.sort()
# print(lst)

# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split()
# and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

# fh = open('mbox-short.txt')
# count = 0
# for line in fh:
#     if line.startswith('From '):
#         print(line)
#         print(line.split()[1])
#         count = count + 1
#
#
# print("There were", count, "lines in the file with From as the first word")

# purse = dict()
# purse['money'] = 3
# purse['candy'] = 13
# purse['candy'] = purse['candy'] + 2
# print(purse)
#
# counts = dict()
# names = ['h', 'd', 'c', 'e', 'h', 'c', 'd', 'h']

# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts['h'])
#
# if name in counts:
#     x = counts[name]
# else:
#     x = 0
#
# x = counts.get('c', 0)
# print(x)

# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# counts = dict()
# texts = input('texts?')
# words = texts.split()
#
# for word in words:
#     counts[word] = counts.get(word, 0) + 1

# print(word)
# print(counts)
# for key in counts:
#     print(str(key) + ': ' + str(counts[key]))
# print(list(counts))
# print(counts.keys())
# print(counts.items())
# for a, b in counts.items():
#     print(a, b)

# mbox-short.txt
# name = input('file name?')
# fh = open(name)
# counts = dict()
# for line in fh:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# bigWord = None
# bigCount = None
#
# for key, value in counts.items():
#     if bigCount is None or bigCount < value:
#         bigWord = key
#         bigCount = value
# print(bigWord, bigCount)

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# counts = dict()
# for line in handle:
#     if line.startswith('From:'):
#         address = line.split()[1]
#         counts[address] = counts.get(address, 0) + 1
# proAddress = None
# proCount = None
# # print(counts.items())
# for key, val in counts.items():
#     if proCount is None or val > proCount:
#         proAddress = key
#         proCount = val
# print(proAddress, proCount)
# # for key in counts:
# #     print(key, counts[key])

# print(dir(list()))
#
# print(dir(tuple()))

d = dict()
d['a'] = 2
d['b'] = 4
for (k, v) in d.items():
    print(str(k) + ': ' + str(v))
