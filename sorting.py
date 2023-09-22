# bubble_sort#

'''
def bubble_sort(unsorted_lst):
    len_unsorted_lst = len(unsorted_lst)
    for i in range(len_unsorted_lst+1):
        for j in range(len_unsorted_lst-1):
            if unsorted_lst[j]>unsorted_lst[j+1]:
                unsorted_lst[j],unsorted_lst[j+1]=unsorted_lst[j+1],unsorted_lst[j]
                j+=1
    return unsorted_lst

lst = [14,46,43,27,57,41,45,21,70]
print(bubble_sort(lst))
'''

# unique number in given array

# i/p = [4,7,8,5,4,5] , o/p = [7,8]

# l = [4,7,8,5,4,5]
# res = []
# res2 =[]
# c=0
# for i in l:
#     if i not in res:
#         res.append(i)
#         c +=1
#         if c>=2:
#             pass
#         else:
#


# print(res)


# # initializing list
# test_list = [1, 5, 3, 6, 3, 5, 6, 1]
# #print("The original list is : " + str(test_list))
#
# res = []
# for i in test_list:
#     if i not in res:
#         res.append(i)
#
# # printing list after removal
# print("The list after removing duplicates : " + str(res))
#


# Write a program to print longest non repeated word in the sentence,
# s = "see and saw went to see a sea"
# d={}
#
# words = s.split()
# for word in words:
#     if words.count(word)==1:
#           d[word]=len(word)
#
# print(sorted(d.items(),key = lambda item: item[-1])[-1])


# s = "see and saw went to see a sea"
# words = s.split()
# d = {word: len(word) for word in words if words.count(word) == 1}
# print(sorted(d.items(), key=lambda item: item[-1])[-1])

#
# s = "apples"
# d={}
#
# if len(s)%2 == 0:
#     d[s]=ord(s[0])
#
# else:
#     d[s]=len(s)
#
# print(d)

# def is_prime(n):
#       for i in range(2,n):
#             if n%i ==0:
#                 print("not prime")
#                 break
#       else:
#              print("prime")
#
#
# is_prime(10)


# def is_primerange(n):
#     for i in range(10):
#         if n>1:
#             for i in range(2,n):
#                  if n % i == 0:
#                       print(i,"not prime")
#
#
#
#
#
# is_primerange(10)

# fibo
#
# a = 0
# b=1
#
# for i in range(10):
#     print(a,end = " ")
#     c=a+b
#     a=b
#     b=c
#
#
#
from collections import defaultdict

l = [98, 14, 62, 17, 56, 1, 5, 96]

# type1
# l1 = sorted(l)
# print(l1[-1])

# type2
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         l[i],l[i+1]=l[i+1],l[i]
# print(l)
# print(l[-1])

# nth largest

# type1
# l1 = sorted(l)
# print(l1)
# print(l1[5])

# type2
# n=5
# for _ in range(5):
#     for i in range(len(l)-1):
#         if l[i]>l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
# print(l)
# print(l[n])
#


# def dict_(sentence):
#     d={}
#     words = sentence.split()
#     for word in words:
#         if word not in d:
#             d[word]=1
#         else:
#             d[word]+=1
#
#     print(d)
#
#
# sentence = "hi how are you doing today"
# dict_(sentence)


# word and its count pair
# sentence = "hello hai hello how are you how are you hai hello my"
# d = {}
# #
# for word in sentence.split():
#     if word not in d:
#         d[word]=1
#     else:
#         d[word]+=1
#
# print(d)
# dd = defaultdict(int)
#
# for word in sentence.split():
#     dd[word] += 1
#
# print(dd)


# index and word pair
# sentence = "hello hai hello how are you how are you hai hello"
# d={}
# word = sentence.split()
# # for i in range(len(word)):
# #     d[i]=word[i]
# #
# # print(d)
#
# for index,item in enumerate(word):
#     d[index]=item
#
# print(d)
#

# convert 2 lists into a dictionary
l1 = ["hello", "world"]
l2 = [10, 20]
d = {}

# using zip
# for item1,item2 in zip(l1,l2):
#     d[item1]= item2
#
# for loop

# for i in range(len(l1)):
#     d[l1[i]]=l2[i]
#
#
# print(d)

# reversing an iterable
# s="hello"
# #
# # print(s[::-1])
#
# res = ""
#
# for char in s:
#     res = char+res
#
# print(res)

#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# d={}
# for item1,item2 in zip(l1,l2):
#     d[item1]=item2
# print(d)
# print(dict(zip(l1,l2)))
#
#
# temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}
#
# print(temperatures.items())

# # program to print all the vowels in the given string
# string = "hello world i e u"
# i = 0
#
# while i<len(string):
#     if string[i] in "aeiou":
#        print(string[i])
#     i+=1
# #
# for char in string.lower():
#     if char in "aeiou":
#         print(char)

# to print numbers from 10 to 1

# i=10
#
# while i>=1:
#     print(i)
#     i-=1

# to print even numbers in the range 1 to 50

# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i+=1

# print
# index and element
# l = ["walmart", "google", "flipkart", "amazon", "gmail", "yahoo"]
# len_ = len(l)
# for i in range(len_):
#     print(l[i],i)

# to print the numeric values in the given string
# using inbuilt method
# s = "abc1983jkhs234"
# for char in s:
#     if char.isdigit():
#         print(char)

# print
# all
# repeated
# characters
# s = "hello world"
# res = ""
# for char in s:
#     if s.count(char)>1:
#         print(char)

# to remove the duplicate/repeated characters in the given string

# s = "hello world"
# res = ""
# for char in s:
#     if s.count(char)==1:
#         res=res+char
#
# print(res)

#correct
# for char in s:
#     if char not in res:
#         res += char
# print(res)
# print duplicate characters without using inbuilt methods

# s = "hello world hell"
# non_duplicates = ""
# duplicates = ""
#
# for char in s:
#     if char not in non_duplicates:
#         non_duplicates = non_duplicates+char
#     else:
#         duplicates = duplicates+char
# print(non_duplicates)
# print(duplicates)

# to print all the indices of the given substring
#
# s = "hello world"
# character = "o"
#
# for i in range(len(s)):
#     if s[i]==character:
#         print(i)

